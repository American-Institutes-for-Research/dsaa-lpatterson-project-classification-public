import pandas as pd
import openai
from gptutils import getKey, get_chatgpt_response
openai.api_key = getKey()
import time

df = pd.read_excel("data/projects_to_review_w_abstracts.xlsx", index_col= 0)
df = df.dropna(subset='abstract')

template = '''
    You are reviewing project abstracts to detect if this project is related to public health. You are a public health
    expert.
    
    Here's a definition to use: the science of protecting and improving the health of people and their 
    communities through promotion of healthy lifestyles, research for disease and injury 
    prevention, and detection and control of infectious diseases. Public health 
    professionals work to prevent problems from happening or recurring by implementing educational 
    programs, recommending policies, administering services, and conducting research. 
    Public health is concerned with protecting the health of entire populations, ranging 
    from a local neighborhood to an entire country or region of the world. Public health also 
    works to limit health disparities and promote health care equity, quality, and accessibility. 
    
    Classify whether or not this abstract is related to public health. Some records may not have any text or may have 
    text that is not really an abstract. In those cases, return "unknown". Otherwise, return "Yes" if it is an abstract
    related to public health and "No" if it is not related to public health. 
    
    Return you response in the following format, replacing the values in brackets with your response:
    "Verdict: [Yes/No/Unknown] 
     
    Justification: [Explain why you chose your verdict]
    "
    
    Here is the abstract: 
'''

for n, row in df.iterrows():
    print(n)
    prompt = template + row['abstract']
    response = get_chatgpt_response([prompt]).return_response()
    if 'Verdict:' in response and 'Justification:' in response:
        response2 = response.replace('Verdict:','').replace(f'\n\n','').split('Justification:')
        verdict = response2[0].strip()
        justification = response2[1].strip()
        df.loc[n, 'public_health_flag'] = verdict
        df.loc[n, 'flag_justification'] = justification
    else:
        df.loc[n, 'public_health_flag'] = "Bad response"
        df.loc[n, 'flag_justification'] = response
    time.sleep(1)
    pass

df.to_excel('data/projects_chatgpt_flags.xlsx', index = False)
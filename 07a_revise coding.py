import pandas as pd
import time
from gptutils_10 import get_chatgpt_response
from sklearn.metrics import classification_report, cohen_kappa_score

df = pd.read_excel('data/projects_chatgpt_flags_tagged expansive thinking_areas_one shot.xlsx')

filt_df = df.loc[df.public_health_cat == 'Education (e.g., safe and healthy schools)']

template = '''
    You are reviewing education project abstracts believed to be possibly related to public health. However, the classifier  
    used for these projects is often falsely flagging these kinds of projects. You are a public health
    expert who is reexamining the abstracts to confirm their finding. Confirm the flag only if you see a direct relationship
    between the project and public health.
    
    Here's a definition to use: the science of protecting and improving the health of people and their 
    communities through promotion of healthy lifestyles, research for disease and injury 
    prevention, and detection and control of infectious diseases. Public health 
    professionals work to prevent problems from happening or recurring by implementing educational 
    programs, recommending policies, administering services, and conducting research. 
    Public health is concerned with protecting the health of entire populations, ranging 
    from a local neighborhood to an entire country or region of the world. Public health also 
    works to limit health disparities and promote health care equity, quality, and accessibility. 
    
     
    
    Return you response in the following format, replacing the values in brackets with your response:
    "Verdict: [Yes/No/Unknown] 
     
    Justification: [Explain why you chose your verdict]
    '''
overturn_count = 0
for n, row in filt_df.iterrows():
    print(n)
    prompt = template + row['abstract']
    response = get_chatgpt_response([prompt]).return_response()
    if 'Verdict:' in response and 'Justification:' in response:
        response2 = response.replace('Verdict:','').replace(f'\n\n','').split('Justification:')
        verdict = response2[0].strip()
        justification = response2[1].strip()
        df.loc[n, 'public_health_flag'] = verdict
        df.loc[n, 'flag_justification'] = justification
        if df.loc[n, 'public_health_flag'] != 'Yes':
            overturn_count += 1
            df.loc[n, 'public_health_cat'] = pd.NA
            print('overturned:', overturn_count)
    time.sleep(1)

df.to_excel('data/final_flags_cats.xlsx',index=False)

gpt_df = df.copy()
gpt_df = gpt_df.loc[gpt_df.public_health_flag != 'Unknown']
human_df = pd.read_excel("data/human_tags.xlsx")
human_df = human_df.loc[human_df['Public Health?'].isna() == False]
human_df = human_df[['Project Number','Public Health?','If Y, subcategory']]
human_df = human_df.rename({'Public Health?':'human_ph_flag',
                            'If Y, subcategory':'human_ph_cat'}, axis = 1)
human_df['human_ph_flag'] = human_df['human_ph_flag'].replace({'N':'No','Y':'Yes'})
gpt_df = gpt_df[['Project Number', 'abstract','public_health_flag','flag_justification', 'public_health_cat']]
gpt_df.columns = ['Project Number', 'abstract', 'bot_ph_flag', 'flag_justification', 'bot_ph_cat']
df = gpt_df.merge(human_df, on='Project Number')
df['cat_match'] = df.human_ph_cat == df.bot_ph_cat
df.loc[(df.bot_ph_flag!='Yes') | (df.human_ph_flag!='Ye'), 'cat_match'] = pd.NA

result_df = pd.DataFrame()
# print('human-bot public health flag cohen K')
result_df.loc['human-bot public health flag','cohen K'] = cohen_kappa_score(df['human_ph_flag'], df['bot_ph_flag'])
result_df.loc['human-bot public health flag','N'] = df.shape[0]

h2_df = pd.read_excel('data/for_second_tagging.xlsx')
h2_df = h2_df[['Project Number', 'abstract','Public Health?', 'If Y, subcategory','ph_flag_2', 'ph_cat2']]
h2_df = h2_df.rename({'Public Health?':'human_ph_flag',
                            'If Y, subcategory':'human_ph_cat'}, axis = 1)
# print('human-human public health flag cohen K')
result_df.loc['human-human public health flag','cohen K'] = cohen_kappa_score(h2_df['human_ph_flag'], h2_df['ph_flag_2'])
result_df.loc['human-human public health flag','N'] = h2_df.shape[0]

filt_df = df.loc[(df.bot_ph_flag=='Yes') & (df.human_ph_flag=='Yes') & (df['human_ph_cat'].isna() == False) & (df['bot_ph_cat'].isna() == False)]
# print('human-bot public health category cohen K')
result_df.loc['human-bot public health category','cohen K'] = cohen_kappa_score(filt_df['human_ph_cat'], filt_df['bot_ph_cat'])
result_df.loc['human-bot public health category','N'] = filt_df.shape[0]

filt2_df = h2_df.loc[(h2_df.ph_flag_2=='Y') & (h2_df.human_ph_flag=='Y')]
# print('human-human public health category cohen K')
result_df.loc['human-human public health category','cohen K'] = cohen_kappa_score(filt2_df['human_ph_cat'], filt2_df['ph_cat2'])
result_df.loc['human-human public health category','N'] = filt2_df.shape[0]
result_df.to_excel('output/final performance test_expansive.xlsx')

pd.crosstab(df.bot_ph_flag, df.human_ph_flag).to_csv('output/final disagreement xtab_expansive.csv')

flag_diffs = df.loc[(df.bot_ph_flag!=df.human_ph_flag)]
flag_diffs.to_excel('output/final flag disagreements_expansive.xlsx', index=False)
pass

pass


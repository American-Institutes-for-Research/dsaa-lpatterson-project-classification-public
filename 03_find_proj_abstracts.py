from utils import extract_text_from_pdf, extract_text_from_docx
import pandas as pd
import openai
from gptutils_10 import get_chatgpt_response

df = pd.read_excel('data/projects_to_review.xlsx')

template = '''
    You are scanning through project review reports. You are looking for the section that is the project
    abstract, which is a brief summary of the technical content of the project. Once you find it, return
    the abstract in your response and no other text.
    
    Text:
'''
error_counter = 0
#df = df.iloc[1900:,:]
for n, row in df.iterrows():
    print(n)
    proj_num = row['Project Number']
    ext = row['review_file'].split('.')[-1]
    try:
        if ext in ['doc', 'docx']:
            text = extract_text_from_docx(row['review_file'])
        elif ext == 'pdf':
            text = extract_text_from_pdf(row['review_file'])
        else:
            raise 'unexpected file type: ' + ext
    except Exception as e:
        print('error encountered with file:', row['Project Number'], 'Exception: ', e)
        error_counter += 1
        continue
    # make sure text is not too long
    if len(text) > 40000:
        text = text[:40000]
    prompt = template + text
    try:
        response = get_chatgpt_response([prompt], engine='gpt35-turbo-16k').return_response()
        df.loc[n, 'abstract'] = response
    except Exception as e:
        print('error getting chatgpt response:', e)
    if n % 100 == 0:
        df.to_excel("data/projects_to_review_w_abstracts_checkpoint.xlsx")
df.to_excel("data/projects_to_review_w_abstracts.xlsx")
pass
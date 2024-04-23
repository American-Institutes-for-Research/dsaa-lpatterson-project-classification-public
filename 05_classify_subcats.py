import pandas as pd
import openai
from gptutils import getKey, get_chatgpt_response
openai.api_key = getKey()
import time


df = pd.read_excel('data/projects_chatgpt_flags.xlsx')
filt_df = df.loc[df['public_health_flag'].str.lower().str.contains('yes')]
areas = [
    "Education (e.g., safe and healthy schools)",
    "Workforce (e.g., income inequality)",
    "Health system reform and improvement",
    "Health services (quality and delivery)",
    "Health equity",
    "Violence prevention and interruption",
    "Housing",
    "Aging and disability",
    "Food security",
    "Maternal and child health and welfare",
    "Substance use disorder",
    "Mental health and suicide prevention",
    "Diseases and vaccinations",
    "Environmental justice (e.g. water quality, pollution)",
    "Sexual and reproductive health",
    "Community design/urban planning/transportation",
    "None"
]

template = f'''
    You are reviewing abstracts for projects related to public health. Review the abstract below and determine
    which of the categories best applies to the abstract. Return only the category with which you feel is best.
    If none of the categories are appropriate, return the "None" category.
    
    Categories:{areas}
    
    Abstract:
'''

for n, row in filt_df.iterrows():
    print(n)
    prompt = template + row['abstract']
    response = get_chatgpt_response([prompt]).return_response()
    df.loc[n, 'public_health_cat'] = response
    time.sleep(1)

def clean_cats(s):
    for a in areas:
        if not pd.isna(s) and a in s:
            clean_s = a
            return clean_s

df['public_health_cat'] = df['public_health_cat'].apply(clean_cats)

df.to_excel('data/projects_chatgpt_flags_tagged.xlsx',index=False)
pass
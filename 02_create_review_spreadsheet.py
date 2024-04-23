# create spreadsheet of relevant information for humans/ChatGPT to review
import pandas as pd
import os
from utils import extract_text_from_pdf, extract_text_from_docx

df = pd.read_excel('data/ProjectTags.xlsx')
projects = os.listdir('reviews/')
df = df.loc[df['Project Number'].isin(projects)]

keep_cols = ['Last Update', 'Updated By', 'Project Number', 'Project Title',
       'Client', 'Project Director', 'Start Date', 'End Date', 'Service Area',
       'Sub-Service Area', 'Practice Area', 'Primary Focus']

df = df[keep_cols]
for n, row in df.iterrows():
       files = os.listdir(os.path.join('reviews/', row['Project Number']))
       if len(files) > 0:
              file = files[0]
              df.loc[n, 'review_file'] = os.path.join('reviews/', row['Project Number'], file)
              split_file = df.loc[n, 'review_file'].split('.')
              df.loc[n, 'file_ext'] = split_file[-1]

df = df.dropna(subset='review_file')
print(df['file_ext'].value_counts())

df.to_excel('data/projects_to_review.xlsx', index=False)
pass
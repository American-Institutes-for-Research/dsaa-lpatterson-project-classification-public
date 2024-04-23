# pull a project review document for each project
import os
import pandas as pd
from utils import extract_text_from_pdf, extract_text_from_docx
import shutil
root = os.path.join(r'C:\Users\lpatterson\AIR\AIR Project Review System (PRS) - Project Document Sets')
folders = os.listdir(root)

# track results
no_files_found = []
no_reviews_found = []
latest_reviews = {}
file_counter = 0
for folder in folders:
    fpath = os.path.join(root, folder)
    try:
        files = os.listdir(fpath)
    except NotADirectoryError as e:
        print(fpath, 'does not exist')
        continue
    if len(files) == 0:
        no_files_found.append(folder)
    else:
        # sort in date modified order
        files.sort(key=lambda x: os.path.getmtime(os.path.join(fpath, x)), reverse=True)
        # find the latest project review document for the project
        found = False
        # seems to match one of these two patterns
        for file in files:
            pattern1 = ('project' in file.lower()) & ('review' in file.lower()) & ('checklist' not in file.lower())
            pattern2 = ('project' in file.lower()) & ('director' in file.lower()) & ('checklist' not in file.lower())

            filepath = os.path.join(fpath, file)
            if os.path.isfile(filepath):

                file_ext = file.split('.')[-1].lower()
                if (pattern1 or pattern2) and (file_ext in ['doc', 'docx']):
                    latest_reviews[folder] = file
                    found = True
                    file_counter += 1
                    print(file_counter)
                    if os.path.exists(os.path.join('reviews/',folder)) == False:
                        os.mkdir(os.path.join('reviews/',folder))

                    shutil.copy(filepath, os.path.join('reviews/',folder, file))
                    break

        # pdfs tend to be financials, so only take a pdf if there's no docx file
        if found is False:
            for file in files:
                pattern1 = ('project' in file.lower()) & ('review' in file.lower()) & ('checklist' not in file.lower())
                pattern2 = ('project' in file.lower()) & ('director' in file.lower()) & ('checklist' not in file.lower())

                filepath = os.path.join(fpath, file)
                if os.path.isfile(filepath):
                    file_ext = file.split('.')[-1].lower()
                    if (pattern1 or pattern2) and (file_ext in ['pdf']):
                        latest_reviews[folder] = file
                        found = True
                        file_counter += 1
                        print(file_counter)
                        if os.path.exists(os.path.join('reviews/', folder)) == False:
                            os.mkdir(os.path.join('reviews/', folder))

                        shutil.copy(filepath, os.path.join('reviews/', folder, file))
                        break


pass
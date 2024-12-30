import os
from dotenv import load_dotenv
import pandas as pd
import ast
from utils.data_processing import Dataset
import google.generativeai as genai
from time import sleep
from tqdm import tqdm


def extractText(listDicts):
    result = ''
    for i in listDicts:
        result += f'{i["id"]}: {i["text"]}\n'
    return result

if __name__=='__main__':
    load_dotenv()
    df = pd.read_csv('~/project/python/gemini-api-synth-dataset/dataset/clean_v0.3_1118_unclass-only_formatted-lb.csv')
    dataset = Dataset(df)
    # dataset.applySliceEnd('long_answer', ['Referensi:', 'Dasar Hukum:'])
    # dataset.applyFormatLb('legal_basis')

    genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    SLEEP_INTERVAL = 15
    SLEEP_DURATION = 60  # seconds

    for i, row in enumerate(tqdm(dataset.data.itertuples())):
        idx = row.Index
        
        response = model.generate_content(f'''
From the PASSAGE below, try to recreate the ORIGINAL_TEXT for each one of the REFERENCES
Note:
- write in the same language as the PASSAGE which is bahasa Indonesia
- write between 80 to 100 words
- if there are litle to no information about the reference, try to construct an artificial one based on the title or author and the topic of the PASSAGE.
- maintain all factual informations and keeping the same flow of information.
- do not write any addition.

PASSAGE:
{row.long_answer}

REFERENCES:
{extractText(ast.literal_eval(row.legal_basis))}
ORIGINAL_TEXT:
        ''')
        
        dataset.data.at[idx, 'fulltext'] = response.text
        print(f'update at row = {idx}, status: success')
        # Sleep every SLEEP_INTERVAL iterations
        if (i + 1) % SLEEP_INTERVAL == 0:
            sleep(SLEEP_DURATION)

    
    dataset.data.to_csv('../dataset/clean_v0.3_1118_final.csv')


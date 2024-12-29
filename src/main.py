import os
from dotenv import load_dotenv
import pandas as pd
from utils.data_processing import Dataset
import google.generativeai as genai

if __name__=='__main__':
    load_dotenv()
    df = pd.read_csv('~/project/python/gemini-api-synth-dataset/dataset/clean_v0.3_1118_unclass-only.csv')
    dataset = Dataset(df)
    dataset.applySliceEnd('long_answer', ['Referensi:', 'Dasar Hukum:'])
    dataset.applyFormatLb('legal_basis')
    inputText = dataset.data.loc[2, 'legal_basis']
    print(inputText)
    
    # genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
    # model = genai.GenerativeModel('gemini-1.5-flash')
    # response = model.generate_content(f'write the summary of the following text in the same language: {inputText}')
    # print(response)


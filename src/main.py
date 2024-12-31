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

def main():

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



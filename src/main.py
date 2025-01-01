import os
from dotenv import load_dotenv
from models.llm_client import GeminiClient
from utils.data_processing import Dataset
from tasks.recreate_from_ref import RecreateFromReference

if __name__=='__main__':
    dataset_df = Dataset('~/project/python/gemini-api-synth-dataset/dataset/clean_v0.3_1118_final.csv', **{'index_col':0})
    
### this should go in test, ik ###

    load_dotenv()
    client = GeminiClient(
        my_api_key=os.getenv('GOOGLE_API_KEY'),
        rate_limit=15
    )

    # Task specific
    task = RecreateFromReference(
        client=client,
        ref_df=dataset_df
    )

    prompts = task.build_prompt_list(
        column_document='long_answer',
        column_ref='legal_basis'
    )

    output_df = task.recreate(
        prompts=prompts,
        column_target='fulltext'
    )

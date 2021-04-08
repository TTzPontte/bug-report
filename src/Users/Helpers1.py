# %%
import requests
import boto3
import os

ENV = os.getenv("ENV") or 'dev'
ssm_client = boto3.client('ssm')

API_KEY = ssm_client.get_parameter(
    Name=f'/airtable/{ENV}/bug_api_key'
)
base_url = 'https://api.airtable.com/v0'

base_id = 'appyxraZ9ECUTtWRI'


def helper_get_all(table_name):
    response = requests.get(
        url=f'{base_url}/{base_id}/{table_name}?api_key={API_KEY}'
    )
    return response.json()


# def get_table():
def get_table(table):
    switcher = {
        'bugs': helper_get_all('Bugs').get('records'),
        'members': helper_get_all('Membros').get('records'),
        'requester': helper_get_all('Reportado por').get('records')
    }
    return switcher.get(table, "Invalid table")

# %%
import requests
import boto3
import os

ENV = os.getenv("ENV") or 'dev'
ssm_client = boto3.client('ssm')

API_KEY = 'keyeVk6MVJj1N0ZIZ'

    # ssm_client.get_parameter(
    # Name=f'/airtable/{ENV}/bug_api_key'
# )

base_url = 'https://api.airtable.com/v0'

base_id = 'appyxraZ9ECUTtWRI'


def helper_get_all(table_name):
    response = requests.get(
        url=f'{base_url}/{base_id}/{table_name}?api_key={API_KEY}'
    )
    print(f'response: {response}')
    return response.json()


# def get_table():
def get_table(table):
    switcher = {
        'bugs': helper_get_all('Bugs').get('records'),
        'members': helper_get_all('Membros').get('records'),
        'requester': helper_get_all('Reportado por').get('records')
    }
    return switcher.get(table, "Invalid table")


response = get_table(table='requester')


def build_users_list(requester_table):
    users = []
    for i in requester_table:
        item = i.get('fields')
        users.append({
            "id": i["id"],
            "Email": item["Email"],
            "Name": item["Name"],
            "Time": item["Time"],
        })
    return users

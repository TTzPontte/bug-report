# %%
import requests
import boto3
import os

ENV = os.getenv("ENV") or 'dev'
# table_name = 'Bugs'
ssm_client = boto3.client('ssm')

# API_KEY = ssm_client.get_parameter(
#     Name=f'/airtable/{ENV}/bug_api_key'
# )

API_KEY = 'keyeVk6MVJj1N0ZIZ'


def helper_get_all(table_name):
    response = requests.get(
        url=f'https://api.airtable.com/v0/appyxraZ9ECUTtWRI/{table_name}?api_key={API_KEY}'
    )
    return response.json()


bugs_table = helper_get_all('Bugs').get('records')
members_table = helper_get_all('Membros').get('records')
requester_table = helper_get_all('Reportado por').get('records')


def build_users_list():
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


print(f'bugs_table, {bugs_table}')
print(f'members_table, {members_table}')

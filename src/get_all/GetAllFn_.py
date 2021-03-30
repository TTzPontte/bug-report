# %%

import os

import boto3
import requests

ENV = os.getenv("ENV") or 'dev'
ssm_client = boto3.client('ssm')

API_KEY = os.getenv('AIRTABLE_API_KEY')


# API_KEY = ssm_client.get_parameter(
#     Name=f'/airtable/{ENV}/bug_api_key'
# )
# %%
def get_members():
    members_table = 'Membros'
    return helper_get_all(members_table)

# %%
def get_bugs():
    table_name = 'Bugs'
    return helper_get_all(table_name)


def helper_get_all(table_name):
    response = requests.get(
        url=f'https://api.airtable.com/v0/appyxraZ9ECUTtWRI/{table_name}?api_key={API_KEY}'
    )
    return response.json()


table_name = 'Bugs'
response = helper_get_all(table_name)
print(f'response:  {response}')

# class GetAll(event, context):
#     def handler(self):
#         return helper_get_all()


# def handler(event, context):
#     GetAll(event, context).run()

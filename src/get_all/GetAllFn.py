import requests
import boto3
import os

ENV = os.getenv("ENV") or 'dev'
table_name = 'Bugs'
ssm_client = boto3.client('ssm')

API_KEY = ssm_client.get_parameter(
    Name=f'/airtable/{ENV}/bug_api_key'
)


def helper_get_all():
    response = requests.get(
        url=f'https://api.airtable.com/v0/appyxraZ9ECUTtWRI/{table_name}?api_key={API_KEY}'
    )
    return response.json()


class GetAll(event, context):
    def handler(self):
        return helper_get_all()


def handler(event, context):
    GetAll(event, context).run()

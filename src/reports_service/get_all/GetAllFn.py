import requests
import boto3
import os
from common.handlebase import Handler

from dao import ReportDao

class GetAllReports(Handler):
  def handler(self):
    report_dao = ReportDao()
    items = report_dao.get_all()

def handler(event, context):
  return GetAllReports(event, context).run()
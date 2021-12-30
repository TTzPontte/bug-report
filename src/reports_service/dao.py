import os
import boto3
import botocore

from model import ReportModel

boto_error = botocore.exceptions.ClientError

table_name = os.getenv('BUG_REPORTS_DB')
client = boto3.client('dynamodb')

class ReportDao:
  def __init__(self):
    self._table = table_name

    def get_all(self):
        try:
            response = self._renegotiation_table.scan()
        except boto_error as exc:
            print(
                "não foi possivel recuperar o recurso: %s",
                exc, exc_info=1
            )
            return None
        if not response["Items"]:
            return None
        else:
            return response["Items"]

  def create(self, item):
    try:
      json_data = json.dumps(item)
      report_schema = marshmallow_dataclass.class_schema(ReportModel)()
      report_schema.loads(json_data)
      new_report = report_schema.dumps(item)

      self._table.put_item(
          Item=new_report,
      )

    return new_report["id"]
    except boto_error as exc:
        print(
            "não foi possivel persistir o objeto no banco de dados: %s",
            exc, exc_info=1
        )
        return None
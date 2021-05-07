# %%
import json
import marshmallow_dataclass

from uuid import uuid4
from dataclasses import dataclass
from marshmallow import fields

@dataclass
class ReportModel():
  priority: str
  location: int
  files: str
  description: str
  requested_by: str
  handled_by: str
  title: str = fields.String()
  id: str = uuid4()

# %%
obj = {
  'title': 0,
  'priority': 'str',
  'location': 'int',
  'files': 'str',
  'description': 'str',
  'requested_by': 'str',
  'handled_by': 'str',
}
# %%
json_data = json.dumps(obj)
property_schema = marshmallow_dataclass.class_schema(ReportModel)()
property_schema.loads(json_data)
# %%

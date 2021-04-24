# %%

from dataclasses import dataclass


@dataclass
class File:
    id: str
    filename: str
    size: int
    type: str
    url: str


@dataclass
class Fields:
    attachments: File
    location: list
    bug_name: str
    requested_by: list
    description: str
    created_at: str
    days_opened: int


@dataclass
class Report:
    id: str
    fields: Fields
    createdTime: str


# %%

from marshmallow import Schema, fields


class FileSchema:
    id: fields.Str()
    filename: fields.Str()
    size: fields.Int()
    type: fields.Str()
    url: fields.Str()


class FieldsSchema(Schema):
    files: fields.Nested(FileSchema)
    createdAt: fields.Str()
    desciption: fields.Str()
    daysOpened: fields.Int()
    location: fields.List
    title: fields.Str()
    timeStamp: fields.Str()
    priority: fields.Str()
    requestedBy: fields.List
    type: fields.Str()


class ReportSchema(Schema):
    id = fields.Str()
    createdTime = fields.Str()
    fields = fields.Nested(FieldsSchema)

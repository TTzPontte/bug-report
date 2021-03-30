# %%
import pprint
from dataclasses import dataclass

pp = pprint.PrettyPrinter(indent=4)
WORDS = {
    "Anexos": "files",
    "Local": "location",
    "Nome do Bug": "title",
    "Reportado por": "requested_by",
    "Descrição": "desciption",
    "Data de abertura": "created_at",
    "Dias em aberto": "days_opened",
}


def change_keys(obj, convert):
    """
    Recursively goes through the dictionary obj and replaces keys with the convert function.
    """
    if isinstance(obj, (str, int, float)):
        return obj
    if isinstance(obj, dict):
        new = obj.__class__()
        for k, v in obj.items():
            if k in convert:
                new[convert[k]] = change_keys(v, convert)
            else:
                new[k] = change_keys(v, convert)
    elif isinstance(obj, (list, set, tuple)):
        new = obj.__class__(change_keys(v, convert) for v in obj)
    else:
        return obj
    return new


@dataclass
class Fields:
    files: list
    location: list
    bug_name: str
    requested_by: list
    description: str
    created_at: str
    days_opened: int


@dataclass
class Report:
    id: str
    fields: dict
    createdTime: str


@dataclass
class BugReport:
    records: list

    def total_reports(self):
        return len(self.records)

    def teams(self):
        records_list = self.records
        ameno = []
        dorime = []
        no_squad = []
        for record in records_list:
            print(record)
            fields = record.get('fields', None)
            squad = fields.get('Squad', None)
            if squad == 'Ameno':
                ameno.append(record)
            elif squad == 'Dorime':
                dorime.append(record)
            else:
                no_squad.append(record)

        return {"Ameno": ameno, "Dorime": dorime, "noSquad": no_squad}

    def by_location(self):
        locations = {}
        obj = dict()
        for i in self.records:
            fields = i.get('fields')
            print(f"fields :: {fields}")

            # for field in fields:
            location = fields['Local']
            print(f"location :: {location}")

            existing_array = []
            if existing_array.__contains__(location):
                ll = locations[location]
                locations[location] = ll.extend(fields['id'])
            else:
                existing_array.extend(location)
        return obj


def handler(data):
    bug_reports = change_keys(data, WORDS)
    BugReport(bug_reports)


str_data = {
    "records": [
        {
            "id": "rec0rH0qMm7diK8Ls",
            "fields": {
                "Anexos": [
                    {
                        "id": "att8N0znSg6GJtp3S",
                        "url": "https://dl.airtable.com/.attachments/4a708424cdab64ff7249fa616284fffb/08dc574e/flYo4CmzTzmXQ_n4yk0ZrQ",
                        "filename": "flYo4CmzTzmXQ_n4yk0ZrQ",
                        "size": 1464,
                        "type": "text/html"
                    }
                ],
                "Local": [
                    "Torre de controle - HE"
                ],
                "Nome do Bug": "Tagear operação",
                "Reportado por": [
                    "recWzW16YZt3LY9Xx"
                ],
                "Descrição": "Tagear a operação: https://torrecontrole.pontte.com.br/contracts/flYo4CmzTzmXQ_n4yk0ZrQ como \u0027\u0027best\u0027\u0027",
                "Opened date \u0026 time (GMT)": "2021-02-11T16:50:29.000Z",
                "Data de abertura": "02-11-21",
                "Dias em aberto": 21
            },
            "createdTime": "2021-02-11T16:50:29.000Z"
        },
    ]
}

records = str_data["records"]
# b_report = handler(data)
# reports = BugReport(records)

for i in records[0]['fields']:
    print(f"{i} --- {records[0]['fields'][i]}")

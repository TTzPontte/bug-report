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

    def total_reports(self) -> int:
        return len(self.records)

    def by_location(self):
        locations_return = {}
        obj = dict()
        existing_array = []
        for record in self.records:
            print(f'existing_array: {existing_array}')
            fields = record.get('fields')
            # for field in fields:
            locations = fields['Local']
            pp.pprint(locations)
            for location in locations:
                if existing_array.__contains__(location):
                    ll = locations_return[location]
                    locations_return[location] = ll.extend(fields['id'])
                else:
                    locations_return[location] = record
                    existing_array.extend(location)
        return locations_return


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


def handler(data):
    bug_reports = change_keys(data, WORDS)
    BugReport(bug_reports)


# %%
# records = str_data["records"]
records = []
# b_report = handler(data)
# reports = BugReport(records)

for i in records[0]['fields']:
    print(f"{i} --- {records[0]['fields'][i]}")

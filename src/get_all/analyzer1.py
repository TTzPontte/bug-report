# %%
import pprint
from dataclasses import dataclass

pp = pprint.PrettyPrinter(indent=4)


@dataclass
class BugReport:
    records: list

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


# %%

records = [
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
    }
]
s = BugReport(records)
s.by_location()
# %%
# records = str_data["records"]
records =
# b_report = handler(data)
# reports = BugReport(records)

for i in records[0]['fields']:
    print(f"{i} --- {records[0]['fields'][i]}")

import pprint

pp = pprint.PrettyPrinter(indent=4)

WORDS = {
    "Anexos": "files",
    "Data de abertura": "createdAt",
    "Descrição": "description",
    "Dias em aberto": "daysOpened",
    "Local": "location",
    "Nome do Bug": "title",
    "Opened date & time (GMT)": "timeStamp",
    "Prioridade": "priority",
    "Reportado por": "requestedBy",
    "Tipo": "type",
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


# %%
item = {'id': 'rec0rH0qMm7diK8Ls', 'fields': {'Anexos': [{'id': 'att8N0znSg6GJtp3S',
                                                          'url': 'https://dl.airtable.com/.attachments/4a708424cdab64ff7249fa616284fffb/08dc574e/flYo4CmzTzmXQ_n4yk0ZrQ',
                                                          'filename': 'flYo4CmzTzmXQ_n4yk0ZrQ', 'size': 1464,
                                                          'type': 'text/html'}], 'Tipo': 'Feature',
                                              'Local': ['Torre de controle - HE'], 'Nome do Bug': 'Tagear operação',
                                              'Reportado por': ['recWzW16YZt3LY9Xx'],
                                              'Descrição': "Tagear a operação: https://torrecontrole.pontte.com.br/contracts/flYo4CmzTzmXQ_n4yk0ZrQ como ''best''",
                                              'Prioridade': 'Média',
                                              'Opened date & time (GMT)': '2021-02-11T16:50:29.000Z',
                                              'Data de abertura': '02-11-21', 'Dias em aberto': 72},
        'createdTime': '2021-02-11T16:50:29.000Z'}
ppp = change_keys(item, WORDS)

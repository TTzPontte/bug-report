from .get_helper import *
from .translate import *

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


def translate_keys(obj):
    return change_keys(obj, WORDS)

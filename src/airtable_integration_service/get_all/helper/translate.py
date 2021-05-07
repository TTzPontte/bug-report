class Translate:
  def __init__(self):
    self.WORDS = {
      "Anexos": "files",
      "Local": "location",
      "Nome do Bug": "title",
      "Reportado por": "requestedBy",
      "Descrição": "desciption",
      "Opened date & time (GMT)": "timestamp",
      "Data de abertura": "createdAt",
      "Dias em aberto": "daysOpened",
      "Tipo": "type",
      "Prioridade": "priority",
    }

  def change_keys(self, obj):
        """
    Recursively goes through the dictionary obj and replaces keys with the convert function.
    """

    convert = self.WORDS

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
def build_users_list(requester_table):
    users = []
    for i in requester_table:
        item = i.get('fields')
        users.append({
            "id": i["id"],
            "Email": item["Email"],
            "Name": item["Name"],
            "Time": item["Time"],
        })
    return users

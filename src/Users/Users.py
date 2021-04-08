from dataclasses import dataclass


@dataclass
class User:
    user_id: str
    name: str
    email: str


@dataclass
class Users:
    user_list: list
    table: str = 'requester'

    # user_list: list[User]

    def total_users(self):
        return len(self.user_list)

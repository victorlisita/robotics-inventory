class Log:
    def __init__(self, login: str, log_part: str, num: int):
        self.login = login
        self.log_part = log_part
        self.num = num


class User:
    def __init__(self, username: str, card: int):
        self.username = username
        self.card = card


class Part:
    def __init__(self, partname: str, sign_in: int, sign_out: int):
        self.partname = partname
        self.sign_in = sign_in
        self.sign_out = sign_out

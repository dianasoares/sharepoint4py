class Sharepoint4pyError(Exception):
    def __init__(self, msg, details=None):
        if details:
            super().__init__(f"{msg} : {details}")
        else:
            super().__init__(msg)


class Sharepoint4pyRequestError(Sharepoint4pyError):
    pass

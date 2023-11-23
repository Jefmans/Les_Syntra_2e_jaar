
class Company():
    def __init__(self, name, url) -> None:
        self.name = name
        self.url = url
    
    def __eq__(self, __value: object) -> bool:
        pass


class Job():
    def __init__(self, titel, company_name, company_url, email) -> None:
        self.titel = titel
        self.email = email

    


def remove_digit_part(string):
    for i, c in enumerate(string):
        if c.isdigit():
            string = string[:i-1]
            break
    return string.strip()
    

TYPES = ['fles', 'clip', 'blik']
def split_naam(string):
    naam = string
    for vol_type in TYPES:
        if vol_type in string:
            naam = string.replace(vol_type, '')
            return (naam, vol_type)
    return naam, 'None'


class Bier():
    def __init__(self, naam, type, url) -> None:
        self.naam = naam
        self.type = type
        self.url = url

    def set_prijs(self, prijs):
        self.prijs = prijs

    def __str__(self) -> str:
        return self.naam + ' - ' + self.url + ' - '  + str(self.prijs)
    
    def __eq__(self, other):
        return self.url == other.url

    def __hash__(self) -> int:
        return hash(self.url)
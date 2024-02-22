def main():
    all_vats = get_all_vats()
    for vat in all_vats:
        
        get_detail(vat)


def get_all_vats():
    all_vats = [1, 2]
    return all_vats

def get_detail(vat):
    "so something"
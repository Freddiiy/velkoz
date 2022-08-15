from core import champion, common


def get_champion(name: str):
    return champion.get_champion(name)


if __name__ == "__main__":
    ahri = get_champion("Ahri")
    print(ahri.name)

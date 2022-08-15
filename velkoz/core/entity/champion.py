import json


class Skin:
    id: int
    num: int
    name: str
    chroma: bool

    def __init__(self, id: int, num: int, name: str, chroma: bool):
        self.id = id
        self.num = num
        self.name = name
        self.chroma = chroma


class Champion(object):
    id: str = None
    key: int = None
    name: str = None
    title: str = None
    image: dict = {}
    skins: list[Skin]
    lore: str = None

    def __init__(self, j):
        self.__dict__ = json.loads(j)

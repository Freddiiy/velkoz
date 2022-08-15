import requests

from core.entity.champion import Champion


class DDragon:
    url: str = "https://ddragon.leagueoflegends.com/cdn"
    newest_version: str = requests.get("https://ddragon.leagueoflegends.com/api/versions.json").json()[0]

    def __init__(self):
        self.newest_version = requests.get("https://ddragon.leagueoflegends.com/api/versions.json").json()[0]

    def get_champion(self, name: str) -> Champion:
        name = name.capitalize()
        champ_json = requests.get(f"{self.url}/{self.newest_version}/data/en_US/champion/{name}.json").json()
        return Champion(champ_json)


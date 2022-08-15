from core.entity.champion import Champion
from wrappers.ddragon import DDragon


def get_champion(name: str) -> Champion:
    champ = DDragon().get_champion(name)
    return champ

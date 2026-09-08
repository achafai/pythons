from alchemy.potions import strength_potion
from elements import create_fire

from ..elements import create_air


def lead_to_gold() -> str:
    created_air = create_air()
    created_potion = strength_potion()
    created_fire = create_fire()
    return (
        f"Recipe transmuting Lead to Gold: brew '{created_air}'"
        f" and '{created_potion}' "
        f"mixed with '{created_fire}'"
        )

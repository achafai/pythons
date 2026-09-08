# Unresolved top-level circular dependency:
# dark_validator imports dark_spellbook
from alchemy.grimoire.dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    result = validate_ingredients(ingredients)
    if "VALID" in result:
        return f"Spell '{spell_name}' recorded: {result}"
    return f"Spell '{spell_name}' rejected: {result}"

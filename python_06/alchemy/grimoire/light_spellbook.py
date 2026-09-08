def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    # Function-level (lazy) import to avoid top-level circular dependency
    from alchemy.grimoire.light_validator import validate_ingredients

    result = validate_ingredients(ingredients)
    if "VALID" in result:
        return f"Spell '{spell_name}' recorded: {result}"
    return f"Spell '{spell_name}' rejected: {result}"

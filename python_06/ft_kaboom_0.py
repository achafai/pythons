from alchemy import grimoire


def main() -> None:
    result = grimoire.light_spellbook.light_spell_record(
        "Lumos", "fire and air"
    )
    print(result)


if __name__ == "__main__":
    main()

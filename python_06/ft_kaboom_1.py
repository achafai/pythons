def main() -> None:
    try:
        from alchemy.grimoire.dark_spellbook import dark_spell_record

        print(dark_spell_record("Curse", "bats and frogs"))
    except ImportError as e:
        print(f"KABOOM! The laboratory exploded due to circular import: {e}")


if __name__ == "__main__":
    main()

"""Tournament script for testing battle strategies with various creatures."""

import sys
from ex0 import AquaFactory, CreatureFactory, FlameFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    AggressiveStrategy,
    BattleStrategy,
    DefensiveStrategy,
    InvalidStrategyError,
    NormalStrategy,
)


def run_tournament(
    opponents: list[tuple[CreatureFactory, BattleStrategy]]
) -> None:
    """Run a round-robin tournament between all pairs of opponents.

    Each opponent tuple contains a CreatureFactory and a BattleStrategy.
    """
    total_opponents = len(opponents)
    print(f"=== Starting Tournament ({total_opponents} Competitors) ===")

    for i in range(total_opponents):
        factory_a, strategy_a = opponents[i]
        creature_a = factory_a.create_base()

        for j in range(i + 1, total_opponents):
            factory_b, strategy_b = opponents[j]
            creature_b = factory_b.create_base()

            print(
                f"\n--- Match: {creature_a.name} ({type(strategy_a).__name__}) "
                f"vs {creature_b.name} ({type(strategy_b).__name__}) ---"
            )

            # Process Opponent A action
            try:
                action_a = strategy_a.act(creature_a)
                print(f"[{creature_a.name} Strategy Execution]:\n{action_a}")
            except InvalidStrategyError as err:
                print(
                    f"Invalid strategy for {creature_a.name}: {err}",
                    file=sys.stderr,
                )

            # Process Opponent B action
            try:
                action_b = strategy_b.act(creature_b)
                print(f"[{creature_b.name} Strategy Execution]:\n{action_b}")
            except InvalidStrategyError as err:
                print(
                    f"Invalid strategy for {creature_b.name}: {err}",
                    file=sys.stderr,
                )


def main() -> None:
    """Instantiate factories, strategies, and run tournament scenario."""
    try:
        # Create factories
        flame_factory = FlameFactory()
        aqua_factory = AquaFactory()
        healing_factory = HealingCreatureFactory()
        transform_factory = TransformCreatureFactory()

        # Create strategies
        normal_strat = NormalStrategy()
        aggressive_strat = AggressiveStrategy()
        defensive_strat = DefensiveStrategy()

        # Define opponents (including valid and invalid combinations)
        opponents: list[tuple[CreatureFactory, BattleStrategy]] = [
            (flame_factory, normal_strat),          # Valid
            (transform_factory, aggressive_strat),  # Valid
            (healing_factory, defensive_strat),     # Valid
            (aqua_factory, aggressive_strat),       # Invalid combination
            (flame_factory, defensive_strat),        # Invalid combination
        ]

        run_tournament(opponents)

    except Exception as err:
        print(f"Tournament error: {err}", file=sys.stderr)


if __name__ == "__main__":
    main()

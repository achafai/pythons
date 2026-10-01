from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    """Abstract base class defining the common data processing interface."""

    def __init__(self) -> None:
        """Initialize storage for processed data items and rank counter."""
        self._data: list[tuple[int, str]] = []
        self._rank_counter: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Check whether the input data is appropriate for this processor."""
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        """Process and store input data."""
        pass

    def output(self) -> tuple[int, str]:
        """Extract and remove the oldest piece of data stored internally."""
        if not self._data:
            raise IndexError("No data available to output.")
        return self._data.pop(0)


class NumericProcessor(DataProcessor):
    """Data processor specialized for numeric inputs."""

    def validate(self, data: Any) -> bool:
        """Validate if input is int, float, or a list of numbers."""
        if isinstance(data, (int, float)) and not isinstance(data, bool):
            return True
        if isinstance(data, list):
            return all(
                isinstance(x, (int, float)) and not isinstance(x, bool)
                for x in data
            )
        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        """Ingest numeric data or list of numeric data into storage."""
        if not self.validate(data):
            raise TypeError("Improper numeric data")

        if isinstance(data, list):
            for item in data:
                self._data.append((self._rank_counter, str(item)))
                self._rank_counter += 1
        else:
            self._data.append((self._rank_counter, str(data)))
            self._rank_counter += 1


class TextProcessor(DataProcessor):
    """Data processor specialized for text inputs."""

    def validate(self, data: Any) -> bool:
        """Validate if input is str or a list of strings."""
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        """Ingest string or list of strings into storage."""
        if not self.validate(data):
            raise TypeError("Improper text data")

        if isinstance(data, list):
            for item in data:
                self._data.append((self._rank_counter, item))
                self._rank_counter += 1
        else:
            self._data.append((self._rank_counter, data))
            self._rank_counter += 1


class LogProcessor(DataProcessor):
    """Data processor specialized for key-value log entries."""

    def validate(self, data: Any) -> bool:
        """Validate if input is a dict of strings or list of string dicts."""
        if isinstance(data, dict):
            return all(
                isinstance(k, str) and isinstance(v, str)
                for k, v in data.items()
            )
        if isinstance(data, list):
            return all(
                isinstance(item, dict) and all(
                    isinstance(k, str) and isinstance(v, str)
                    for k, v in item.items()
                )
                for item in data
            )
        return False

    def _format_log(self, log_dict: dict[str, str]) -> str:
        """Format log dictionary into readable string representation."""
        if "log_level" in log_dict and "log_message" in log_dict:
            return f"{log_dict['log_level']}: {log_dict['log_message']}"
        return ": ".join(log_dict.values())

    def ingest(
        self, data: dict[str, str] | list[dict[str, str]]
    ) -> None:
        """Ingest log dictionary or list of log dictionaries."""
        if not self.validate(data):
            raise TypeError("Improper log data")

        if isinstance(data, list):
            for item in data:
                formatted = self._format_log(item)
                self._data.append((self._rank_counter, formatted))
                self._rank_counter += 1
        else:
            formatted = self._format_log(data)
            self._data.append((self._rank_counter, formatted))
            self._rank_counter += 1


def main() -> None:
    """Test the data processor architecture."""
    print("=== Code Nexus - Data Processor ===")

    print("Testing Numeric Processor...")
    num_proc = NumericProcessor()
    print(f"Trying to validate input '42': {num_proc.validate(42)}")
    print(f"Trying to validate input 'Hello': {num_proc.validate('Hello')}")

    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num_proc.ingest("foo")  # type: ignore
    except ValueError as exc:
        print(f"Got exception: {exc}")

    num_data: list[int | float] = [1, 2, 3, 4, 5]
    print(f"Processing data: {num_data}")
    num_proc.ingest(num_data)

    print("Extracting 3 values...")
    for _ in range(3):
        rank, val = num_proc.output()
        print(f"Numeric value {rank}: {val}")

    print("Testing Text Processor...")
    text_proc = TextProcessor()
    print(f"Trying to validate input '42': {text_proc.validate(42)}")

    text_data = ["Hello", "Nexus", "World"]
    print(f"Processing data: {text_data}")
    text_proc.ingest(text_data)

    print("Extracting 1 value...")
    rank, val = text_proc.output()
    print(f"Text value {rank}: {val}")

    print("Testing Log Processor...")
    log_proc = LogProcessor()
    print(f"Trying to validate input 'Hello': {log_proc.validate('Hello')}")

    log_data = [
        {
            "log_level1": "NOTICE",
            "log_message": "Connection to server",
        },
        {
            "log_level": "ERROR",
            "log_message": "Unauthorized access!!",
        },
    ]
    print(f"Processing data: {log_data}")
    log_proc.ingest(log_data)

    print("Extracting 2 values...")
    for _ in range(2):
        rank, val = log_proc.output()
        print(f"Log entry {rank}: {val}")


if __name__ == "__main__":
    main()

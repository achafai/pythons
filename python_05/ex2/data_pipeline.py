from abc import ABC, abstractmethod
from typing import Any, Protocol, Union


class DataProcessor(ABC):
    """Abstract base class defining the common data processing interface."""

    def __init__(self) -> None:
        """Initialize storage for processed data items and rank counter."""
        self._data: list[tuple[int, str]] = []
        self._rank_counter: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Check whether input data is appropriate for this processor."""
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

    @property
    def total_processed(self) -> int:
        """Return the total number of items processed."""
        return self._rank_counter

    @property
    def remaining(self) -> int:
        """Return the number of items remaining in storage."""
        return len(self._data)


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

    def ingest(self, data: Union[int, float, list[Union[int, float]]]) -> None:
        """Ingest numeric data or list of numeric data into storage."""
        if not self.validate(data):
            raise ValueError("Improper numeric data")

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

    def ingest(self, data: Union[str, list[str]]) -> None:
        """Ingest string or list of strings into storage."""
        if not self.validate(data):
            raise ValueError("Improper text data")

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
        """Validate if input is dict of strings or list of string dicts."""
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
        self, data: Union[dict[str, str], list[dict[str, str]]]
    ) -> None:
        """Ingest log dictionary or list of log dictionaries."""
        if not self.validate(data):
            raise ValueError("Improper log data")

        if isinstance(data, list):
            for item in data:
                formatted = self._format_log(item)
                self._data.append((self._rank_counter, formatted))
                self._rank_counter += 1
        else:
            formatted = self._format_log(data)
            self._data.append((self._rank_counter, formatted))
            self._rank_counter += 1


class ExportPlugin(Protocol):
    """Protocol defining structural interface for export plugins."""

    def process_output(self, data: list[tuple[int, str]]) -> None:
        """Process and export formatted data tuples."""
        ...


class CSVExportPlugin:
    """Export plugin formatting data as CSV strings."""

    def process_output(self, data: list[tuple[int, str]]) -> None:
        """Format extracted tuples into a CSV line and print."""
        print("CSV Output:")
        values = [val for _, val in data]
        print(",".join(values))


class JSONExportPlugin:
    """Export plugin formatting data as JSON strings."""

    def process_output(self, data: list[tuple[int, str]]) -> None:
        """Format extracted tuples into a JSON object string and print."""
        print("JSON Output:")
        items = [f'"item_{rank}": "{val}"' for rank, val in data]
        print("{" + ", ".join(items) + "}")


class DataStream:
    """Manages data processors, routes input,
      and outputs via export plugins."""

    def __init__(self) -> None:
        """Initialize empty processor list."""
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        """Register a new data processor."""
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        """Route each element in stream to appropriate processor."""
        for element in stream:
            processed = False
            for proc in self._processors:
                if proc.validate(element):
                    try:
                        proc.ingest(element)
                        processed = True
                        break
                    except Exception as exc:
                        print(f"DataStream error - Ingest failed: {exc}")
                        processed = True
                        break
            if not processed:
                print(
                    "DataStream error - Can't process element in stream: "
                    f"{element}"
                )

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        """Consume nb elements from each processor and export via plugin."""
        for proc in self._processors:
            extracted: list[tuple[int, str]] = []
            for _ in range(nb):
                if proc.remaining > 0:
                    try:
                        extracted.append(proc.output())
                    except IndexError:
                        break
                else:
                    break
            plugin.process_output(extracted)

    def print_processors_stats(self) -> None:
        """Print statistics for all registered processors."""
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return

        for proc in self._processors:
            class_name = proc.__class__.__name__
            if class_name.endswith("Processor"):
                name = class_name[:-9] + " Processor"
            else:
                name = class_name
            print(
                f"{name}: total {proc.total_processed} items processed, "
                f"remaining {proc.remaining} on processor"
            )


def main() -> None:
    """Run data pipeline test scenario."""
    print("=== Code Nexus - Data Pipeline ===")
    print("Initialize Data Stream...")
    ds = DataStream()
    ds.print_processors_stats()

    print("Registering Processors")
    num_proc = NumericProcessor()
    text_proc = TextProcessor()
    log_proc = LogProcessor()
    ds.register_processor(num_proc)
    ds.register_processor(text_proc)
    ds.register_processor(log_proc)

    batch1 = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {"log_level": "INFO", "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]

    print(f"Send first batch of data on stream: {batch1}")
    ds.process_stream(batch1)
    ds.print_processors_stats()

    csv_plugin = CSVExportPlugin()
    print("Send 3 processed data from each processor to a CSV plugin:")
    ds.output_pipeline(3, csv_plugin)   # type:ignore
    ds.print_processors_stats()

    batch2 = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": "ERROR", "log_message": "500 server crash"},
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days",
            },
        ],
        [32, 42, 64, 84, 128, 168],
        "World hello",
    ]

    print(f"Send another batch of data: {batch2}")
    ds.process_stream(batch2)
    ds.print_processors_stats()

    json_plugin = JSONExportPlugin()
    print("Send 5 processed data from each processor to a JSON plugin:")
    ds.output_pipeline(5, json_plugin)    # type:ignore
    ds.print_processors_stats()


if __name__ == "__main__":
    main()

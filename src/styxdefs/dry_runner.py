"""Dummy runner for debugging purposes."""

import pathlib

from .types import Execution, InputPathType, Metadata, OutputPathType, Runner


class DryRunner(Runner, Execution):
    """Dry runner for debugging purposes."""

    def __init__(self) -> None:
        """Create new dry runner."""
        self.last_cargs: list[str] | None = None
        self.last_metadata: Metadata | None = None

    def start_execution(self, metadata: Metadata) -> Execution:
        """Start execution."""
        self.last_metadata = metadata
        return self

    def input_file(
        self,
        host_file: InputPathType,
        resolve_parent: bool = False,
        mutable: bool = False,
    ) -> str:
        """Resolve input file."""
        return str(host_file)

    def output_file(self, local_file: str, optional: bool = False) -> OutputPathType:
        """Resolve output file."""
        return pathlib.Path(local_file)

    def run(self, cargs: list[str]) -> None:
        """Execute command (in this dry runner this only captures the outputs)."""
        self.last_cargs = cargs


def DummyRunner():  # noqa
    from warnings import warn

    warn(
        "The DummyRunner alias will be removed in a future version of styxdefs! "
        "Please use the new name DryRunner."
    )
    return DryRunner()
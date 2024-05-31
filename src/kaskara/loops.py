__all__ = ("ProgramLoops",)

from collections.abc import Iterable

import attr

from .core import FileLocation, FileLocationRange, FileLocationRangeSet


@attr.s(frozen=True, slots=True, auto_attribs=True)
class ProgramLoops:
    """Maintains information about all loops within a program."""
    _covered_by_loop_bodies: FileLocationRangeSet

    @classmethod
    def from_body_location_ranges(cls,
                                  bodies: Iterable[FileLocationRange],
                                  ) -> "ProgramLoops":
        return ProgramLoops(FileLocationRangeSet(bodies))

    def is_within_loop(self, location: FileLocation) -> bool:
        """Checks whether a given location is enclosed within a loop."""
        is_within: bool = self._covered_by_loop_bodies.contains(location)
        return is_within

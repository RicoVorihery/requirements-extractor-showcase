"""
Simplified schemas extracted from a larger private project.
Included here to illustrate data contracts and extraction outputs.
"""
from enum import Enum
from typing import Optional, List
from pydantic import BaseModel


class TextPatternMode(str, Enum):
    WITH_PREFIX = "with_prefix"
    NO_PREFIX_AFTER_ID = "no_prefix_after_id"


class CoverageMode(str, Enum):
    WITH_PREFIX = "with_prefix"
    NO_PREFIX_LISTED = "no_prefix_listed"


class CoveragePosition(str, Enum):
    AFTER_ID = "after_id"
    AFTER_TEXT = "after_text"
    NO_COVERAGE = "no_coverage"


class BlockResult(BaseModel):
    id_line: str
    has_coverage: bool
    id_index: int
    text_index: int
    coverage_index: Optional[int]


class BlockBuildStats(BaseModel):
    blocks_found: int
    blocks_with_coverage: int
    candidate_id_lines: List[str]
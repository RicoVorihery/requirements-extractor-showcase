"""
Simplified block detection logic from a private system.
This version focuses on deterministic neighborhood-based extraction.
"""


from __future__ import annotations

from typing import List, Optional

from app.core.schemas import TextPatternMode, CoverageMode, CoveragePosition, BlockBuildStats, BlockResult
from app.core.utils import normalize, looks_like_id, looks_like_coverage, looks_like_text, starts_with_prefix


class BlockBuilder:
    def __init__(
        self,
        paragraphs: List[str],
        *,
        text_mode: TextPatternMode,
        text_prefix: Optional[str],
        coverage_mode: CoverageMode,
        coverage_prefix: Optional[str],
        coverage_position: CoveragePosition,
    ):
        self.paragraphs = [normalize(p) for p in paragraphs]

        self.text_mode = text_mode
        self.text_prefix = text_prefix

        self.coverage_mode = coverage_mode
        self.coverage_prefix = coverage_prefix
        self.coverage_position = coverage_position

    def build(self) -> BlockBuildStats:
        results: List[BlockResult] = []
        i = 0
        n = len(self.paragraphs)

        while i < n:
            id_line = self.paragraphs[i]

            if not looks_like_id(id_line):
                i += 1
                continue

            block = self._try_build_block(i)
            if block:
                results.append(block)
                # saut direct après le bloc (consecutif)
                i = (
                    max(
                        filter(
                            lambda x: x is not None,
                            [block.text_index, block.coverage_index],
                        )
                    )
                    + 1
                )
            else:
                i += 1

        # agrégation
        unique_ids: List[str] = []
        seen = set()

        for r in results:
            if r.id_line not in seen:
                unique_ids.append(r.id_line)
                seen.add(r.id_line)

        return BlockBuildStats(
            blocks_found=len(results),
            blocks_with_coverage=sum(1 for r in results if r.has_coverage),
            candidate_id_lines=unique_ids,
        )

    # -------------------------
    # Bloc logique
    # -------------------------

    def _try_build_block(self, i: int) -> Optional[BlockResult]:
        """
        Tente de construire un bloc strictement consécutif
        selon la config UI.
        """
        p = self.paragraphs
        n = len(p)

        id_line = p[i]

        # 1) NO_COVERAGE : ID -> Texte (uniquement)
        if self.coverage_position == CoveragePosition.NO_COVERAGE:
            text_idx = i + 1
            if text_idx >= n:
                return None
            if not self._match_text(p[text_idx]):
                return None

            return BlockResult(
                id_line=id_line,
                has_coverage=False,
                id_index=i,
                text_index=text_idx,
                coverage_index=None,
            )

        # 2) AFTER_ID : ID -> Coverage -> Texte
        if self.coverage_position == CoveragePosition.AFTER_ID:
            cov_idx = i + 1
            text_idx = i + 2
            if cov_idx >= n or text_idx >= n:
                return None
            if not self._match_coverage(p[cov_idx]):
                return None
            if not self._match_text(p[text_idx]):
                return None

            return BlockResult(
                id_line=id_line,
                has_coverage=True,
                id_index=i,
                coverage_index=cov_idx,
                text_index=text_idx,
            )

        # 3) AFTER_TEXT : ID -> Texte -> Coverage?
        text_idx = i + 1
        if text_idx >= n:
            return None
        if not self._match_text(p[text_idx]):
            return None

        cov_idx = text_idx + 1
        has_cov = False
        cov_real_idx = None

        if cov_idx < n and self._match_coverage(p[cov_idx]):
            has_cov = True
            cov_real_idx = cov_idx

        return BlockResult(
            id_line=id_line,
            has_coverage=has_cov,
            id_index=i,
            text_index=text_idx,
            coverage_index=cov_real_idx,
        )

    # -------------------------
    # Matchers
    # -------------------------

    def _match_text(self, line: str) -> bool:
        if self.text_mode == TextPatternMode.WITH_PREFIX:
            prefix = self.text_prefix or ""
            return starts_with_prefix(line, prefix)
        else:
            return looks_like_text(line)

    def _match_coverage(self, line: str) -> bool:
        if self.coverage_mode == CoverageMode.WITH_PREFIX:
            prefix = self.coverage_prefix or ""
            return starts_with_prefix(line, prefix)
        else:
            return looks_like_coverage(line)
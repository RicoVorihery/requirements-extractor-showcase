"""
Minimal FastAPI entrypoint for the showcase.

This file exists only to demonstrate how the core extraction logic
could be exercised in isolation. It is not a production API.
"""

from fastapi import FastAPI

from app.core.block_builder import BlockBuilder
from app.demo.sample_paragraphs import SAMPLE_PARAGRAPHS

app = FastAPI(title="Requirements Extractor Showcase")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/demo/extract")
def demo_extract():
    """
    Demonstration endpoint using static sample paragraphs.
    """
    builder = BlockBuilder(paragraphs=SAMPLE_PARAGRAPHS)
    result = builder.run()

    return {
        "blocks_found": result.blocks_found,
        "blocks_with_coverage": result.blocks_with_coverage,
        "candidate_id_lines": result.candidate_id_lines,
    }

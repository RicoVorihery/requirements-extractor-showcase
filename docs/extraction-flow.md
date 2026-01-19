# Extraction Flow

This document describes the end-to-end extraction flow at a conceptual level.
It focuses on _what happens_ and _why_, rather than implementation details.

---

## 1. Document Intake

The user provides one or more specification documents.
Each document represents a requirement level (e.g. user, system, subsystem).

At this stage, no assumptions are made about traceability or correctness.
The goal is simply to make the document content accessible for processing.

---

## 2. Paragraph Normalization

Documents are converted into a linear sequence of normalized paragraphs.

Normalization includes:

- whitespace and formatting cleanup
- consistent prefix handling
- removal of layout-specific noise

This step ensures that downstream logic operates on predictable inputs.

---

## 3. Configuration by Intent

Instead of asking users to define low-level detection rules, the system captures intent:

- where requirement identifiers appear
- how requirement text is positioned
- whether coverage information is present

This configuration is lightweight and reflects how engineers reason about their documents.

---

## 4. Block Detection

The system iterates through paragraphs and applies neighborhood-based rules.

A valid requirement block is detected when:

- an identifier is found
- the associated text is located in the expected position
- optional coverage information is present or absent as configured

Detection is deterministic and produces explicit results.

---

## 5. Requirement Extraction

Once blocks are detected, the system extracts structured requirements:

- requirement identifier
- requirement text
- optional coverage information

Extraction follows explicit rules derived from the detection phase and produces consistent, reviewable outputs.

---

## 6. Structured Output

Extracted requirements are grouped into a structured dataset that includes:

- normalized requirement entries
- summary metrics (counts, coverage presence)
- intermediate data useful for traceability review

The goal is not to hide uncertainty, but to make it visible.

---

## 7. Review and Validation

Extracted requirements are presented in a review-friendly format.
Users can:

- inspect individual requirements
- assess coverage and completeness
- identify missing or inconsistent items

This step is critical in safety and compliance-oriented workflows.

---

## 8. Iteration

If issues are found, users adjust configuration and re-run extraction.
Because the process is deterministic, changes have predictable effects.

This enables fast iteration without guesswork.

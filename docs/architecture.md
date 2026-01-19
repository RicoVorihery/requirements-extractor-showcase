# Architecture Overview

This repository is intentionally scoped as an engineering showcase.
It focuses on a practical systems-engineering workflow: extracting and structuring requirements across multiple specification documents and levels (N / N-1), then supporting coverage and traceability review.

The goal is not to present a full SaaS, but to highlight architectural decisions, algorithmic boundaries, and product-driven trade-offs.

---

## Problem Context

Systems engineers work with multiple specification documents written by different authors, across different requirement levels:

- User Requirement
  "As an operator, I want the drone to deliver packages autonomously within 30 minutes."

- System Requirement
  "The drone delivery system shall navigate to a specified GPS coordinate and deliver a payload up to 5 kg."

- Subsystem Requirement
  "The propulsion subsystem shall provide sufficient thrust for a 30-minute flight with a 5 kg payload."

- Component Requirement
  "The GPS receiver component shall output position data with 2-meter accuracy at 10 Hz."

Even when document structures are stable, validating coverage and traceability across those documents is time-consuming and error-prone.

With tools like Reqtify, engineers often need to manually configure identifier detection rules for each document. This configuration effort is hard to maintain over time and adds friction every time files are updated.

---

## High-Level Architecture

The extraction pipeline is organized into clear layers:

[ Document Input ]

|

v

[ Paragraph Normalization ]

|

v

[ Neighborhood-Based Block Detection ]

|

v

[ Structured Requirement Blocks ]

|

v

[ Coverage / Traceability Views ]

Each layer has a narrow responsibility and produces outputs that are easy to validate.

---

## Core Components

### Block Builder (backend/app/core/block_builder.py)

The Block Builder is the core algorithmic component.

Responsibilities:

- iterate through normalized document paragraphs
- apply user-defined neighborhood rules (e.g., where ID/text/coverage appear)
- detect valid requirement blocks deterministically
- output structured blocks and candidate identifier lines for later validation

This design favors predictability and debuggability.

---

### Intermediate Representation (Structured Blocks)

Instead of jumping directly to “final truth”, the system produces:

- structured blocks (ID / text / optional coverage)
- summary counts (blocks found, coverage presence)
- a candidate dataset that can later be validated/scored

This helps engineers understand what was extracted and reduces the risk of silent extraction errors.

---

## Design Decisions

### Deterministic first

The system starts with deterministic logic because it:

- is easier to test and debug
- makes failure modes explicit
- supports user trust before introducing automation layers

---

### Separate concerns: parsing vs inference vs validation

The architecture keeps boundaries between:

- document parsing / normalization
- block detection (neighborhood rules)
- validation and later enrichment (e.g., scoring, traceability)

This allows each concern to evolve independently.

---

### UI focuses on intent, not low-level syntax

The UI is designed to capture user intent (where information is located) rather than forcing users to write and maintain low-level patterns.

---

## What Is Intentionally Missing

This repository does not include:

- persistence or database models
- authentication or multi-tenancy
- production orchestration details
- full traceability graph features

Those aspects are outside the scope of this engineering narrative.

---

## What This Demonstrates

- Clear system boundaries
- Product-driven backend design
- Deterministic extraction logic with explicit trade-offs
- A workflow designed for coverage/traceability review

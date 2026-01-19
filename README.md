# Requirements Extractor — Engineering Showcase

This repository is a public engineering showcase.
It explores how to extract, structure, and review system requirements across multiple specification documents and levels.

The focus is on architecture, deterministic logic, and product-driven trade-offs — not on building a full SaaS.

---

## Why This Exists

Systems engineers routinely work with multiple specification documents:

- User Requirement
  ( e.g: "As an operator, I want the drone to deliver packages autonomously within 30 minutes.")

- System Requirement
  (e.g: "The drone delivery system shall navigate to a specified GPS coordinate and deliver a payload up to 5 kg.")

- Subsystem Requirement
  (e.g: "The propulsion subsystem shall provide sufficient thrust for a 30-minute flight with a 5 kg payload.")

- Component Requirement
  (e.g:"The GPS receiver component shall output position data with 2-meter accuracy at 10 Hz.")

Even when documents are well-structured, validating coverage and traceability across those levels is time-consuming.
Existing tools often require extensive manual configuration before meaningful results can be reviewed.

This project explores a different approach: reduce configuration friction, keep extraction explainable, and optimize for review rather than blind automation.

---

## Problem in One Sentence

"I have specification documents with requirements.
I want to extract them and review their coverage and traceability without spending days configuring the tool."

---

## Mental Model

Requirement extraction is treated as a **review workflow**, not a one-click operation.

Instead of hiding uncertainty, the system:

- detects requirement blocks deterministically
- extracts structured requirements explicitly
- exposes intermediate results for validation
- supports fast iteration when issues are found

---

## Simplified Architecture

The extraction pipeline is organized into clear layers: [ Document Input ]

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

Each step has a clear responsibility and produces outputs that can be inspected.

---

## What This Repository Contains

- A backend core focused on block detection and extraction logic
- A simplified frontend illustrating configuration and review flows
- Architecture and flow documentation explaining design decisions

---

## What Is Intentionally Out of Scope

This repository does not include:

- production persistence or database models
- authentication or authorization
- full traceability graph generation
- advanced automation layers

Those aspects are intentionally omitted to keep the focus on core reasoning.

---

## What This Demonstrates

- Clear system boundaries
- Deterministic extraction logic
- Product-oriented backend design
- UX decisions grounded in real engineering workflows

---

## Who This Is For

This showcase is intended for engineers interested in:

- system design trade-offs
- explainable data extraction
- tooling for safety- or compliance-oriented domains

It is not intended as a production-ready product.

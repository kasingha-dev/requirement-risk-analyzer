# Requirement Risk Analyzer

## Overview

Requirement Risk Analyzer helps teams identify requirement gaps, implementation risks, architecture concerns, and client clarification questions before software development begins.

Users can upload requirement documents such as meeting transcripts, requirement specifications, and notes. The application analyzes the content using a combination of Large Language Models and deterministic rule-based analysis.

The generated report includes:

* Extracted requirements
* Missing requirements
* Implementation risks
* Client clarification questions
* Architecture concerns
* PDF export

---

## Features

### Requirement Extraction

Uses OpenAI GPT models to extract structured requirements from uploaded documents.

Output includes:

* Features
* Actors
* Integrations
* Constraints

### Gap Analysis

Rule-based engine that identifies commonly missed requirements.

Examples:

* Refund process
* Renewal flow
* Audit logs
* Role permissions

### Risk Analysis

Identifies implementation risks based on extracted requirements.

Examples:

* Payment failure handling
* Authorization concerns
* Storage requirements

### Question Generation

Generates prioritized client clarification questions.

Categories:

* Critical Questions
* Important Questions

### Architecture Analysis

Identifies architecture and scalability concerns.

Examples:

* Authentication considerations
* Security concerns
* Infrastructure planning
* Integration complexity

### PDF Export

Generates downloadable analysis reports.

---

## Architecture

See:

architecture-diagram.png

Application flow:

User Upload → Processing → Analysis Engines → Report Generation → UI / PDF

---

## Technology Stack

Backend:

* Python 3.11
* FastAPI

AI:

* OpenAI GPT

Frontend:

* HTML
* CSS
* Jinja Templates

PDF:

* ReportLab

---

## Running Locally

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Configure Environment

Create:

```text
.env
```

Add:

```text
OPENAI_API_KEY=your_key_here
```

### Run

```bash
uvicorn app:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

---

## Example Workflow

1. Upload requirement documents
2. Analyze requirements
3. Review risks and gaps
4. Review generated questions
5. Download PDF report

---

## Design Decisions

### Hybrid Analysis Approach

Requirement extraction and question generation use LLMs.

Gap analysis and risk analysis use deterministic rule-based logic to ensure repeatable and explainable results.

### PDF Export

The latest generated report is temporarily stored in memory for simplicity.

A production implementation would persist reports and generate downloads using report identifiers.

---

## Future Improvements

* Report persistence
* User authentication
* Historical report tracking
* Improved PDF styling
* Additional domain-specific analyzers
* Multi-user support

---

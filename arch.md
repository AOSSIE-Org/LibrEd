# Detailed System Architecture

## 0. Description

Dont Compete is a purely local, containerized, and agent-driven platform for exam preparation. It combines a modern React frontend with an autonomous backend pipeline that scrapes, classifies, and generates study materials, notes and interactive quizzes from raw syllabus PDFs and local LLMs.

Live: https://dontcompete.vercel.app

### 0.1 Possible Improvements

* OCR doesn't work well on different colors and some scenarios.
* LLaMA 3.1 isn't accurate enough.
* Duplicate handling in topic classification is a bit too strict.
* Consider shifting knowledge generation fully to TypeScript?
* Edit markdown from frontend?
* Improve performance on CPU.
* Platform is currently exam-specific; could be generalized.
* Shift to asynchronous operations where viable.
* Shift to better sources for PYQs and answer-keys, generate explaination with LLM.
* Re-evalute the decision of shifting away from LFS, it'll likely be needed.

---

## 1. Data Pipeline: Detailed Components & Flows

The generator (`generator/src/main.py`) runs a sequential, atomic pipeline.

### Stage 1: Acquisition (Scraping)
**Component**: `ScraperEngine` (`scraper_engine.py`) using **Playwright**.
*   **Constraint**: **LLMs are explicitly NOT used** for detection/downloading. Logic must be procedural/heuristic.
*   **Logic**:
    1.  **Syllabus**: Visit `/syllabus/{stream}` -> Find year page -> Extract PDF link.
    2.  **PYQs**: Visit `/py-papers` -> Filter by stream slug -> Iterate years -> Extract PDF links.
*   **Optimization**: Skips re-downloading if file exists in `data/raw/`.

### Stage 2: Processing (Ingestion)
**Component**: `pdf_utils.py` using **PyMuPDF (fitz)** and **Pillow**.
*   **State Machine**:
    *   `START` -> `Question \d+` -> `QUESTION`
    *   `QUESTION` -> `Ans.` -> `ANSWER`
    *   `ANSWER` -> `Sol.` -> `EXPLANATION`
*   **Image Stitching**:
    *   **Full Width**: Captures full content width.
    *   **Vertical Merge**: Merges multi-page segments into single `q.png`/`exp.png`.
*   **Validation**: Image extraction occurs **only** when valid boundaries are detected.

### Stage 3: AI Analysis (Syllabus Parsing)
**Component**: `knowledge_utils.py` + `SyllabusParser`
*   **Input**: Syllabus PDFs from Stage 1.
*   **Prompt**: Extracts structured hierarchy (Subjects -> Subtopics) from raw PDF text.
*   **Output**: Populates `subjects` and `subtopics` tables (idempotent).
*   **Constraint**: Must run *before* Question Classification.

### Stage 4: AI Analysis (Classification)
**Component**: `knowledge_utils.py` + `prompt_utils.py` + **Ollama**.

#### Prompt Generation
*   **Stateless**: Prompts must be self-contained within context window.
*   **Input**: Syllabus Database + Batch of Questions (default 5).
*   **Task**: Map Question ID -> Subject -> Subtopic.
*   **Handling Unknowns**: Maps "Other" to "General Aptitude" -> "Miscellaneous".

#### LLM Processing
*   **Orchestration**: Sequential/Batched execution to handle local resource limits.
*   **Output**: JSON-only response parsed and synced to `questions` table.

### Stage 5: AI Analysis (Theory Generation)
For each Subtopic with > 0 questions:
*   **Prompt**: Includes existing theory and all questions as context to determine depth/scope.
*   **Output**: Markdown with Mermaid diagrams (`graph LR`, etc.) and KaTeX math.
*   **Update Rule**: Updates existing files only if theres something new to add.

### Stage 6: Manifest Generation (Export)
**Component**: `knowledge_utils.generate_manifest` (Per-Stream)
*   **No Global Registry**: Does *not* generate a global `exams.json` or `info.json`. Discovery is purely filesystem-based.
*   **Output**: Generates `structure.json` inside each stream's folder.
*   **Copy/Linking**: Ensures all referenced images exist in `frontend/assets`.

### Stage 7: Auditing
Users can improve the generated notes, and LLMs would use it as a reference.

---

## 2. Database Schema (DuckDB)
The system uses **DuckDB** (`data/app.duckdb`) as an intermediate relational store.

| Table | Column | Type | Description |
| :--- | :--- | :--- | :--- |
| **questions** | `id` | VARCHAR | Global composite ID (`{stream}_{packet}_{qno}`) |
| | `stream_code` | VARCHAR | e.g., `computer-science-information-technology` |
| | `packet_id` | VARCHAR | Source PDF identifier (e.g., `2024-M`) |
| | `question_no` | VARCHAR | e.g., `1`, `55` |
| | `q_type` | VARCHAR | `MCQ`, `MSQ`, `NAT` |
| | `q_key` | VARCHAR | Answer Key (e.g. `A`, `55.2`) |
| | `q_text` | TEXT | Extracted text of question |
| | `a_text` | TEXT | Extracted text of answer |
| | `exp_text` | TEXT | Extracted text of explanation |
| | `subtopic_id` | VARCHAR | FK to `subtopics.id`. Populated by LLM. |
| | `img_path_q` | VARCHAR | Relative path to question image |
| | `img_path_exp` | VARCHAR | Relative path to explanation image |
| **subjects** | `id` | VARCHAR | e.g., `cs_subj_1` |
| | `name` | VARCHAR | e.g., `Digital Logic` |
| **subtopics** | `id` | VARCHAR | e.g., `cs_subj_1_topic_3` |
| | `subject_id` | VARCHAR | FK to `subjects.id` |
| | `name` | VARCHAR | e.g., `Minimization` |
| **theory** | `id` | VARCHAR | e.g., `theory_cs_subj_1_topic_3` |
| | `subtopic_id` | VARCHAR | FK to `subtopics.id` |
| | `content_md` | TEXT | Generated Markdown content |

---

## 3. Configuration Management
*   **Central Config**: `generator/src/config.py`.
*   **Secrets**: Reads from `.env` (passed to Docker).
*   **Parameters**:
    *   `TARGET_STREAMS`: Defines active streams (e.g., CS, DA).
    *   `OLLAMA_MODEL`: Configurable model selection (Llama 3, Qwen, etc.).
    *   `CLASSIFICATION_BATCH_SIZE`: Control prompt context size.

---

## 4. Frontend Architecture (React)

### Tech Stack
*   **Framework**: TanStack Start / React (Vite).
*   **Styling**: Tailwind CSS + DaisyUI.
*   **Routing**: File-based (`@tanstack/react-router`).
*   **Linting**: Biome (No ESLint/Prettier).
*   **MDX**: `rehype-katex` and `mermaid` support.

### Modular & Dynamic UI
*   **Modular Root Layout**: `__root.tsx` acts as a minimal structural shell, delegating specific behaviors to:
    *   `ThemeScript`: Injects a synchronous, blocking script into `<head>` to prevent Flash of Unstyled Content (FOUC).
    *   `GlobalBreadcrumbs`: Dynamically generates consistent navigation from URI path segments, avoiding hardcoded labels.
*   **Stateful Dashboard**: Uses query parameters (`?expanded=`) for targeted expansion while defaulting to "All Expanded" to maximize content visibility.

### Assessment Logic
*   **Flow**: Stream -> Subject -> Subtopic -> Theory -> Assessment.
*   **Rules**:
    *   **Max 20 questions** per attempt (Randomized).
    *   **Time Limit**: **4 minutes per question**.
*   **Interaction**:
    *   **MCQ/MSQ/NAT**: Adaptive input fields.
    *   **Submission**: Correct -> Next; Incorrect -> Show Explanation.
*   **Rendering**:
    *   Theory: MDX with `rehype-katex` and `mermaid`.
    *   Placeholders: Code-based UI for missing artifacts.

---

## 5. Data Contracts & Artifacts

### 5.1 Location
All frontend-consumable data resides in: `frontend/public/assets/gate/`

### 5.2 File Structure
```text
assets/gate/
└── cs/
    ├── structure.json
    ├── digital-logic/
    │   ├── boolean-algebra.md
    │   └── number-systems.md
    └── questions/
        └── 2024-M/
            └── 1/
                ├── q.png
                ├── exp.png
                └── data.json
```

---

## 6. Testing & CI/CD
*   **Unit Testing**: `pytest` for all backend modules (scraper, parser, utils).
*   **Frontend Testing**: Component testing via Vitest/Jest.
*   **CI Pipeline**: GitHub Actions to:
    *   Lint code (Biome/Ruff).
    *   Run unit tests.
    *   Build Docker images (dry run).

---

## 7. System Design Diagram

```mermaid
sequenceDiagram
    participant S as Scraper
    participant FS as FileSystem
    participant P as Processor (No OOP)
    participant DB as DuckDB
    participant G as Generator (Func)
    participant LLM as Ollama
    participant FE as Frontend

    Note over S, FS: Stage 1: Acquisition
    S->>S: Heuristic DOM Analysis (No LLM)
    S->>FS: Download PDF (Skip if exists)

    Note over P, DB: Stage 2: Processing & Sync
    P->>FS: Read PDF
    P->>P: Stitch (Full Width) & Crop (3%/5%)
    P->>FS: Save q.png, exp.png, data.json
    P->>DB: Sync Metadata

    Note over G, LLM: Stage 3,4,5: Classification
    G->>DB: Fetch Questions
    G->>G: Create Stateless Prompts
    G->>LLM: Classify (JSON)
    LLM-->>G: Response
    G->>DB: Update Taxonomy

    Note over G, LLM: Stage 6,7: Theory
    G->>DB: Fetch Context
    G->>LLM: Generate Theory (MD + Mermaid)
    G->>FS: Save {topic}.md

    Note over G, FS: Stage 8: Manifest
    G->>FS: Generate structure.json

    Note over FE, FS: Runtime
    FE->>FS: Load structure.json
    FE->>FE: Select Subtopic
    FE->>FE: Render Theory
    FE->>FE: Start Test (Random 20, 4min/q)
```

---

## 8. Constraints

### Execution & Environment
*   **No Local Installations**: Entire workflow must run via **Docker / Docker Compose**.
*   **Single-Entry Workflow**: Docker Compose runs both asset generation and frontend.
*   **Local & Private**: Relies entirely on local LLMs (Ollama) and local artifacts; **No remote API support**.

### Data Integrity & Reusability
*   **Incremental & Idempotent**: Re-runs extend existing datasets instead of recreating them.
*   **Reusability-First**: Existing PDFs, databases, and artifacts must be reused.
*   **Single Source of Truth**: All derived data must be traceable to original PDFs.
*   **Robust Prompting**: Prompts must be self-contained (stateless) and designed to fit within model context windows.
*   **No Hardcoded Values**: Architecture should minimize hardcoded values, unless module-specific.

### Performance & Safety
*   **Skip Re-downloading**: Do not download PDFs if they already exist.
*   **Safe DB Ops**: Use `INSERT OR IGNORE`/`REPLACE` to maintain idempotency.
*   **Valid Extraction**: Image extraction occurs **only** when valid boundaries are detected.

### Non-Goals
*   Authentication, Cloud Deployment, Real-time collaboration, Analytics (beyond counts).

---

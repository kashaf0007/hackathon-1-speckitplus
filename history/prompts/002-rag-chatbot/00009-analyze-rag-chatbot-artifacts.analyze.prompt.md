---
id: 00009
title: Analyze RAG Chatbot Artifacts
stage: analyze
date: 2025-12-10
surface: agent
model: gemini
feature: 002-rag-chatbot
branch: docs/update-rag-chatbot-t019
user: Kashaf Aman
command: /sp.analyze
labels: [analysis, quality-check]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - specs/002-rag-chatbot/spec.md
 - specs/002-rag-chatbot/plan.md
 - specs/002-rag-chatbot/tasks.md
 - .specify/memory/constitution.md
tests:
 - "No tests run"
---

## Prompt

---
description: Perform a non-destructive cross-artifact consistency and quality analysis across spec.md, plan.md, and tasks.md after task generation.
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Goal

Identify inconsistencies, duplications, ambiguities, and underspecified items across the three core artifacts (`spec.md`, `plan.md`, `tasks.md`) before implementation. This command MUST run only after `/sp.tasks` has successfully produced a complete `tasks.md`.

## Operating Constraints

**STRICTLY READ-ONLY**: Do **not** modify any files. Output a structured analysis report. Offer an optional remediation plan (user must explicitly approve before any follow-up editing commands would be invoked manually).

**Constitution Authority**: The project constitution (`.specify/memory/constitution.md`) is **non-negotiable** within this analysis scope. Constitution conflicts are automatically CRITICAL and require adjustment of the spec, plan, or tasks—not dilution, reinterpretation, or silent ignoring of the principle. If a principle itself needs to change, that must occur in a separate, explicit constitution update outside `/sp.analyze`.

## Execution Steps

### 1. Initialize Analysis Context

Run `.specify/scripts/powershell/check-prerequisites.ps1 -Json -RequireTasks -IncludeTasks` once from repo root and parse JSON for FEATURE_DIR and AVAILABLE_DOCS. Derive absolute paths:

- SPEC = FEATURE_DIR/spec.md
- PLAN = FEATURE_DIR/plan.md
- TASKS = FEATURE_DIR/tasks.md

Abort with an error message if any required file is missing (instruct the user to run missing prerequisite command).
For single quotes in args like "I'm Groot", use escape syntax: e.g 'I''m Groot' (or double-quote if possible: "I'm Groot").

### 2. Load Artifacts (Progressive Disclosure)

Load only the minimal necessary context from each artifact:

**From spec.md:**

- Overview/Context
- Functional Requirements
- Non-Functional Requirements
- User Stories
- Edge Cases (if present)

**From plan.md:**

- Architecture/stack choices
- Data Model references
- Phases
- Technical constraints

**From tasks.md:**

- Task IDs
- Descriptions
- Phase grouping
- Parallel markers [P]
- Referenced file paths

**From constitution:**

- Load `.specify/memory/constitution.md` for principle validation

### 3. Build Semantic Models

Create internal representations (do not include raw artifacts in output):

- **Requirements inventory**: Each functional + non-functional requirement with a stable key (derive slug based on imperative phrase; e.g., "User can upload file" → `user-can-upload-file`)
- **User story/action inventory**: Discrete user actions with acceptance criteria
- **Task coverage mapping**: Map each task to one or more requirements or stories (inference by keyword / explicit reference patterns like IDs or key phrases)
- **Constitution rule set**: Extract principle names and MUST/SHOULD normative statements

### 4. Detection Passes (Token-Efficient Analysis)

Focus on high-signal findings. Limit to 50 findings total; aggregate remainder in overflow summary.

#### A. Duplication Detection

- Identify near-duplicate requirements
- Mark lower-quality phrasing for consolidation

#### B. Ambiguity Detection

- Flag vague adjectives (fast, scalable, secure, intuitive, robust) lacking measurable criteria
- Flag unresolved placeholders (TODO, TKTK, ???, `<placeholder>`, etc.)

#### C. Underspecification

- Requirements with verbs but missing object or measurable outcome
- User stories missing acceptance criteria alignment
- Tasks referencing files or components not defined in spec/plan

#### D. Constitution Alignment

- Any requirement or plan element conflicting with a MUST principle
- Missing mandated sections or quality gates from constitution

#### E. Coverage Gaps

- Requirements with zero associated tasks
- Tasks with no mapped requirement/story
- Non-functional requirements not reflected in tasks (e.g., performance, security)

#### F. Inconsistency

- Terminology drift (same concept named differently across files)
- Data entities referenced in plan but absent in spec (or vice versa)
- Task ordering contradictions (e.g., integration tasks before foundational setup tasks without dependency note)
- Conflicting requirements (e.g., one requires Next.js while other specifies Vue)

### 5. Severity Assignment

Use this heuristic to prioritize findings:

- **CRITICAL**: Violates constitution MUST, missing core spec artifact, or requirement with zero coverage that blocks baseline functionality
- **HIGH**: Duplicate or conflicting requirement, ambiguous security/performance attribute, untestable acceptance criterion
- **MEDIUM**: Terminology drift, missing non-functional task coverage, underspecified edge case
- **LOW**: Style/wording improvements, minor redundancy not affecting execution order

### 6. Produce Compact Analysis Report

Output a Markdown report (no file writes) with the following structure:

## Specification Analysis Report

| ID | Category | Severity | Location(s) | Summary | Recommendation |
|----|----------|----------|-------------|---------|----------------|
| A1 | Duplication | HIGH | spec.md:L120-134 | Two similar requirements ... | Merge phrasing; keep clearer version |

(Add one row per finding; generate stable IDs prefixed by category initial.)

**Coverage Summary Table:**

| Requirement Key | Has Task? | Task IDs | Notes |
|-----------------|-----------|----------|-------|

**Constitution Alignment Issues:** (if any)

**Unmapped Tasks:** (if any)

**Metrics:**

- Total Requirements
- Total Tasks
- Coverage % (requirements with >=1 task)
- Ambiguity Count
- Duplication Count
- Critical Issues Count

### 7. Provide Next Actions

At end of report, output a concise Next Actions block:

- If CRITICAL issues exist: Recommend resolving before `/sp.implement`
- If only LOW/MEDIUM: User may proceed, but provide improvement suggestions
- Provide explicit command suggestions: e.g., "Run /sp.specify with refinement", "Run /sp.plan to adjust architecture", "Manually edit tasks.md to add coverage for 'performance-metrics'"

### 8. Offer Remediation

Ask the user: "Would you like me to suggest concrete remediation edits for the top N issues?" (Do NOT apply them automatically.)

## Operating Principles

### Context Efficiency

- **Minimal high-signal tokens**: Focus on actionable findings, not exhaustive documentation
- **Progressive disclosure**: Load artifacts incrementally; don't dump all content into analysis
- **Token-efficient output**: Limit findings table to 50 rows; summarize overflow
- **Deterministic results**: Rerunning without changes should produce consistent IDs and counts

### Analysis Guidelines

- **NEVER modify files** (this is read-only analysis)
- **NEVER hallucinate missing sections** (if absent, report them accurately)
- **Prioritize constitution violations** (these are always CRITICAL)
- **Use examples over exhaustive rules** (cite specific instances, not generic patterns)
- **Report zero issues gracefully** (emit success report with coverage statistics)

## Context

complete the task in @002-rag-chatbot

## Response snapshot

## Specification Analysis Report

| ID | Category | Severity | Location(s) | Summary | Recommendation |
|----|----------|----------|-------------|---------|----------------|
| C1 | Constitution | CRITICAL | .specify/memory/constitution.md | The project constitution is a template and has not been filled out. | Complete the constitution to define project principles and quality gates. |
| H1 | Coverage Gaps | HIGH | tasks.md | Non-functional requirements for performance, accuracy, and speed are not covered by any tasks. | Add specific tasks to test SC-001, SC-002, SC-003, and SC-004. |
| M1 | Underspecification | MEDIUM | tasks.md:L49 | Task T019 is a very large and complex UI task that could be broken down. | Decompose T019 into smaller, more manageable tasks for UI components, animations, and responsiveness. |
| L1 | Inconsistency | LOW | spec.md, tasks.md | Minor terminology drift between spec ('OpenAI Agents/ChatKit') and tasks ('agent.py'). | Unify terminology to 'RAG Agent' or a similar consistent name. |

**Coverage Summary Table:**

| Requirement Key | Has Task? | Task IDs | Notes |
|-----------------|-----------|----------|-------|
| FR-001 | ✅ | T019, T020 | |
| FR-002 | ✅ | T014, T015 | |
| FR-003 | ✅ | T017, T022 | |
| FR-004 | ✅ | T014 | |
| FR-005 | ✅ | T025, T031 | |
| FR-006 | ✅ | T025 | |
| FR-007 | ✅ | T033, T034 | |
| FR-008 | ✅ | T016 | |
| FR-009 | ✅ | T012 | |
| SC-001 | ❌ | | No performance testing task. |
| SC-002 | ❌ | | No accuracy testing task for refusals. |
| SC-003 | ❌ | | No ingestion speed testing task. |
| SC-004 | ❌ | | No hallucination testing task. |

**Constitution Alignment Issues:**

- The constitution is a template and provides no rules to align with. This is a **CRITICAL** issue.

**Unmapped Tasks:**

- All tasks are mapped to a user story or are part of the setup/foundational phases.

**Metrics:**

- Total Requirements: 13 (9 FR, 4 SC)
- Total Tasks: 36
- Coverage % (FRs): 100%
- Coverage % (SCs): 0%
- Critical Issues Count: 1
- High Issues Count: 1
- Medium Issues Count: 1
- Low Issues Count: 1

## Next Actions

- **CRITICAL**: The constitution should be filled out before starting implementation to ensure alignment on project standards. Run `/sp.constitution`.
- **HIGH**: Add tasks to `tasks.md` to cover the non-functional requirements (Success Criteria).
- You may proceed with implementation, but it is highly recommended to address the CRITICAL and HIGH severity issues first.

Would you like me to suggest concrete remediation edits for the top 2 issues?

## Outcome

- ✅ Impact: Generated a quality analysis report for the RAG chatbot feature, identifying critical and high-severity issues.
- 🧪 Tests: No tests were run.
- 📁 Files: Read 4 files.
- 🔁 Next prompts: User can choose to get remediation edits for the top 2 issues.
- 🧠 Reflection: The analysis revealed significant gaps in the project's setup, particularly the templated constitution and lack of non-functional requirement testing. This highlights the importance of the analyze command in catching issues early.

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): Suggest concrete remediation for the top issues.

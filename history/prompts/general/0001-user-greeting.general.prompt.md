---
id: 0001
title: User Greeting
stage: general
date: 2025-12-07
surface: agent
model: gemini-1.5-pro-a
feature: none
branch: main
user: Kashaf Aman
command: hi
labels: ["greeting"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
- history/prompts/general/0001-user-greeting.general.prompt.md
tests:

---

## Prompt

hi

## Response snapshot

Hello! How can I help you today?

## Outcome

- ✅ Impact: User greeted.
- 🧪 Tests: None
- 📁 Files: 1 file created.
- 🔁 Next prompts: User's next request.
- 🧠 Reflection: Acknowledged user greeting and created PHR.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
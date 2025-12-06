# Tasks: Docusaurus Book Structure

**Input**: Design documents from `/specs/1-docusaurus-book-structure/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: No explicit test tasks were requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create Docusaurus project in the repository root.
- [x] T002 Initialize `docusaurus.config.js` with basic project metadata and plugins.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T003 Add "Physical AI" sidebar and routing configuration in `docusaurus.config.js`.
- [x] T004 Generate empty markdown files for chapters (introduction.md, humanoid-robotics.md, ros2-fundamentals.md, digital-twin-simulation.md, nvidia-isaac.md, vla-systems.md, capstone-project.md) in `docs/physical-ai/`.
- [x] T005 Generate empty markdown file for weekly breakdown (`weekly-breakdown.md`) in `docs/physical-ai/`.

---

## Phase 3: User Story 1 - Read Physical AI Book Content (Priority: P1) 🎯 MVP

**Goal**: A user can navigate to the deployed Docusaurus site, browse through the chapters, and read the content.

**Independent Test**: Access the deployed Docusaurus site and verify content and navigation.

### Implementation for User Story 1

- [x] T006 [US1] Write content for Chapter 1: Introduction to Physical AI in `docs/physical-ai/introduction.md`.
- [x] T007 [US1] Write content for Chapter 2: Basics of Humanoid Robotics in `docs/physical-ai/humanoid-robotics.md`.
- [x] T008 [US1] Write content for Capstone: Autonomous Humanoid Project in `docs/physical-ai/capstone-project.md`.

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Access Tutorials (Priority: P2)

**Goal**: A user can find and follow the ROS 2, Gazebo, Isaac, and VLA tutorials within the book.

**Independent Test**: Locate and follow specified tutorials for ROS 2, Gazebo, Isaac, and VLA.

### Implementation for User Story 2

- [ ] T009 [US2] Write content for Chapter 3: ROS 2 Fundamentals (including tutorial) in `docs/physical-ai/ros2-fundamentals.md`.
- [ ] T010 [US2] Write content for Chapter 4: Digital Twin Simulation (Gazebo + Unity) (including tutorial) in `docs/physical-ai/digital-twin-simulation.md`.
- [ ] T011 [US2] Write content for Chapter 5: NVIDIA Isaac: AI-Robot Brain (including tutorial) in `docs/physical-ai/nvidia-isaac.md`.
- [ ] T012 [US2] Write content for Chapter 6: Vision-Language-Action (VLA) Systems (including tutorial) in `docs/physical-ai/vla-systems.md`.

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - View Weekly Breakdown (Priority: P3)

**Goal**: A user can find and view the "Weekly Breakdown" appendix.

**Independent Test**: Navigate to the appendix section of the Docusaurus site and verify content.

### Implementation for User Story 3

- [ ] T013 [US3] Write content for Weekly Breakdown section in `docs/physical-ai/weekly-breakdown.md`.

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T014 Add citations and references across all chapters (update `docs/physical-ai/**/*.md`).
- [ ] T015 Run plagiarism check on all book content.
- [ ] T016 Enable GitHub Pages deployment configuration in `docusaurus.config.js`.
- [ ] T017 Connect GitHub MCP server.
- [ ] T018 Implement PDF export functionality for the Docusaurus site.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Within Each User Story

- Content writing tasks for chapters can be done in parallel within their respective user story phases.
- Cross-cutting tasks like citations, plagiarism check, and PDF export should be done after content writing.

### Parallel Opportunities

- Tasks within Phase 1 and Phase 2 marked [P] can run in parallel. (None explicitly marked yet, but can be if granular)
- Once Foundational phase completes, User Story phases (Phase 3, 4, 5) can start in parallel (if team capacity allows).
- Within each user story, multiple content writing tasks can be done in parallel by different team members.
- Polish tasks (Phase 6) can be done in parallel where dependencies allow (e.g., plagiarism check and GitHub Pages deployment).

---

## Parallel Example: User Story 1

```bash
# Example of parallel content writing within User Story 1:
Task: "Write content for Chapter 1: Introduction to Physical AI in docs/physical-ai/introduction.md"
Task: "Write content for Chapter 2: Basics of Humanoid Robotics in docs/physical-ai/humanoid-robotics.md"
Task: "Write content for Capstone: Autonomous Humanoid Project in docs/physical-ai/capstone-project.md"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently (e.g., build Docusaurus and navigate to chapters)
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence

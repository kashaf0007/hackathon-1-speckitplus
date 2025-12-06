## User Input
Task: Generate the Docusaurus homepage (index.tsx) for Hackathon I: "Create a Textbook for Teaching Physical AI & Humanoid Robotics Course".

Instructions:
1. Read `specs.md` and `plan.md` for requirements.
2. Keep navbar and footer unchanged.
3. Add Hero section with title, subtitle, and "Get Started" button linking to /docs/intro.
4. Use React functional components and Docusaurus styling.
5. Output: Complete index.tsx ready to use.

## Tasks for Docusaurus Homepage

**Feature Name**: Docusaurus Homepage
**User Story**: Create Docusaurus homepage (index.tsx)

### Phase 1: Setup

(No specific project setup beyond what Docusaurus provides for this task.)

### Phase 2: Foundational Tasks

(No blocking prerequisites for this specific task.)

### Phase 3: User Story 1 (Create Docusaurus Homepage)

**Story Goal**: A fully functional Docusaurus homepage (`index.tsx`) with a Hero section and 2-3 feature cards, adhering to Docusaurus styling and React functional components.

**Independent Test Criteria**:
- The `index.tsx` file is created in `src/pages/`.
- The page builds successfully without errors.
- The Hero section displays the correct title, subtitle, and a functional "Get Started" button linking to `/docs/intro`.
- The navbar and footer remain unchanged.

**Implementation Tasks**:

- [ ] T001 [US1] in docusaurus folder the pages folder the `index.tsx` file for the Docusaurus homepage `src/pages/index.tsx`
- [ ] T002 [P] [US1] Implement the `Hero` component for the Docusaurus homepage `src/pages/index.tsx`
- [ ] T003 [US1] Integrate Hero and feature cards into `index.tsx` ensuring Docusaurus layout and styling `src/pages/index.tsx`

### Final Phase: Polish & Cross-Cutting Concerns

- [ ] T004 Build the Docusaurus project to verify no compilation errors occur
- [ ] T005 Run the Docusaurus development server to visually inspect the homepage

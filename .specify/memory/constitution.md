# SpeckitPlus Book Constitution

## Core Principles

### I. Clean and Maintainable Code
All code must be written in a clean, simple, and maintainable way. Follow SOLID principles and language-specific best practices.

### II. Test-Driven Development (TDD)
TDD is mandatory for all new features. Tests must be written before the implementation, they must fail before the implementation, and they must pass after the implementation. Use `pytest` for backend testing and a suitable framework (like Jest or Vitest) for frontend testing.

### III. API First and Documented
APIs are first-class citizens. All endpoints must be documented using the OpenAPI standard. FastAPI's automatic documentation generation should be leveraged.

### IV. Consistent Code Style
All Python code must be formatted with `black` and linted with `ruff`. All frontend code should follow standard Prettier and ESLint configurations.

### V. Semantic Versioning
The project follows semantic versioning (MAJOR.MINOR.PATCH). All breaking changes must be introduced in a new MAJOR version.

### VI. Git Workflow
All work must be done on feature branches. Feature branches should be named like `[feature-number]-[short-description]` (e.g., `002-rag-chatbot`). All changes must be submitted as Pull Requests (PRs) and reviewed by at least one other team member.

## Development Workflow

### Spec-Driven Development
All features must start with a specification (`spec.md`), a plan (`plan.md`), and tasks (`tasks.md`) before implementation begins. The `/sp.analyze` command should be run to ensure consistency.

### Quality Gates
- All tests must pass.
- Linting and formatting checks must pass.
- All conversations in a PR must be resolved.
- The PR must be approved by at least one reviewer.

## Governance
This constitution is the source of truth for all development practices. Any changes to this constitution must be proposed as a PR and approved by the project owner.

**Version**: 1.0.0 | **Ratified**: 2025-12-10 | **Last Amended**: 2025-12-10
# Research

## Deployment Platform

- **Decision**: We will use **Render** for deployment.
- **Rationale**: Render provides a simple and cost-effective way to deploy FastAPI applications and managed Postgres databases. It has a generous free tier that is suitable for this project's scale. Railway is another good option but has recently changed its pricing model. Fly.io is more focused on global distribution and might be overkill for this project.
- **Alternatives considered**: Railway, Fly.io.

## Scale and Scope

- **Decision**: We will assume a small to medium scale: up to 1,000 users and up to 10,000 documents (chunks).
- **Rationale**: This is a reasonable starting point for a personal project or a small team. The architecture can be scaled up later if needed.
- **Alternatives considered**: Assuming a larger scale would require more complex infrastructure and planning, which is not necessary at this stage.

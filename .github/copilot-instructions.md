# Repository instructions

This is a small server-rendered FastAPI application used in a learning workshop.

- Keep source code, identifiers, comments, and technical documentation in English.
- Keep workshop instructions and user-facing UI text in German. Enum values, form field names, routes, and sample identifiers stay in English.
- Preserve the current separation between routes, services, models, database code, and templates.
- Put business queries and commands in `app/services/`; routes should translate HTTP input and output.
- Use SQLModel sessions supplied by the FastAPI dependency in `app/database/db.py`.
- Keep the UI server-rendered with Jinja2. Do not introduce Node.js, a frontend build, or a JavaScript framework.
- Use only fictional names and data. Do not introduce customer or company references.
- Add or update pytest coverage when changing behavior.
- Run `uv run pytest` after code changes and report the result.
- Do not silently change public routes, domain enum values, or documented behavior.

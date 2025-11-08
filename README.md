# resume-tailor

resume-tailor/
 ├─ client/          # React / Next.js
 ├─ server/          # FastAPI or Express
 │   └─ tests/       # Unit tests (pytest/Jest)
 ├─ docs/
 │   ├─ architecture-diagram.png
 │   └─ api-reference.md
 ├─ .github/
 │   └─ workflows/   # CI pipeline for tests
 └─ README.md


resume-tailor/
 ├─ server/                 # FastAPI backend
 │   ├─ app/
 │   │   ├─ main.py
 │   │   ├─ routers/
 │   │   │   ├─ job.py
 │   │   │   ├─ resume.py
 │   │   ├─ services/
 │   │   │   ├─ job_parser.py
 │   │   │   ├─ ai_tailor.py
 │   │   ├─ tests/
 │   │   │   ├─ test_job.py
 │   │   │   ├─ test_resume.py
 │   ├─ requirements.txt
 │   └─ .env (gitignored)
 │
 ├─ client/                 # Next.js frontend
 │   ├─ pages/
 │   │   └─ index.tsx
 │   ├─ components/
 │   ├─ utils/
 │   ├─ package.json
 │   └─ .env.local (gitignored)
 │
 ├─ README.md
 └─ .github/
     └─ workflows/ci.yml (CI pipeline later)

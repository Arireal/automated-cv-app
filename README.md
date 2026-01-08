# CV Builder – ATS-Friendly Resume Generator

CV Builder is a Streamlit-based application designed to help job seekers quickly generate tailored, ATS-friendly CVs using **their own verified content**.

Instead of relying on AI to invent or rewrite experiences, this app reorganizes and selects pre-existing summaries, skills, projects, and experiences based on a pasted job description.



## Key Features

- Generate CVs optimized for specific job descriptions
- Content Library to manage:
  - Professional summaries
  - Skills
  - Projects
  - Work experiences
  - Education
  - Languages
- Multi-language CV support (EN, PT, ES, FR)
- Tag-based matching (no AI hallucinations)
- Export final CV as PDF
- Single-page app navigation with persistent top menu

##  Philosophy

This project focuses on:
- **Honesty** (no fabricated experience)
- **Speed** (reduce manual CV editing)
- **Control** (user always reviews and edits)
- **ATS compatibility**

AI may be added later, but the MVP works without it.

##  Tech Stack

- Python 3.10+
- Streamlit
- PDF generation (planned)
- Local state management (session_state)
- Git for version control

##  Project Structure

```text
.
├── app.py              # Main Streamlit app (router + UI)
├── .gitignore
├── README.md
└── generated_cvs/      # (optional) PDF output folder

import streamlit as st
from content_library import render_content_library
from settings import render_settings


# ===============================
# APP CONFIG
# ===============================
st.set_page_config(page_title="CV Builder", layout="wide")

if "current_page" not in st.session_state:
    st.session_state.current_page = "generate"

if "portfolios" not in st.session_state:
    st.session_state.portfolios = [
        {"name": "UX/UI Portfolio", "url": "https://"}
    ]


# ===============================
# TOP NAVIGATION (PERSISTENT)
# ===============================
nav1, nav2, nav3 = st.columns(3)

with nav1:
    if st.button("Generate CV"):
        st.session_state.current_page = "generate"

with nav2:
    if st.button("Content Library"):
        st.session_state.current_page = "library"

with nav3:
    if st.button("Settings"):
        st.session_state.current_page = "settings"

st.divider()



# ===============================
# PAGE: GENERATE CV
# ===============================
def render_generate_cv():
    st.title("Generate CV")
    st.caption(
        "Create an ATS-friendly CV by matching your existing content to a job description."
    )

    st.divider()

    # ---------- JOB DESCRIPTION ----------
    with st.container():
        st.subheader("Job Description")

        st.text_area(
            "Paste the job description here",
            height=220,
            placeholder=(
                "Paste the full job description. "
                "This text will be used only for keyword matching."
            ),
        )

        col1, col2 = st.columns(2)
        with col1:
            st.selectbox(
                "Target Role",
                ["UX/UI Designer", "Motion Designer", "Frontend Developer"],
            )
        with col2:
            st.selectbox(
                "CV Language",
                ["English", "Portuguese", "Spanish", "French"],
            )

    st.divider()

    # ---------- HEADER INFO ----------
    with st.container():
        st.subheader("CV Header")

        col1, col2 = st.columns(2)
        with col1:
            st.text_input(
                "Professional Title",
                "UX/UI Designer Specialist & Front-End Developer",
            )
            st.text_input("Full Name", "Your Name")
        with col2:
            st.text_input("Email", "you@email.com")

        st.markdown("**Portfolio Links**")

        for i, portfolio in enumerate(st.session_state.portfolios):
            c1, c2, c3 = st.columns([3, 6, 1])
            with c1:
                portfolio["name"] = st.text_input(
                    f"Portfolio name {i}",
                    portfolio["name"],
                    label_visibility="collapsed",
                )
            with c2:
                portfolio["url"] = st.text_input(
                    f"Portfolio URL {i}",
                    portfolio["url"],
                    label_visibility="collapsed",
                )
            with c3:
                if st.button("🗑", key=f"delete_portfolio_{i}"):
                    st.session_state.portfolios.pop(i)
                    st.experimental_rerun()

        if st.button("+ Add portfolio"):
            st.session_state.portfolios.append({"name": "", "url": "https://"})
            st.experimental_rerun()

    st.divider()

    # ---------- PROFESSIONAL SUMMARY ----------
    with st.container():
        st.subheader("Professional Summary")
        st.text_area(
            "Selected summary",
            height=120,
            placeholder="Auto-selected summary will appear here. You can edit it manually.",
        )

    st.divider()

    # ---------- KEY SKILLS ----------
    with st.container():
        st.subheader("Key Skills")

        skills = [
            "User Research",
            "UX/UI Design",
            "Figma",
            "Agile Collaboration",
            "Communication",
            "React.js",
            "Tailwind CSS",
            "Motion Design",
        ]

        cols = st.columns(2)
        for i, skill in enumerate(skills):
            with cols[i % 2]:
                st.checkbox(skill, value=True)

        st.caption(
            "Skills are auto-selected based on the job description. "
            "You can adjust them manually."
        )

    st.divider()

    # ---------- RELATED PROJECTS ----------
    with st.container():
        st.subheader("Related Projects")

        projects = [
            "StrengthsAsia – Information Architecture",
            "ADW Studium – SaaS Landing Page",
            "Google for Education – Trifold Brochure",
            "Kinkoa – Digital Menu",
        ]

        for project in projects:
            st.checkbox(project, value=True)

    st.divider()

    # ---------- EXPERIENCE ----------
    with st.container():
        st.subheader("Experience")

        experiences = [
            "UX/UI Designer | StrengthsAsia (2025)",
            "UX/UI Designer & Frontend Developer | Hello Innovation (2024–2025)",
            "Lead UX/UI Designer | Vila Velha Insurance Broker (2024–2025)",
            "Frontend Architect & UX Analyst | Genotec (2022)",
        ]

        for i, exp in enumerate(experiences):
            with st.expander(exp, expanded=True):
                st.checkbox(
                    "Include this experience",
                    value=True,
                    key=f"experience_include_{i}"
                )
                st.markdown(
                    "• Example bullet point describing responsibilities and impact."
                )

    # ---------- EDUCATION ----------
    with st.container():
        st.subheader("Education")

        st.checkbox(
            "Frontend Development Bootcamp – Le Wagon (2021)", value=True
        )
        st.checkbox(
            "Bachelor’s Degree in Graphic Design – UNIFACS (2018)", value=True
        )

    st.divider()

    # ---------- LANGUAGES ----------
    with st.container():
        st.subheader("Languages")

        st.checkbox("English – Fluent (C2)", value=True)
        st.checkbox("Portuguese – Native", value=True)
        st.checkbox("French – Advanced (B2)", value=False)

    st.divider()

    # ---------- SOCIAL LINKS ----------
    with st.container():
        st.subheader("Social Links")

        st.checkbox("LinkedIn", value=True)
        st.checkbox("GitHub", value=False)
        st.checkbox("Behance", value=False)

    st.divider()

    # ---------- FINAL ACTIONS ----------
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.button("Preview CV")
        with col2:
            st.button("Download PDF")


# ===============================
# PAGE: CONTENT LIBRARY (PLACEHOLDER)
# ===============================



# ===============================
# PAGE: SETTINGS (PLACEHOLDER)
# ===============================



# ===============================
# ROUTER
# ===============================
if st.session_state.current_page == "generate":
    render_generate_cv()

elif st.session_state.current_page == "library":
    render_content_library()

elif st.session_state.current_page == "settings":
    render_settings()


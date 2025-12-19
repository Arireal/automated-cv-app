import streamlit as st


def render_settings():
    st.title("Settings")
    st.caption(
        "General preferences and app behavior. "
        "These settings affect how CVs are generated, not the content itself."
    )

    # ---------- GENERAL ----------
    with st.container():
        st.subheader("General")

        default_role = st.selectbox(
            "Default target role",
            ["UX/UI Designer", "Motion Designer", "Frontend Developer"]
        )

        default_language = st.selectbox(
            "Default CV language",
            ["English", "Portuguese", "Spanish", "French"]
        )

        auto_select = st.checkbox(
            "Auto-select content when generating a CV",
            value=True,
            help="If disabled, all selections must be made manually on the Generate CV page."
        )

    st.divider()

    # ---------- CV GENERATION RULES ----------
    with st.container():
        st.subheader("CV Generation Rules")

        max_skills = st.slider(
            "Maximum number of skills",
            min_value=3,
            max_value=15,
            value=8
        )

        max_projects = st.slider(
            "Maximum number of projects",
            min_value=1,
            max_value=6,
            value=4
        )

        max_experiences = st.slider(
            "Maximum number of experience entries",
            min_value=1,
            max_value=8,
            value=5
        )

    st.divider()

    # ---------- PDF OUTPUT ----------
    with st.container():
        st.subheader("PDF Output")

        st.checkbox(
            "Use ATS-friendly layout",
            value=True,
            disabled=True,
            help="The layout follows a fixed ATS-optimized structure and cannot be changed."
        )

        file_naming = st.text_input(
            "PDF file name pattern",
            value="CV_{role}_{language}.pdf",
            help="Available variables: {role}, {language}"
        )

    st.divider()

    # ---------- DATA & STORAGE ----------
    with st.container():
        st.subheader("Data & Storage")

        st.info("Your content is stored locally. No data is generated or modified automatically.")

        col1, col2 = st.columns(2)
        with col1:
            st.button("Export content library")
        with col2:
            st.button("Import content library")

    st.divider()

    # ---------- ADVANCED ----------
    with st.container():
        st.subheader("Advanced")

        st.checkbox(
            "Enable experimental features",
            value=False,
            help="Includes upcoming automation features that may change behavior."
        )

        st.button("Reset all settings")

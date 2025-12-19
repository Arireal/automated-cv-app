import streamlit as st


def render_content_library():
    st.title("Content Library")
    st.caption(
        "Manage all reusable content used to generate your CVs. "
        "Nothing here is auto-generated."
    )

    # ---------- TABS ----------
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "Summaries",
        "Skills",
        "Projects",
        "Experience",
        "Education",
        "Languages"
    ])

    # ---------- SUMMARIES ----------
    with tab1:
        st.subheader("Professional Summaries")
        st.caption("Short summaries (3–4 lines). One will be selected automatically per CV.")

        summaries = [
            {
                "title": "UX/UI Summary",
                "language": "English",
                "tags": "ux, ui, figma, research",
                "text": "UX/UI Designer with 6+ years of experience crafting scalable digital products."
            }
        ]

        for i, summary in enumerate(summaries):
            with st.expander(summary["title"], expanded=False):
                st.text_input("Language", summary["language"], key=f"sum_lang_{i}")
                st.text_input("Tags", summary["tags"], key=f"sum_tags_{i}")
                st.text_area("Summary Text", summary["text"], height=120, key=f"sum_text_{i}")
                st.button("Delete", key=f"delete_summary_{i}")

        st.button("+ Add new summary")

    # ---------- SKILLS ----------
    with tab2:
        st.subheader("Skills Library")
        st.caption("Skills are selected automatically based on tag matching.")

        skills = [
            {"name": "User Research", "tags": "ux, research", "language": "English"},
            {"name": "Figma", "tags": "ui, figma", "language": "English"}
        ]

        for i, skill in enumerate(skills):
            c1, c2, c3, c4 = st.columns([3, 4, 2, 1])
            c1.text_input("Skill", skill["name"], key=f"skill_name_{i}")
            c2.text_input("Tags", skill["tags"], key=f"skill_tags_{i}")
            c3.text_input("Language", skill["language"], key=f"skill_lang_{i}")
            c4.button("🗑", key=f"delete_skill_{i}")

        st.button("+ Add skill")

    # ---------- PROJECTS ----------
    with tab3:
        st.subheader("Projects")

        projects = [
            {
                "name": "StrengthsAsia",
                "description": "Information architecture and data visualization",
                "url": "https://",
                "tags": "ux, information architecture",
                "language": "English"
            }
        ]

        for i, project in enumerate(projects):
            with st.expander(project["name"], expanded=False):
                st.text_input("Project Name", project["name"], key=f"proj_name_{i}")
                st.text_area("Description", project["description"], key=f"proj_desc_{i}")
                st.text_input("Project URL", project["url"], key=f"proj_url_{i}")
                st.text_input("Tags", project["tags"], key=f"proj_tags_{i}")
                st.text_input("Language", project["language"], key=f"proj_lang_{i}")
                st.button("Delete project", key=f"delete_project_{i}")

        st.button("+ Add project")

    # ---------- EXPERIENCE ----------
    with tab4:
        st.subheader("Experience")

        experiences = [
            {
                "role": "UX/UI Designer",
                "company": "StrengthsAsia",
                "period": "2025",
                "bullets": "Redesigned data-heavy reports into UX-driven layouts.",
                "tags": "ux, data, research",
                "language": "English"
            }
        ]

        for i, exp in enumerate(experiences):
            with st.expander(f"{exp['role']} | {exp['company']}", expanded=False):
                st.text_input("Role", exp["role"], key=f"exp_role_{i}")
                st.text_input("Company", exp["company"], key=f"exp_company_{i}")
                st.text_input("Period", exp["period"], key=f"exp_period_{i}")
                st.text_area("Bullet Points", exp["bullets"], height=120, key=f"exp_bullets_{i}")
                st.text_input("Tags", exp["tags"], key=f"exp_tags_{i}")
                st.text_input("Language", exp["language"], key=f"exp_lang_{i}")
                st.button("Delete experience", key=f"delete_exp_{i}")

        st.button("+ Add experience")

    # ---------- EDUCATION ----------
    with tab5:
        st.subheader("Education")
        st.text_input("Degree", "Bachelor’s Degree in Graphic Design")
        st.text_input("Institution", "UNIFACS")
        st.text_input("Year", "2018")
        st.button("+ Add education")

    # ---------- LANGUAGES ----------
    with tab6:
        st.subheader("Languages")
        st.text_input("Language", "English")
        st.selectbox("Proficiency", ["Basic", "Intermediate", "Advanced", "Fluent", "Native"])
        st.button("+ Add language")

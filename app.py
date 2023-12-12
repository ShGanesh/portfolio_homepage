import streamlit as st

# Projects Data
projects = [
    {
        "title": "Research Paper Summarizer",
        "description": "A tool to summarize research papers intelligently. It first splits the paper in sections by the titles, and summarizes them part by part.",
        "tech_stack": ["Technology 1", "Technology 2"],
        "screenshot": "images/profile_pic.jpg",
        "url": "https://github.com/your-username/project1",
    },
    {
        "title": "Project 2 Title",
        "description": "Another brief description of the project.",
        "tech_stack": ["Technology 3", "Technology 4"],
        "screenshot": "images/profile_pic.jpg",
        "url": "https://github.com/your-username/project2",
    },
    # ... Add more projects ...
]

# Skills Data
skills = [
    {"name": "Natural Language Processing", "proficiency": 90},
    {"name": "Computer Vision", "proficiency": 80},
    {"name": "Deep Learning", "proficiency": 95},
]

# Layout

# Homepage
st.markdown("# Welcome to my portfolio!")
st.markdown("I'm MC Sharen Ganesh, a passionate Machine Learning and LLM enthusiast.")
st.markdown("I'm skilled in stuff here and there.")
st.markdown("Check out my projects below.")
st.link_button("Explore Projects", '#Projects')

# Projects
st.markdown("## Projects")
lst_projects = list(d["title"] for d in projects)
project_tabs = st.tabs(lst_projects)
for i, project in enumerate(projects):
    with project_tabs[i]:
        col1, col2 = st.columns(2)
        with col1:
            st.image(project["screenshot"], width=300)
        with col2:
            st.markdown("### " + project["title"])
            st.markdown(project["description"])
            st.markdown("**Tech Stack:** " + ", ".join(project["tech_stack"]))

# Skills
st.markdown("## Skills")
for skill in skills:
    st.markdown(f"**{skill['name']}:**  {skill['proficiency']}%")
    st.progress(skill["proficiency"] / 100)

# Contact
st.markdown("## Contact")
st.markdown("Email: mc.sharen.ganesh@gmail.com")
st.markdown("LinkedIn: https://www.linkedin.com/in/shganesh/")
st.markdown("GitHub: https://github.com/ShGanesh")

# Footer
st.markdown("Copyright © 2023 ShGanesh. All rights reserved.")


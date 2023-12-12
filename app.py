import streamlit as st
import base64
import os

# Projects Data
projects = [
    {
        "title": "Research Paper Summarizer",
        "description": "A tool to summarize research papers intelligently. It first splits the paper in sections by the titles, and summarizes them part by part.",
        "tech_stack": ["Technology 1", "Technology 2"],
        "screenshot": "images/profile_pic.jpg",
        "proj_skills": ["Natural Language Processing", "Langchain", "Deep Learning"],
        "url": "https://github.com/your-username/project1",
    },
    {
        "title": "Project 2 Title",
        "description": "Another brief description of the project.",
        "tech_stack": ["Technology 3", "Technology 4"],
        "screenshot": "images/profile_pic.jpg",
        "proj_skills": ["Computer Vision", "Natural Language Processing"],
        "url": "https://github.com/your-username/project2",
    },
    # ... TODO: Add more projects ...
]

# Skills Data
skills = [
    {"name": "Natural Language Processing", "proficiency": 90, "description": "Natural Language Processing (NLP) is the field of AI concerned with enabling computers to understand, interpret, and manipulate human language."},
    {"name": "Computer Vision", "proficiency": 80, "description": "Computer vision (CV) is a subfield of AI that enables computers to extract meaningful information from digital images and videos for automated understanding and action."},
    {"name": "Deep Learning", "proficiency": 95, "description": "Deep learning is a subfield of machine learning that uses artificial neural networks with multiple layers to learn complex representations of data."},
]
# TODO: Correct and apend to the skills


# Display PDF
def displayPDF():
    # Creates a window to viewa PDF.
    file = "files\Ganesh_Resumex09.pdf"
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')     
    # Embedding PDF
    pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="450" height="580" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

# Retrieve PDF
def getPDF():
    # Returns object that can be used to download a PDF
    file = "files/Ganesh_Resumex09.pdf"
    with open(file, "rb") as f:
        PDFbyte = f.read()
        return PDFbyte

# Get Project Data by Skill
def get_proj_by_skill(skill):
    # Input: String - Skill (Like "Computer Vision", "Deep Learning", etc)
    # Output: list of dictionaries of all projects that have this skill
    filtered_projects = []
    for project in projects:
        if skill in project["proj_skills"]:
            filtered_projects.append(project)
    return filtered_projects

def expander(lst, name):
    # Input: List of dictionaries of projects
    # Output: Expander object, with tabs of projects inside
    with st.expander(f"See my {name} Projects"):
        # Lists project titles correnponding to function argument
        lst_projects = []
        for d in lst:
            lst_projects.append(d['title'])
        # Create tabs for each project
        project_tabs = st.tabs(lst_projects)
        for i, project in enumerate(lst):
            with project_tabs[i]:
                col1, col2 = st.columns(2)
                with col1:
                    st.image(project["screenshot"], width=300)
                with col2:
                    st.markdown("### " + project["title"])
                    st.markdown(project["description"])
                    st.markdown("**Tech Stack:** " + ", ".join(project["tech_stack"]))
                    st.link_button("Visit the project", project["url"], help=f"Directed to {project['url']}")

# Layout
# Homepage
st.markdown("# Welcome to my portfolio!")
st.markdown(os.listdir("."))
st.markdown(os.listdir("./images"))
st.markdown(os.listdir("./files"))

st.markdown("I'm MC Sharen Ganesh, a passionate Machine Learning and LLM enthusiast.")
st.markdown("I'm skilled in stuff here and there.")
displayPDF()
st.download_button("Download my resume", data = getPDF(), file_name="ShGanesh_Resume.pdf", mime='application/octet-stream') 
st.markdown("Check out my projects below.")

st.markdown("***")
# Skills
st.markdown("## Skills")
for skill in skills:
    st.markdown(f"""
                **{skill['name']}:**  
                {skill['description']}
                """)

    proj_list = get_proj_by_skill(skill['name'])
    expander(proj_list, skill['name'])

st.markdown("***")
# Contact
st.markdown("## Contact")
st.markdown("Email: mc.sharen.ganesh@gmail.com")
st.markdown("LinkedIn: https://www.linkedin.com/in/shganesh/")
st.markdown("GitHub: https://github.com/ShGanesh")

st.markdown("***")
# Footer
st.markdown("Copyright © 2023 ShGanesh. All rights reserved.")


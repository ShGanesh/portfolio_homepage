import streamlit as st
import base64

# Projects Data
projects = [
    {
        "title": "Research Paper Summarizer",
        "description": "A tool to summarize research papers intelligently. It first splits the paper in sections according to semantic sense and summarizes them part by part. There are nine levels of abstractions a user can choose from.",
        "tech_stack": ["Streamlit", "Google GenAI (Gemini)"],
        "screenshot": "images/summarizer_ss.png",
        "proj_skills": ["Natural Language Processing", "Google Generative AI"],
        "url": "https://summarizer-shganesh.streamlit.app/",
    },
    {
        "title": "Implementation of Transformers paper in PyTorch",
        "description": "Implementation(s) of paper by Vaswani et al.",
        "tech_stack": ["LlamaIndex", "BertTokenizer"],
        "screenshot": "images/attention.png",
        "proj_skills": ["PyTorch", "Natural Language Processing", "Deep Learning"],
        "url": "https://github.com/ShGanesh/Attention-Paper-pytorch",
    },
    {
        "title": "RAG model for retrieval of HR policies",
        "description": "Retrieval-Augmented Generation (RAG) is an AI framework for retrieving facts from an external knowledge base. It was used to help me ",
        "tech_stack": ["FAISS", "LangChain", "LlamaIndex", ],
        "screenshot": "images/rag.png",
        "proj_skills": ["LangChain", "Natural Language Processing", "HuggingFace"],
        "url": "https://github.com/ShGanesh/RAG",
    },
    # ... TODO: Add more projects ...
]

# Skills Data
skills = [
    {"name": "Natural Language Processing", "proficiency": 0, "description": "Natural Language Processing (NLP) is the field of AI concerned with enabling computers to understand, interpret, and manipulate human language."},
#    {"name": "Computer Vision", "proficiency": 0, "description": "Computer vision (CV) is a subfield of AI that enables computers to extract meaningful information from digital images and videos for automated understanding and action."},
    {"name": "Deep Learning", "proficiency": 0, "description": "Deep learning is a subfield of machine learning that uses artificial neural networks with multiple layers to learn complex representations of data."},
    {"name": "HuggingFace", "proficiency": 0, "description": "HuggingFace is an Open-Source hub for pre-trained models and AI/DL development tools"},
    {"name": "PyTorch", "proficiency": 0, "description": "PyTorch is a powerful library used for training Deep Neural Networks."},
    {"name": "LangChain", "proficiency": 0, "description": "Langchain is an Open-Source language model integration framework."},
]
# TODO: Correct and append to the skills


# Display PDF
def displayPDF():
    # Creates a window to viewa PDF.
    file = "files/Ganesh_Resumex09.pdf"
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
        if len(lst_projects) == 0:
            return None
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
st.markdown("I'm MC Sharen Ganesh, a passionate Machine Learning and LLM enthusiast.")
st.markdown("I'm skilled in stuff here and there.")
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
st.markdown("Copyright © 2024 ShGanesh. All rights reserved.")


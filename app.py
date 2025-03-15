import streamlit as st
import plotly.graph_objects as go

# Page Configuration
st.set_page_config(
    page_title="Ashesh Raj Gnawali - Portfolio",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for dark theme and sleek design
st.markdown("""
    <style>
    /* Overall theme */
    .stApp {
        background-color: #121212;
        color: #e0e0e0;
    }

    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #1e1e1e;
        padding: 2rem 1rem;
    }

    /* Headers */
    h1, h2, h3, h4, h5, h6 {
        color: #bb86fc;
        font-weight: 500;
    }

    /* Links */
    a {
        color: #03dac6 !important;
    }
    a:hover {
        color: #018786 !important;
        text-decoration: none;
    }

    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: transparent;
        border-radius: 4px 4px 0 0;
        gap: 1px;
        padding-top: 10px;
        padding-bottom: 10px;
        color: #e0e0e0;
    }
    .stTabs [aria-selected="true"] {
        background-color: #1e1e1e;
        color: #bb86fc;
        border-bottom: 2px solid #bb86fc;
    }

    /* Cards */
    .card {
        background-color: #1e1e1e;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 16px;
        border-left: 3px solid #bb86fc;
    }

    /* Skill tags */
    .skill-tag {
        background-color: #2d2d2d;
        color: #03dac6;
        padding: 5px 10px;
        border-radius: 4px;
        margin-right: 6px;
        margin-bottom: 6px;
        display: inline-block;
        font-size: 0.8rem;
    }

    /* Images */
    img {
        border-radius: 8px;
    }

    /* Dividers */
    hr {
        border-color: #333;
    }

    /* Footer */
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        background-color: #1e1e1e;
        color: #e0e0e0;
        text-align: center;
        padding: 10px 0;
    }

    .footer img {
        height: 20px;
        vertical-align: middle;
        margin-top: -5px;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://via.placeholder.com/300", use_container_width=True)
    st.markdown("<h2 style='text-align: center; margin-bottom: 0px;'>Ashesh Raj Gnawali</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #bb86fc; margin-top: 0px;'>Data Scientist & ML Engineer</p>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 📍 Oslo, Norway")
    st.markdown("### 📧 [ashez2051@gmail.com](mailto:ashez2051@gmail.com)")
    st.markdown("### 🔗 [LinkedIn Profile](https://www.linkedin.com/in/ashesh-raj-gnawali/)")
    st.markdown("### 📞 (+47) 93671761")

    st.markdown("---")
    st.markdown("### Education")
    st.markdown("**MSc in Data Science**")
    st.markdown("Norwegian University of Life Sciences")
    st.markdown("**BEng in Electrical Engineering**")
    st.markdown("Tribhuvan University")
    st.markdown("---")
    st.markdown("### Certifications")
    st.markdown("✅ [Professional Scrum Master (PSM II)](https://www.credly.com/badges/67227184-d4e6-450b-a644-5862bd4410c6/linked_in_profile)")
    st.markdown("✅ [Professional Scrum Master (PSM I)](https://www.credly.com/badges/392b6543-def7-47e5-8b96-5adced6d21f1/linked_in_profile)")

# Main Content
st.markdown("<h1 style='text-align: center;'>Data Science Portfolio</h1>", unsafe_allow_html=True)

# Brief introduction
st.markdown("""
<div style='background-color: #1e1e1e; padding: 20px; border-radius: 8px; margin-bottom: 25px;'>
Proven success in developing predictive models, saving costs, and optimizing operations. Skilled in building data pipelines and ETL processes using Azure and Apache Airflow. Proficient in creating actionable insights and dashboards with PowerBI and Python. Experienced in cross-functional collaboration to deliver data-driven solutions.
</div>
""", unsafe_allow_html=True)

# Create tabs for better organization
tabs = st.tabs(["🛠️ Skills", "🚀 WebApp Projects", "📝 Publications"])

# Tab 1: Skills & Tools
with tabs[0]:
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### Core Competencies")

        # Create a radar chart for skills
        categories = ['Predictive Modeling', 'Data Pipelines', 'ETL Processes',
                      'Dashboard Creation', 'Cross-functional Collaboration', 'Agile Methodologies']
        values = [85, 70, 70, 85, 85, 80]

        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            line_color='#bb86fc',
            fillcolor='rgba(187, 134, 252, 0.2)'
        ))

        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100]
                )
            ),
            showlegend=False,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            height=400,
            margin=dict(l=80, r=80, t=20, b=20)
        )
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### Technical Stack")

        st.markdown("#### AI & Machine Learning")
        st.markdown("""
        <span class='skill-tag'>Azure ML</span>
        <span class='skill-tag'>Scikit-learn</span>
        <span class='skill-tag'>TensorFlow</span>
        <span class='skill-tag'>LangChain</span>
        <span class='skill-tag'>OpenAI</span>
        <span class='skill-tag'>RAG</span>
        <span class='skill-tag'>Docker</span>
        """, unsafe_allow_html=True)

        st.markdown("#### Data Engineering")
        st.markdown("""
        <span class='skill-tag'>Azure DataFactory</span>
        <span class='skill-tag'>Azure DataFlow</span>
        <span class='skill-tag'>Apache Airflow</span>
        <span class='skill-tag'>DBT</span>
        <span class='skill-tag'>Azure Containerization</span>
        <span class='skill-tag'>Azure Container Instances</span>
        """, unsafe_allow_html=True)

        st.markdown("#### Programming & Databases")
        st.markdown("""
        <span class='skill-tag'>Python</span>
        <span class='skill-tag'>R</span>
        <span class='skill-tag'>SQL</span>
        <span class='skill-tag'>DAX</span>
        <span class='skill-tag'>SSAS</span>
        """, unsafe_allow_html=True)

        st.markdown("#### Visualization")
        st.markdown("""
        <span class='skill-tag'>PowerBI</span>
        <span class='skill-tag'>Matplotlib</span>
        <span class='skill-tag'>Seaborn</span>
        <span class='skill-tag'>Plotly</span>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# Tab 2: WebApp Projects
with tabs[1]:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### WebApp Projects")

    # Sample Streamlit apps
    apps = [
        {"title": "Amortization Calculator App", "description": "A portfolio showcasing data science projects and skills.", "link": "https://asheshrajgnawali-amortization-calculator-app.streamlit.app/"},
        #{"title": "Analytics Dashboard", "description": "An interactive dashboard for data analytics and visualization.", "link": "https://your-dashboard-link.com"},
        #{"title": "Machine Learning App", "description": "A web app for exploring machine learning models and predictions.", "link": "https://your-ml-app-link.com"}
    ]

    for app in apps:
        st.markdown(f"<a href='{app['link']}' style='text-decoration:none; color: inherit;'><div class='card' style='margin-bottom: 20px;'><h3>{app['title']}</h3><p>{app['description']}</p></div></a>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# Tab 3: Publications
with tabs[2]:
    st.markdown("<div class='section-bar'><h3>Publications</h3></div>", unsafe_allow_html=True)
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    # Updated publication entries
    publications = [
        {
            "title": "Handling Slowly Changing Dimensions Using PySpark in Microsoft Fabric",
            "description": """
            Data warehousing is essential for businesses to monitor trends, gain insights, and make data-driven strategic decisions.
            It involves storing and handling extensive data from various sources in a centralized location.
            Slowly Changing Dimensions (SCD) is a key concept in data warehousing designed to handle the evolving nature of dimension data.
            This article explores the implementation of SCD-1 and SCD-2 techniques using Spark Notebooks in Microsoft Fabric.
            """,
            "platform": "Hashnode",
            "link": "https://datacrafts.hashnode.dev/handling-slowly-changing-dimensions-using-pyspark-in-microsoft-fabric"
        },
        {
            "title": "Cardiac Computational Modelling",
            "abstract": """
            <strong>Abstract</strong><br>
            This thesis aims to model heart function using data-driven approaches to complement traditional mechanistic models, which are computationally intensive. It explores metamodeling techniques, specifically HC-PLSR and Deep Learning, to emulate the Pandit-Hinch-Niederer model for rat cardiac excitation-contraction. By using Latin hypercube sampling for input variation and recording action potentials, the study demonstrates that deep learning provides powerful emulation, while HC-PLSR offers comprehensive model behavior insights. The findings underscore the importance of subspace analysis in understanding complex model behaviors.
            """,
            "platform": "Research Publication",
            "link": "https://nmbu.brage.unit.no/nmbu-xmlui/handle/11250/2789007"
        }
    ]

    for pub in publications:
        st.markdown(f"**{pub['title']}**")
        if "description" in pub:
            st.markdown(f"{pub['description']}")
        if "abstract" in pub:
            st.markdown(f"{pub['abstract']}", unsafe_allow_html=True)
        st.markdown(f"*{pub['platform']}*")
        st.markdown(f"[Read more]({pub['link']})", unsafe_allow_html=True)
        st.markdown("---")

    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        <p>© 2025 Ashesh Raj Gnawali</p>
    </div>
""", unsafe_allow_html=True)

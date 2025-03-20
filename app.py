import streamlit as st
import plotly.graph_objects as go
import math
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="Ashesh Raj Gnawali - Portfolio",
    layout="wide",
    initial_sidebar_state="expanded"
)

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
    st.markdown("""
    <div style='text-align: center; padding: 0px 10px 15px 10px;'>
        <h2 style='margin-bottom: 5px; color: white;'>Ashesh Raj Gnawali</h2>
        <p style='color: #bb86fc; margin-top: 0px; font-size: 16px;'>Data Scientist | AI Engineer | Analytics Engineer</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style='padding: 0px 10px; margin-bottom: 15px;'>
        <div style='display: flex; align-items: center; margin-bottom: 8px;'>
            <div style='width: 24px; margin-right: 10px;'>📍</div>
            <div>Oslo, Norway</div>
        </div>
        <div style='display: flex; align-items: center; margin-bottom: 8px;'>
            <div style='width: 24px; margin-right: 10px;'>📧</div>
            <div><a href='mailto:ashez2051@gmail.com' style='color: #bb86fc; text-decoration: none;'>ashez2051@gmail.com</a></div>
        </div>
        <div style='display: flex; align-items: center; margin-bottom: 8px;'>
            <div style='width: 24px; margin-right: 10px;'>🔗</div>
            <div><a href='https://www.linkedin.com/in/ashesh-raj-gnawali/' target='_blank' style='color: #bb86fc; text-decoration: none;'>LinkedIn Profile</a></div>
        </div>
        <div style='display: flex; align-items: center; margin-bottom: 8px;'>
            <div style='width: 24px; margin-right: 10px;'>📞</div>
            <div>(+47) 93671761</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Divider
    st.markdown("<hr style='margin: 15px 0px; border-color: #333;'>", unsafe_allow_html=True)
    
    # Education
    st.markdown("""
    <div style='padding: 0px 10px;'>
        <h3 style='margin-bottom: 12px; color: white;'>Education</h3>
        <div style='margin-bottom: 12px;'>
            <p style='margin: 0; font-weight: bold; color: white;'>MSc in Data Science</p>
            <p style='margin: 0; font-size: 14px; color: #bbbbbb;'>Norwegian University of Life Sciences</p>
        </div>
        <div style='margin-bottom: 15px;'>
            <p style='margin: 0; font-weight: bold; color: white;'>BEng in Electrical Engineering</p>
            <p style='margin: 0; font-size: 14px; color: #bbbbbb;'>Tribhuvan University</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<hr style='margin: 15px 0px; border-color: #333;'>", unsafe_allow_html=True)
    
    # Certifications 
    st.markdown("""
    <div style='padding: 0px 10px;'>
        <h3 style='margin-bottom: 12px; color: white;'>Certifications</h3>
        <div style='display: flex; align-items: flex-start; margin-bottom: 10px;'>
            <div style='color: #4CAF50; margin-right: 8px;'>✅</div>
            <div>
                <a href='https://www.credly.com/badges/67227184-d4e6-450b-a644-5862bd4410c6/linked_in_profile' 
                   target='_blank' style='color: #bb86fc; text-decoration: none;'>
                   Professional Scrum Master (PSM II)
                </a>
            </div>
        </div>
        <div style='display: flex; align-items: flex-start; margin-bottom: 10px;'>
            <div style='color: #4CAF50; margin-right: 8px;'>✅</div>
            <div>
                <a href='https://www.credly.com/badges/392b6543-def7-47e5-8b96-5adced6d21f1/linked_in_profile' 
                   target='_blank' style='color: #bb86fc; text-decoration: none;'>
                   Professional Scrum Master (PSM I)
                </a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Brief introduction
st.markdown("""
<div style='background-color: #1e1e1e; padding: 20px; border-radius: 8px; margin-bottom: 25px; border-left: 3px solid #bb86fc;'>
<ul style='margin: 0; padding-left: 20px; line-height: 1.8; font-size: 15px; color: white;'>
    <li>Proven success in developing predictive models, saving costs, and optimizing operations.</li>
    <li>Skilled in building data pipelines and ETL processes using Azure and Apache Airflow.</li>
    <li>Proficient in creating actionable insights and dashboards with PowerBI and Python.</li>
    <li>Experienced in cross-functional collaboration to deliver data-driven solutions.</li>
</ul>
</div>
""", unsafe_allow_html=True)



# Create tabs 
tabs = st.tabs(["🛠️ Skills", "🚀 WebApp Projects", "📝 Publications"])

# Tab 1: Skills & Tools
with tabs[0]:
    selected_option = st.radio(
        "#### Select View:",
        ["Technical Stack", "Core Competencies"],
        horizontal=True,
        key="view_selector"
    )
    st.markdown(
        """<style>
            /* Target all text elements in the radio component */
            div[data-testid="stHorizontalRadio"] label, 
            div[data-testid="stHorizontalRadio"] p,
            div[data-testid="stHorizontalRadio"] span,
            .stRadio label p,
            div[role="radiogroup"] p,
            div[role="radiogroup"] label p {
                color: white !important;
            }
            
            /* Target specifically the text within radio buttons */
            .stRadio div:has(input[type="radio"]) p {
                color: white !important;
            }
            
            /* Override any Streamlit default styling */
            #view_selector p {
                color: white !important;
            }
            
            /* Target the "Select View:" label specifically */
            .stRadio > label, 
            .stRadio > div > label,
            .stRadio h4,
            .stRadio label h4,
            div.stRadio label:first-child,
            .stRadio > div:first-child > label {
                color: white !important;
            }
        </style>""",
        unsafe_allow_html=True
    )

    if selected_option == "Technical Stack":
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### Technical Stack")

        st.markdown("#### AI & Machine Learning")
        st.markdown("""
        <span class='skill-tag'>Azure ML</span>
        <span class='skill-tag'>Scikit-learn</span>
        <span class='skill-tag'>TensorFlow</span>
        <span class='skill-tag'>Large Language Modelling</span>
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
        <span class='skill-tag'>Yellowbricks</span>
        """, unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    elif selected_option == "Core Competencies":
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### Core Competencies")

        # Define categories and values for Data Science/Engineering skills
        categories = ['Machine Learning', 'SQL & Databases',
                      'Data Visualization', 'Cloud Platforms', 'Data Engineering',
                      'Statistical Analysis', 'Business Intelligence', 'Cross-functional Collaboration']
        values = [83, 77, 85, 70, 72, 83, 85, 90]

        values += [values[0]]
        categories += [categories[0]]

        fig = go.Figure()

        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            line_color='#4361EE',
            fillcolor='rgba(67, 97, 238, 0.4)',
            line=dict(width=3),
            marker=dict(size=12, color='white', symbol='circle', line=dict(color='#4361EE', width=2)),
            hoverinfo='text',
            text=[f"{c}: {v}%" for c, v in zip(categories, values)]
        ))

        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100],
                    tickfont=dict(size=14, color='white'),
                    ticksuffix="%",
                    gridcolor='rgba(255,255,255,0.3)',
                    tickvals=[0, 20, 40, 60, 80, 100]
                ),
                angularaxis=dict(
                    tickfont=dict(size=15, color='white', family='Arial, sans-serif'),
                    rotation=90,
                    direction="clockwise",
                    gridcolor='rgba(255,255,255,0.2)',
                ),
                bgcolor='rgba(0,0,0,0)'
            ),
            showlegend=False,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            height=500
        )

        st.plotly_chart(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)


# Tab 2: WebApp Projects
with tabs[1]:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### WebApp Projects")

    # Sample Streamlit apps
    apps = [
        {"title": "Amortization Calculator App", "description": "A portfolio showcasing data science projects and skills.", "link": "https://asheshrajgnawali-amortization-calculator-app.streamlit.app/"}
    ]

    for app in apps:
        st.markdown(f"<a href='{app['link']}' style='text-decoration:none; color: inherit;'><div class='card' style='margin-bottom: 20px;'><h3>{app['title']}</h3><p>{app['description']}</p></div></a>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# Tab 3: Publications
with tabs[2]:
    st.markdown("<div class='section-bar'><h3>Publications</h3></div>", unsafe_allow_html=True)
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    # publication entries
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

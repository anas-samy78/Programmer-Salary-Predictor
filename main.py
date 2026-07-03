import streamlit as st
import os
import pickle
import pandas as pd

# =========================================================
# PATHS & MODEL LOADING
# =========================================================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "Employee_Salary_Prediction.pkl")
image_path = os.path.join(BASE_DIR, "salary.png")

df = pickle.load(open(model_path, "rb"))

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Programmer Salary Predictor",
    page_icon="💸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# CUSTOM CSS
# =========================================================
st.markdown("""
    <style>
        .main {
            background-color: #0e1117;
        }
        .stApp {
            background: linear-gradient(180deg, #0e1117 0%, #10141c 100%);
        }

        header[data-testid="stHeader"] {
            background-color: #0e1117;
            border-bottom: 1px solid #262c36;
        }
        [data-testid="stToolbar"] {
            background-color: transparent;
        }
        [data-testid="stDecoration"] {
            background: linear-gradient(90deg, #00c6ff, #0072ff);
        }

        .title-container {
            text-align: center;
            padding: 1.2rem 0 0.3rem 0;
        }
        .title-container h1 {
            font-size: 2.6rem;
            font-weight: 800;
            background: linear-gradient(90deg, #00c6ff, #0072ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0;
        }
        .subtitle {
            text-align: center;
            color: #b7c0cc;
            font-size: 1.05rem;
            margin-top: -0.3rem;
            margin-bottom: 1.5rem;
        }
        .section-card {
            background-color: #161b22;
            padding: 1.5rem 1.5rem 1rem 1.5rem;
            border-radius: 16px;
            border: 1px solid #262c36;
            margin-bottom: 1.2rem;
        }
        .section-title {
            font-size: 1.15rem;
            font-weight: 700;
            color: #00c6ff;
            margin-bottom: 0.8rem;
        }

        h1, h2, h3, h4, h5, h6, p, label, .stMarkdown, span {
            color: #e6e9ef;
        }
        [data-testid="stSidebar"] {
            background-color: #10141c;
            border-right: 1px solid #262c36;
        }
        [data-testid="stSidebar"] * {
            color: #d3d9e2 !important;
        }
        [data-testid="stCaptionContainer"] {
            color: #8a94a3 !important;
        }
        .stSelectbox label, .stNumberInput label {
            color: #cdd4de !important;
            font-weight: 600;
        }

        div[data-baseweb="select"] > div {
            background-color: #0e1117;
            border: 1px solid #2c333f;
            color: #e6e9ef;
        }

        div[data-testid="stNumberInput"] input {
            background-color: #0e1117;
            color: #e6e9ef;
            border: 1px solid #2c333f;
            border-radius: 8px;
        }
        div[data-testid="stNumberInput"] input:focus {
            border: 1px solid #00c6ff;
            box-shadow: 0 0 0 1px #00c6ff55;
        }
        div[data-testid="stNumberInput"] button {
            background-color: #161b22;
            border: 1px solid #2c333f;
            color: #e6e9ef;
        }
        div[data-testid="stNumberInput"] button:hover {
            background-color: #1e2530;
            color: #00c6ff;
        }

        div.stButton > button {
            width: 100%;
            background: linear-gradient(90deg, #00c6ff, #0072ff);
            color: white;
            font-weight: 700;
            font-size: 1.05rem;
            padding: 0.7rem 0;
            border-radius: 12px;
            border: none;
            transition: 0.25s ease;
        }
        div.stButton > button:hover {
            transform: scale(1.015);
            box-shadow: 0 6px 20px rgba(0, 114, 255, 0.35);
        }
        .result-card {
            background: linear-gradient(135deg, #0072ff33, #00c6ff1a);
            border: 1px solid #0072ff55;
            padding: 2rem;
            border-radius: 18px;
            text-align: center;
            margin-top: 1.5rem;
        }
        .result-card h2 {
            color: #b7c0cc;
            font-size: 1.1rem;
            font-weight: 500;
            margin-bottom: 0.3rem;
        }
        .result-card h1 {
            font-size: 3rem;
            font-weight: 800;
            background: linear-gradient(90deg, #00c6ff, #00ffb2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin: 0;
        }
    </style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================
st.markdown('<div class="title-container"><h1>Programmer Salary Predictor</h1></div>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Estimate a tech professional\'s expected salary using AI</p>', unsafe_allow_html=True)

col_img1, col_img2, col_img3 = st.columns([1, 2, 1])
with col_img2:
    st.image(image_path, use_container_width=True)

st.write("")

# =========================================================
# ENCODING DATA  (logic untouched)
# =========================================================
job_title = ['AI Engineer', 'Data Analyst', 'Frontend Developer', 'Business Analyst', 'Product Manager', 'Backend Developer', 'Machine Learning Engineer', 'DevOps Engineer', 'Software Engineer', 'Cybersecurity Analyst', 'Data Scientist', 'Cloud Engineer']
education_level = ['Bachelor', 'PhD', 'High School', 'Diploma', 'Master']
industry = ['Healthcare', 'Telecom', 'Media', 'Retail', 'Manufacturing', 'Education', 'Finance', 'Technology', 'Consulting', 'Government']
company_size = ['Medium', 'Small', 'Large', 'Enterprise', 'Startup']
location = ['India', 'Australia', 'Singapore', 'Canada', 'Sweden', 'USA', 'Netherlands', 'Germany', 'UK', 'Other']
remote_work = ['Hybrid', 'No', 'Yes']

job_title_codes = [0, 5, 8, 2, 10, 1, 9, 7, 11, 4, 6, 3]
education_level_codes = [0, 4, 2, 1, 3]
industry_codes = [4, 9, 6, 7, 5, 1, 2, 8, 0, 3]
company_size_codes = [2, 3, 1, 0, 4]
location_codes = [3, 0, 6, 1, 7, 9, 4, 2, 8, 5]
remote_work_codes = [0, 1, 2]

finally_job_title = dict(zip(job_title, job_title_codes))
finally_education_level = dict(zip(education_level, education_level_codes))
finally_industry = dict(zip(industry, industry_codes))
finally_company_size = dict(zip(company_size, company_size_codes))
finally_location = dict(zip(location, location_codes))
finally_remote_work = dict(zip(remote_work, remote_work_codes))

# =========================================================
# SIDEBAR — ABOUT SECTION
# =========================================================
with st.sidebar:
    st.markdown("### About")
    st.write(
        "This app uses a trained Machine Learning model "
        "to predict the expected salary of a tech professional "
        "based on their profile."
    )
    st.markdown("---")
    st.markdown("### Powered by")
    st.write("XGBoost • Streamlit • Pandas")
    st.markdown("---")
    st.caption("Fill in your details and click **Predict** to see your estimated salary.")

# =========================================================
# INPUT FORM
# =========================================================
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Professional Profile</div>', unsafe_allow_html=True)
    model_job_title = st.selectbox("Job Title", job_title)
    model_education_level = st.selectbox("Education Level", education_level)
    model_industry = st.selectbox("Industry", industry)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Company Details</div>', unsafe_allow_html=True)
    model_company_size = st.selectbox("Company Size", company_size)
    model_location = st.selectbox("Location", location)
    model_remote_work = st.selectbox("Remote Work", remote_work)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Experience & Skills</div>', unsafe_allow_html=True)
col3, col4, col5 = st.columns(3)
with col3:
    experience_years = st.number_input("EXPERIENCE YEARS", min_value=0, max_value=50, step=1)
with col4:
    skills_count = st.number_input("SKILLS COUNT", min_value=0, max_value=100, step=1)
with col5:
    certifications = st.number_input("CERTIFICATIONS", min_value=0, max_value=50, step=1)
st.markdown('</div>', unsafe_allow_html=True)

# =========================================================
# ENCODING SELECTED VALUES  (logic untouched)
# =========================================================
job = finally_job_title[model_job_title]
education = finally_education_level[model_education_level]
industry_val = finally_industry[model_industry]
company = finally_company_size[model_company_size]
location_val = finally_location[model_location]
remote = finally_remote_work[model_remote_work]

per_salary = pd.DataFrame({
    "job_title": [job],
    "education_level": [education],
    "industry": [industry_val],
    "company_size": [company],
    "location": [location_val],
    "remote_work": [remote],
    "experience_years": [experience_years],
    "skills_count": [skills_count],
    "certifications": [certifications]
})

# =========================================================
# PREDICTION
# =========================================================
st.write("")
button = st.button("Click to Predict the Salary")

if button:
    with st.spinner("Analyzing profile and calculating salary..."):
        salary = df.predict(per_salary)

    st.markdown(f"""
        <div class="result-card">
            <h2>Estimated Annual Salary</h2>
            <h1>${salary[0]:,.2f}</h1>
        </div>
    """, unsafe_allow_html=True)

    st.balloons()
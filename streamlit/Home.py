import streamlit as st
import os
import sys
from datetime import datetime

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

st.set_page_config(
    page_title='Uber Eats Decision Support System',
    page_icon='🍽️',
    layout='wide'
)

with st.sidebar:
    st.title("🍽️ Uber Eats DSS")
    st.markdown("---")
    st.write("Restaurant Intelligence")

st.title('🍽 Uber Eats Restaurant Intelligence & Decision Support System')

st.markdown('---')

st.header('Project Overview')

st.write("""
This application helps business users analyze Uber Eats Bangalore restaurant and order data.

### Features

- 📊 Dashboard with Dynamic SQL Filters
- 🍽️ Restaurant Business Q&A
- 📦 Orders Business Q&A
- 💾 SQLite Database
- 🐍 Python + Pandas + SQL + Streamlit

""")

st.info('👈 Use the left sidebar to navigate between pages.')

st.markdown("---")

st.markdown(
    "<div style='padding-bottom:60px;'></div>",
    unsafe_allow_html=True
)

st.markdown(f"""
<style>
.footer{{
position:relavtive;
bottom:0;
left:0;
width:100%;
background:#262730;
padding:12px;
text-align:center;
color:white;
border-top:1px solid #4F8BF9;
font-size:14px;
}}
</style>

<div class="footer">
🍽️ Uber Eats Restaurant Intelligence & Decision Support System
<br>
© {datetime.now().year} | Developed by <b>Parthiban Sivanesan</b>
</div>
""", unsafe_allow_html=True)
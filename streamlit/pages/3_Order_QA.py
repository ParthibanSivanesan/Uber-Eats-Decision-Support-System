import os
import sys
import streamlit as st
from datetime import datetime

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(project_root)

from scripts.sql_queries import *

st.set_page_config(
    page_title="Orders Business Questions",
    page_icon="📦",
    layout="wide"
)

with st.sidebar:
    st.title("🍽️ Uber Eats DSS")
    st.markdown("---")
    st.write("Restaurant Intelligence")

st.title("📦 Orders Business Questions")

questions = {
    "A1 - Total Revenue": total_revenue,
    "A2 - Restaurants by Revenue": restaurants_by_revenue,
    "A3 - Most Used Payment Method": most_used_payment_method,
    "A4 - Discount vs Average Order Value": discount_vs_average_order_value,
    "A5 - Highest Revenue Month": highest_revenue_month,
    "A6 - Revenue by Location": revenue_by_location,
    "A7 - Revenue by Cuisine": revenue_by_cuisine,
    "A8 - Revenue by Price Category": revenue_by_price_category,
    "A9 - Rating vs Order Count": rating_vs_order_count,
    "A10 - Average Order Value by Location": average_order_value_by_location,
    "A11 - Top 5 Restaurants by Revenue": top_5_restaurants_by_revenue,
    "A12 - Highest Revenue Premium Restaurants": highest_revenue_premium_restaurants
}

selected_question = st.selectbox(
    "Select an Order Business Question",
    list(questions.keys())
)

with st.expander("Business Question"):
    st.write(selected_question)

if st.button("Run Query", use_container_width=True):

    df = questions[selected_question]()

    st.success("Query executed successfully!")

    st.info(f"Returned {len(df)} records.")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "📥 Download Results",
        csv,
        "query_results.csv",
        "text/csv"
    )

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
import os
import sys
import streamlit as st
from datetime import datetime

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(project_root)

from scripts.sql_queries import *

st.set_page_config(
    page_title="Restaurant Q&A",
    page_icon="🍽️",
    layout="wide"
)

with st.sidebar:
    st.title("🍽️ Uber Eats DSS")
    st.markdown("---")
    st.write("Restaurant Intelligence")

st.title("🍽️ Restaurant Business Questions")

questions = {
    "Q1 - Highest Rated Locations": highest_rated_locations,
    "Q2 - Oversaturated Locations": oversaturated_locations,
    "Q3 - Online Ordering Correlation": onlin_ordering_correlation,
    "Q4 - Table Booking Correlation": table_booking_correlation,
    "Q5 - Price Range Performance": price_range_performance,
    "Q6 - Pricing Segment Performance": pricing_segment_performance,
    "Q7 - Common Cuisines": common_cuisines,
    "Q8 - Highest Rated Cuisines": highest_rated_cuisines,
    "Q9 - Best Performing Cuisines": best_performing_cuisines,
    "Q10 - Cost vs Rating": cost_rating_relationship,
    "Q11 - Premium Locations": ideal_locations_for_premium,
    "Q12 - High Demand Low Rating": high_demand_low_rating,
    "Q13 - Online Order + Table Booking": online_order_table_booking,
    "Q14 - Success Factors": success_factors,
    "Q15 - Top Restaurants by Pricing": top_restaurants_by_pricing_segment
}

selected_question = st.selectbox(
    "Select a Business Question",
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
import streamlit as st
import os
import sys
from datetime import datetime

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(project_root)

from scripts.dashboard_queries import (
    get_locations,
    get_cuisines,
    get_price_categories,
    get_online_order_options,
    get_book_table_options,
    filter_restaurants
)

st.set_page_config(
    page_title='Dashboard',
    page_icon='📊',
    layout='wide'
)

with st.sidebar:
    st.title("🍽️ Uber Eats DSS")
    st.markdown("---")
    st.write("Restaurant Intelligence")

st.title('📊 Uber Eats Dashboard')

st.markdown('### Dynamic Restaurant Search')

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    locations = st.multiselect(
        "Location",
        get_locations()
    )

    cuisines = st.multiselect(
        "Cuisine",
        get_cuisines()
    )

with col2:
    price = st.multiselect(
        "Price Category",
        get_price_categories()
    )

    online = st.multiselect(
        "Online Order",
        get_online_order_options()
    )

with col3:
    booking = st.multiselect(
        "Book Table",
        get_book_table_options()
    )

    rating = st.slider(
        "Minimum Rating",
        0.0,
        5.0,
        3.5,
        0.1
    )

st.divider()


submit = st.button(
    '🔍 Apply Filters',
    use_container_width=True
)

st.divider()

st.subheader('Filtered Restaurants')

if submit:

    df = filter_restaurants(
        locations,
        cuisines,
        price,
        online,
        booking,
        rating
    )

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
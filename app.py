import streamlit as st
from st_pages import Page, add_page_title, show_pages

st.sidebar.image('petjoy1.png',caption="Jalan Boulevar Raya Barat Blok RGA No.61, RT.001/RW.002, Jaka Setia, Kec. Bekasi Sel., Kota Bks, Jawa Barat 17147",use_column_width=True)

show_pages(
    [
        Page("home.py", "Home", "🏠"),
        Page("pg1.py", "Monitoring Dispenser", ":books:"),
        Page("pg2.py", "Monitoring Berat Makanan", "📖"),
        Page("pg3.py", "Automations", "✏️"),
    ]
)

add_page_title() 
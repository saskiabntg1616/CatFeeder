import streamlit as st
from deta import Deta
import requests 
import json
import time
from PIL import Image
from st_pages import add_page_title

add_page_title(layout="wide")

hide_st_style = """
<style>
footer {visibility: hidden;}
[data-testid="column"] {
    border: 1px solid #CCCCCC;
    padding: 5% 5% 5% 3%;
    border-radius: 5px;
    
    border-left: 0.5rem solid #9AD8E1 !important;
    box-shadow: 0 0.15rem 1.75rem 0 rgba(58, 59, 69, 0.15) !important;
    }
[data-testid="stMarkdownContainer"]{
    font-weight: 700 !important;
    text-transform: uppercase !important;
}
</style>
"""

st.sidebar.image('petjoy1.png',caption="Jalan Boulevar Raya Barat Blok RGA No.61, RT.001/RW.002, Jaka Setia, Kec. Bekasi Sel., Kota Bks, Jawa Barat 17147",use_column_width=True)

st.markdown(hide_st_style,unsafe_allow_html=True)

def load(data):
    res = requests.get(f'https://blynk.cloud/external/api/get?token=0hS-1b3fyoWDNwK-4LULXeIj1o3-00ro&{data}')
    return res.text

def app():

    st.divider()

    image = Image.open('interface.png')
    st.image(image, caption='Interface pada Blynk by Saskia Bintang Maharani', use_column_width=False)
    st.write(""
             "")

    st.write("**Hasil Yang Diperoleh Untuk :blue[Mendapatkan Nilai Volume Pada Dispenser] Adalah Sebagai Berikut:**")
    placeholder = st.empty()
    st.write(""
             "")
    st.write("**Berikut merupakan :red[alur] yang digunakan untuk mendapatkan hasil diatas:**")

    image = Image.open('ultrasonik.png')
    st.image(image, caption='Flowchart Penggunaan Sensor Load Cell by Saskia Bintang Maharani', use_column_width=False)
    st.write(""
             "")
    st.markdown('<div style="text-align:justify">validasi dibuat agar petugas dapat memonitoring berat makanan pada wadah dengan menggunakan aplikasi Blynk IoT dengan validasi apabila berat kurang dari 20 gram maka Blynk akan memunculkan notifikasi berupa tulisan dan buzzer akan berbunyi sehingga saat notifikasi ditekan dan petugas memilih show device petugas dapat memantau berat dan disaat berat makanan yang tertera terpantau akan habis pada wadahnya maka servo akan membuka kenop hingga berat mencapai 20 gram.</div>', unsafe_allow_html=True)
    
    for seconds in range(200):

        with placeholder.container():

            st.metric("BERAT MAKANAN", load("V2")+" gr")

            time.sleep(1)

        st.write(""
                    "")
        
if __name__ == "__main__":
    app()


import streamlit as st
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

def app():

    st.divider()

    image = Image.open('automation.png')
    st.image(image, caption='Automation Cat Feeder by Saskia Bintang Maharani', use_column_width=False)
    st.write(""
                    "")

    st.markdown('<div style="text-align:justify">Automatic Cat Feeder berbasis IoT ini dibuat menggunakan Aplikasi Blynk dan dikoneksikan dengan WiFi yang berfungsi untuk melakukan pemberian makanan secara otomatis sesuai jadwal yang telah diatur sebelumnya oleh petugas. Dengan validasi tersebut petugas dapat memantau serta mengendalikan perangkat IoT melalui sistem antarmuka yang tertera pada Aplikasi Blynk.</div>', unsafe_allow_html=True)

    st.write(""
                "")

    image = Image.open('aluraut.png')
    st.image(image, caption='Automation Cat Feeder by Saskia Bintang Maharani', use_column_width=False)
    st.write(""
                    "")

    st.markdown('<div style="text-align:justify">Setelah petugas berhasil masuk ke aplikasi Blynk IoT maka selanjutnya petugas dapat menginput jadwal pemberian makan kucing sesuai dengan kebutuhannya pada menu automations. Apabila data yang dimasukkan dapat dipastikan kebenarannya maka petugas bisa menyimpan data tersebut yang kemudian program akan berjalan sesuai perintah yang terlah diatur sebelumnya. </div>', unsafe_allow_html=True)
                
if __name__ == "__main__":
    app()

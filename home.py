import streamlit as st
from PIL import Image

st.sidebar.image('petjoy1.png',caption="Jalan Boulevar Raya Barat Blok RGA No.61, RT.001/RW.002, Jaka Setia, Kec. Bekasi Sel., Kota Bks, Jawa Barat 17147",use_column_width=True)

st.header("Rancang Bangun Sistem Automatic Cat Feeder Pada Tempat Penitipan Hewan Berbasis Internet of Things (IoT)")

g1, g2, g3 = st.columns([1,2,1])
with g1:
  st.write(" ")
with g3:
  st.write(" ")
with g2:
    image = Image.open('feeder.png')
    st.image(image, caption='Automatic Cat Feeder by Saskia Bintang Maharani', use_column_width=False)
    st.write(""
                    "")

st.markdown('<div style="text-align:justify">Perkembangan Internet of Things semakin marak digunakan dalam kehidupan sehari-hari.  masyarakat yang memiliki hewan peliharaan namun hewan tersebut tidak terawat dengan baik dikarenakan seringnya bepergian sehingga alternatif dari hal tersebut yaitu menitipkan hewan peliharaannya kepada tempat penitipan hewan. Hal itu tak luput dikarenakan mobilitas yang tinggi membuat masyarakat menyukai hal yang praktis. PETJOY Clinic and Petshop tidak ingin ketinggalan untuk meningkatkan citranya dengan upgrade untuk memperbaiki sistem penitipan hewan khususnya kucing sehingga pemberian makan dapat terjadwal dan sesuai dengan kebutuhan sehingga terhindar dari adanya komplain kembali oleh pemilik hewan karna penggunaan sistem konvensional yang dinilai masih kurang optimal. Untuk dapat merancang sistem Automatic Cat Feeder membutuhkan komponen hardware maupun software dalam pengimplementasiannya. Sistem ini dibuat dengan menggunakan mikrokontroler ESP32 dan akan menghasilkan pemberian makan otomatis berdasarkan penjadwalan menggunakan Blynk IoT, pemberian makanan baru sesuai keinginan kucing menggunakan Sensor PIR, pendeteksian dispenser tempat menyimpan makanan kucing menggunakan Sensor Ultrasonik sehingga memungkinkan untuk memberi tahu petugas apabila makanan pada dispenser akan segera habis, dan juga pengukuran berat makanan kucing menggunakan Sensor Loadcell pada wadahnya.</div>', unsafe_allow_html=True)
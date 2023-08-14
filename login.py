import streamlit as st
import numpy as np
from deta import Deta
import streamlit_authenticator as stauth
import requests 
import time
from st_pages import Page, add_page_title, show_pages

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
deta = Deta(st.secrets["db_key"])
db = deta.Base("users")

st.markdown(hide_st_style,unsafe_allow_html=True)

#st.sidebar.image("asset/petjoy.png",caption="Cat Feeder",use_column_width=True)

def insert_user(username,name,password):
    try:
        db.put({"key": username, "name": name, "password": password})
        return st.success("Berhasil Registrasi")
    except:
        return st.warning("Username Telah Digunakan") 

def fetch_all_users():
    res = db.fetch()
    return res.items

def get_user(username):
    return db.get(username)

  
def load(data):
    res = requests.get(f'https://blynk.cloud/external/api/get?token=0hS-1b3fyoWDNwK-4LULXeIj1o3-00ro&{data}')
    return res.text


def app():
    users = fetch_all_users()
    usernames = [user["key"] for user in users]
    names = [users["name"] for users in users]
    passwords = [user["password"] for user in users]

    credentials = {"usernames":{}}

    for un, name, pw in zip(usernames, names, passwords):
        user_dict = {"name":name,"password":pw}
        credentials["usernames"].update({un:user_dict})

    authenticator = stauth.Authenticate(credentials, "app_home", "auth", cookie_expiry_days=30)
    name_user, authenticator_status, username = authenticator.login("Login", "main")

    if authenticator_status == False:
        st.error("Username atau Password Salah")

    if authenticator_status == None:
         st.warning("Please Input Your Username or Password Correctly")

    if authenticator_status == True:           

        show_pages(
            [
                Page("app.py"),
            ]
        )

add_page_title()

if __name__ == "__main__":
    app()
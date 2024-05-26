import streamlit as st
from streamlit_lottie import st_lottie
import requests
import base64
import json
import time
#python -m pipreqs.pipreqs

def autoplay(AudioFile):  #Autoplay audio
    with open(f"{AudioFile}.mp3", "rb") as f:
            media_bytes = f.read()
            encoded_media = base64.b64encode(media_bytes).decode()

    html_string = f"""
        <audio id="myAudio" src="data:audio/mp3;base64,{encoded_media}" autoplay></audio>
        <script>
        document.getElementById('myAudio').controls = false;
        </script>
        """

    st.components.v1.html(html_string)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.set_page_config(page_title = "Rafiq", page_icon = ":robot_face:")

def page_1():
    with st.container():
        lottie_coding = load_lottieurl("https://lottie.host/61c87b55-4ec6-44a4-bcf0-b5b04290b5ea/Qel5MP9yiV.json")
        st_lottie(lottie_coding)

        begin = st.button("Begin", use_container_width=True)

        if begin:
            st.session_state["current_page"] = "page2"
            st.rerun()

def page_2():
    with st.container():

        st.image("1.jpg")
        
        st.markdown("""<center> Welcome <br> How can i help you? </center>""", True)

        login = st.button("Login", use_container_width=True)

        if login:
            st.session_state["current_page"] = "page3"
            st.rerun()
        
        autoplay(1)

def page_3():
    with st.container():
        st.image("2.jpg")

        n = 0 #Regarding audio play

        code = st.text_input("Sign In", max_chars = 4, placeholder = "Enter your code")
        proceed = st.button("Confirm", use_container_width=True)

        if proceed:
            
            if code == "0000":
                st.session_state["current_page"] = "page4"
                st.rerun()
            else:
                st.markdown("<p style='text-align: center; color: red;'>Invalid code. Please try again.</p>", unsafe_allow_html=True)
                autoplay(4)
                n += 1
        
        if n == 0:
            autoplay(2)

def page_4():
    with st.container():
        st.image("3.jpg")

        st.markdown("""<center> Please choose a room </center>""", True)

        row1, row2 = st.columns(2)

        with row1:
            R101 = st.button("R101", use_container_width = True)
            R102 = st.button("R102", use_container_width = True)
            R103 = st.button("R103", use_container_width = True)
            R104 = st.button("R104", use_container_width = True)
        with row2:
            R105 = st.button("R105", use_container_width = True)
            R106 = st.button("R106", use_container_width = True)
            R107 = st.button("R107", use_container_width = True)
            R108 = st.button("R108", use_container_width = True)
        
        if R101:
            st.session_state["current_page"] = "page5"
            print("R101")
            st.rerun()
        elif R102:
            st.session_state["current_page"] = "page5"
            print("R102")
            st.rerun()
        elif R103:
            st.session_state["current_page"] = "page5"
            print("R103")
            st.rerun()
        elif R104:
            st.session_state["current_page"] = "page5"
            print("R104")
            st.rerun()
        elif R105:
            st.session_state["current_page"] = "page5"
            print("R105")
            st.rerun()
        elif R106:
            st.session_state["current_page"] = "page5"
            print("R106")
            st.rerun()
        elif R107:
            st.session_state["current_page"] = "page5"
            print("R107")
            st.rerun()
        elif R108:
            st.session_state["current_page"] = "page5"
            print("R108")
            st.rerun()

        autoplay(3)

def page_5():
    with st.container():
        st.image("4.jpg")

        st.markdown("""<center> Please confirm your order </center>""", True)

        confirm = st.button("Confirm", use_container_width=True)
        discrad = st.button("Discrad", use_container_width=True)

        if confirm:
            st.session_state["current_page"] = "page6"
            st.rerun()
        elif discrad:
            st.session_state["current_page"] = "page4"
            st.rerun()

        autoplay(5)

def page_6():
    with st.container():
        st.image("5.jpg")

        st.markdown("""<center> Order confirmed </center>""", True)

        order_again = st.button("Order again", use_container_width=True)

        if order_again:
            st.session_state["current_page"] = "page4"
            st.rerun()

        autoplay(6)

current_page = st.session_state.get("current_page", "page1")

if current_page == "page1":
    page_1()
elif current_page == "page2":
    page_2()
elif current_page == "page3":
    page_3()
elif current_page == "page4":
    page_4()
elif current_page == "page5":
    page_5()
elif current_page == "page6":
    page_6()
else:
    st.error("Invalid page!")

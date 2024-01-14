import streamlit as st

st.header(":mailbox: Comments")

form = """

<form  action="https://formsubmit.io/e_trejoh@yahoo.com.mx" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input name="name" type="text" id="name" placeholder = "Your Name" required>
    <input name="email" type="email" placeholder = "Your email" id="email" required>
    <textarea name="comment" id="comment" rows="3" placeholder = "Leave a comment" required></textarea>    
    <button type="submit">Send </button>
</form>

"""
#<input name="_formsubmit_id" type="text" style="display:none">
#<input value="Submit" type="submit">
st.markdown(form, unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style", unsafe_allow_html=True)

local_css("style/style.css")
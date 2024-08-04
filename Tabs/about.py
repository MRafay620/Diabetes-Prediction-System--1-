"""This modules contains data about about page"""

# Import necessary modules
import streamlit as st
from PIL import Image


def app():
    """This function creates the about page"""
    st.balloons()
    st.title('Contact Us')
    st.markdown('''### Name: MUhammad Rafay''')
    st.markdown('''      ''')
    st.image('./images/icon.jpg')
    st.markdown('''### Linkedin: [Mainak](https://www.linkedin.com)''')
    st.markdown('''### GitHub: [Mainak](https://github.com/)''')
    
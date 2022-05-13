"""Machine Eyes Streamlit Application"""

from mimetypes import init
import streamlit as st

from aws import aws_detect_text
from azure_vision import acvs_detect_text
from goog import gcp_detect_text

st.title("Machine Eyes")

def drop_file_or_url():
    inital_page = st.empty()
    with inital_page.container():
        header_text = """<h3 style="color:#fe644e">Drop in a handwritten text pdf, jpg, png, or IIIF</h3>"""
        st.markdown(header_text, unsafe_allow_html=True)

        all_col, goog_col, ms_col, amz_col = st.columns(4)

        with all_col:
            all_services = st.checkbox("All", key="all-services")

        with goog_col:
            google = st.checkbox("Google", key="google", value=all_services)

        with ms_col:
            microsoft = st.checkbox("Microsoft", key="microsoft", value=all_services)

        with amz_col:
            amazon = st.checkbox("Amazon", key="amazon", value=all_services)

        uploaded_file = st.file_uploader("", type=["pdf", "png", "jpg"])

        url = st.text_input("Image or IIIF URL")

    if uploaded_file is not None:
        image_bytes= uploaded_file.getvalue()
        st.session_state["source"] = image_bytes
        st.session_state["goog"] = google
        st.session_state["ms"] = microsoft
        st.session_state["aws"] = amazon
        inital_page.empty()
        show_results(image_bytes)

def show_results(image_bytes):

    if not any([st.session_state["goog"], st.session_state["ms"], st.session_state["aws"]]):
        st.header("No services selected")
    
    if st.session_state["goog"] is True:
        gcp_detect_text(image_bytes)

    if st.session_state["ms"] is True:
        acvs_detect_text(image_bytes)

    if st.session_state["aws"] is True:
        aws_detect_text(image_bytes)


drop_file_or_url()

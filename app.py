"""Machine Eyes Streamlit Application"""

from mimetypes import init
import streamlit as st
from goog import detect_text

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
    
    if st.session_state["goog"] is True:
        detect_text(image_bytes)


    if st.session_state["ms"] is True:
        st.header("Microsoft")
        st.download_button(
            label="Download transcipt",
            data='''Microsoft Transcript'''
        )

    if st.session_state["aws"] is True:
        st.header("Amazon")
        st.download_button(
            label="Download transcipt",
            data='''Amazon Transcript'''
        )

# if st.session_state.get("source"):
#     image_bytes = st.session_state.pop("source")
#     show_results(image_bytes)
    
# else:
drop_file_or_url()
    # st.session_state["source"] = None

"""Machine Eyes Streamlit Application"""

import streamlit as st

st.title("Machine Eyes")

def drop_file_or_url():
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

    if uploaded_file:
        st.session_state["source"] = uploaded_file

def show_results():
    st.header("Google")
    st.download_button(
        label="Download transcipt",
        data='''Google Transcript'''
    )

    st.header("Microsoft")
    st.download_button(
        label="Download transcipt",
        data='''Microsoft Transcript'''
    )

    st.header("Amazon")
    st.download_button(
        label="Download transcipt",
        data='''Amazon Transcript'''
    )

if "source" in st.session_state:
    show_results()
    # st.session_state.pop("source")
else:
    drop_file_or_url()
    # st.session_state["source"] = "test"

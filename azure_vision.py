# Starting https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/quickstarts-sdk/client-library?tabs=visual-studio&pivots=programming-language-python
import io
import os
import time
from PIL import Image, ImageDraw

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

import streamlit as st

subscription_key = os.environ["AZURE_COMPUTER_VISION_KEY"]
endpoint = os.environ["AZURE_COMPUTER_VISION_ENDPOINT"]

def _generate_annotated_image(content, read_results):
    image_stream = io.BytesIO(content)
    image = Image.open(image_stream)

    for text_result in read_results:
        for line in text_result.lines:
            draw = ImageDraw.Draw(image)
            box = line.bounding_box            
            rect = [
                box[0],  # left
                box[1],  # top
                box[4],  # bottom
                box[-1]  # right
            ]
            draw.rectangle(rect, outline='red')

    return image


def acvs_detect_text(content):
    header_text = """<h3 style="font-family: Monaco">Microsoft</h3>"""
    st.markdown(header_text, unsafe_allow_html=True)

    client = ComputerVisionClient(
        endpoint,
        CognitiveServicesCredentials(subscription_key)
    )

    image_stream = io.BytesIO(content)

    
    read_response = client.read_in_stream(image_stream, raw=True)
    read_op_location = read_response.headers["Operation-Location"]
    op_id = read_op_location.split("/")[-1]

    

    while True:
        read_result = client.get_read_result(op_id)
        if read_result.status.lower() not in ['notstarted', 'running']:
            break
        time.sleep(10)

    text = []
    for text_result in read_result.analyze_result.read_results:
        for line in text_result.lines:
            text.append(line.text)


    st.download_button(
        label="Download transcipt",
        data="\n".join(text),
        key="azure_download_transcript"
    )

    image_col, text_col = st.columns(2)

    annotated_image = _generate_annotated_image(
        content, 
        read_result.analyze_result.read_results
    )

    with image_col:
        st.image(annotated_image)

    with text_col:
        for row in text:
            st.write(row)

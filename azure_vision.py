# Starting https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/quickstarts-sdk/client-library?tabs=visual-studio&pivots=programming-language-python
import io
import os
import time
from PIL import Image

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

import streamlit as st

subscription_key = os.environ["AZURE_COMPUTER_VISION_KEY"]
endpoint = 'https://stanford.cognitiveservices.azure.com/'

def acvs_detect_text(content):
    st.header("Microsoft")

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
        data="\n".join(text)
    )

    image_col, text_col = st.columns(2)
    # image_stream = io.BytesIO(content)
    # pil_image = Image.open(image_stream)
    
    # image_result = client.generate_thumbnail_in_stream(
    #         600,
    #         1000,
    #         io.BytesIO(content),
    #         raw=True
    # )

    with image_col:
        st.image(content)

    with text_col:
        for row in text:
            st.write(row)

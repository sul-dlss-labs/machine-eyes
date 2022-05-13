# Starting https://docs.microsoft.com/en-us/azure/cognitive-services/computer-vision/quickstarts-sdk/client-library?tabs=visual-studio&pivots=programming-language-python
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

    read_response = client.read(content, raw=True)
    read_op_location = read_response.headers["Operation-Location"]
    op_id = read_op_location.split("/")[-1]

    while st.spinner("Waiting for result..."):
        read_result = computervision_client.get_read_result(operation_id)
        if read_result.status.lower() not in ['notstarted', 'running']:
            break
        time.sleep(10)


    st.download_button(
        label="Download transcipt",
        data='''Microsoft Transcript'''
    )



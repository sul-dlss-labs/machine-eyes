# Machine Eyes Application
A proof-of-concept [Streamlit](https://streamlit.io/) application that takes
uploaded or linked image files and performs handwriting OCR using the following
commercial services:

- [Google Vision](https://cloud.google.com/vision/)
- [Microsoft Azure Computer Vision](https://azure.microsoft.com/en-us/services/cognitive-services/computer-vision/)
- [Amazon Textract](https://aws.amazon.com/textract/)


## Running
Set the following environmental variables for the various services:
- **GOOGLE_APPLICATION_CREDENTIALS** path to JSON file
- **AZURE_COMPUTER_VISION_KEY**
- **AZURE_COMPUTER_VISION_ENDPOINT**
- **AWS_ACCESS_KEY**
- **AWS_SECRET_ACCESS_KEY**

These values are set in an `.env` file. 

To run the application on port 80:
1. First change user to root
2. Populate environment variables by `source .env`
3. Activate the Python environment by `source py3-env/bin/activate`
4. Run streamlit in the background `streamlit run app.py --server.address="0.0.0.0" --server.port="80" &`.

To run the application on port 8150 with port-forwarding from Apache:
1. Populate environment variables by `source .env`
2. Activate the Python environment by `source py3-env/bin/activate`
3. Run streamlit in the background with CORS disabled: `run app.py --server.address="0.0.0.0" --server.enableCORS=false &`

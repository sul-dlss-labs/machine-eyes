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
- **AWS_ACCESS_KEY**
- **AWS_SECRET_ACCESS_KEY**

These values are set in an `.env` file. To run the application on port 80, first change to root, and then run the
following command `streamlit run app.py --server.address="0.0.0.0" --server.port="80" &`.

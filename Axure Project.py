import streamlit as st
from azure.ai.contentsafety import ContentSafetyClient
from azure.core.credentials import AzureKeyCredential
from azure.core.exceptions import HttpResponseError
from azure.ai.contentsafety.models import AnalyzeTextOptions, TextCategory

def analyze_text(input_text):
    # Azure Content Safety credentials
    key = '0731df2309f0424d91262cd005ba09a0'
    endpoint = 'https://cintent.cognitiveservices.azure.com/'

    # Create an Azure AI Content Safety client
    client = ContentSafetyClient(endpoint, AzureKeyCredential(key))

    # Construct request
    request = AnalyzeTextOptions(text=input_text)

    # Analyze text
    try:
        response = client.analyze_text(request)
    except HttpResponseError as e:
        st.error("Analyze text failed.")
        if e.error:
            st.error(f"Error code: {e.error.code}")
            st.error(f"Error message: {e.error.message}")
            raise
        st.error(e)
        raise

    return response

def main():
    st.title("Text Content Safety Analyzer")

    input_text = st.text_area("Enter your text here:")

    if st.button("Analyze"):
        if input_text:
            # Analyze text
            response = analyze_text(input_text)

            # Display results
            for category in response.categories_analysis:
                st.write(f"Category: {category.category}")
                st.write(f"Severity: {category.severity}")
        else:
            st.warning("Please enter some text to analyze.")

if __name__ == "__main__":
    main()

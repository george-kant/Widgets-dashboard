import streamlit as st
import requests
# Send a GET request to the API
response = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random")

st.title("🎈 Widgets App Dashboard")

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    fact = response.json()
    # Print the fact
    print(fact["text"])
else:
    st.write(f"Failed to retrieve fact. Status code: {response.status_code}")

st.write( " George ig For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/).")
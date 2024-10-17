import streamlit as st
import requests
import json
import http.client


# Send a GET request to the API
response = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random")

st.title("🎈 Widgets App Dashboard")

st.subheader("Random Useless Fact Generator")

# Button to get the random fact
if st.button("Get Random Fact"):
    response = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random")
    if response.status_code == 200:
        fact = response.json()["text"]
        st.write(f"Here's your random fact: {fact}")
    else:
        st.write(f"Failed to retrieve fact. Status code: {response.status_code}")


# API request to Weatherbit
# Button to trigger the API call
if st.button("Get Weather Forecast"):
    # Create HTTPS connection to Weatherbit API
    conn = http.client.HTTPSConnection("weatherbit-v1-mashape.p.rapidapi.com")

    # API request headers
    headers = {
        'x-rapidapi-key': "477b04cf19msh3b843b62fef3654p184910jsn8f3229ba512f",
        'x-rapidapi-host': "weatherbit-v1-mashape.p.rapidapi.com"
    }

    # Make the request with Limassol's latitude and longitude, using metric units
    conn.request("GET", "/forecast/3hourly?lat=34.68&lon=33.04&units=metric&lang=en", headers=headers)

    # Get the response from the API
    res = conn.getresponse()
    data = res.read()

    # Parse the response as JSON
    weather_data = json.loads(data)

    # Display the first forecast (next 3 hours)
    if "data" in weather_data and len(weather_data["data"]) > 0:
        forecast = weather_data["data"][0]  # Get the first forecast
        temp = forecast['temp']
        description = forecast['weather']['description']
        timestamp = forecast['timestamp_local']

        # Display the weather data
        st.write(f"Forecast for {timestamp}:")
        st.write(f"Temperature: {temp}°C")
        st.write(f"Description: {description}")
    else:
        st.write("No forecast data available.")


4.# Υπολογιστής ΔΜΣ
st.subheader("Υπολογιστής Δείκτη Μάζας Σώματος (ΔΜΣ)")
weight = st.number_input("Εισάγετε το βάρος σας σε κιλά:", min_value=0.0, step=0.1)
height = st.number_input("Εισάγετε το ύψος σας σε εκατοστά:", min_value=0.0, step=0.1)

if st.button("Υπολογισμός ΔΜΣ"):
    if weight > 0 and height > 0:
        height_m = height / 100  # Μετατροπή ύψους σε μέτρα
        bmi = weight / (height_m ** 2)  # Υπολογισμός ΔΜΣ
        st.write(f"Ο ΔΜΣ σας είναι: {bmi:.2f}")
        # Κατηγοριοποίηση του ΔΜΣ
        if bmi < 18.5:
            st.write("Είστε λιποβαρής.")
        elif bmi < 24.9:
            st.write("Έχετε φυσιολογικό βάρος.")
        elif bmi < 29.9:
            st.write("Είστε υπέρβαρος.")
        else:
            st.write("Έχετε παχυσαρκία.")
    else:
        st.write("Παρακαλώ εισάγετε έγκυρες τιμές για βάρος και ύψος.")

# 5. Υπολογιστής Καθημερινών Θερμίδων (BMR Calculator)
st.subheader("Υπολογιστής Καθημερινών Θερμίδων")
age = st.number_input("Εισάγετε την ηλικία σας:", min_value=0, step=1)
gender = st.selectbox("Επιλέξτε το φύλο σας:", ["Άνδρας", "Γυναίκα"])
activity_level = st.selectbox("Επίπεδο δραστηριότητας:", [
    "Καθιστική ζωή",
    "Ελαφριά δραστηριότητα",
    "Μέτρια δραστηριότητα",
    "Υψηλή δραστηριότητα",
    "Πολύ υψηλή δραστηριότητα"
])

if st.button("Υπολογισμός Θερμίδων"):
    if weight > 0 and height > 0 and age > 0:
        # Υπολογισμός BMR
        if gender == "Άνδρας":
            bmr = 10 * weight + 6.25 * height - 5 * age + 5
        else:
            bmr = 10 * weight + 6.25 * height - 5 * age - 161
        # Συντελεστής δραστηριότητας
        activity_factors = {
            "Καθιστική ζωή": 1.2,
            "Ελαφριά δραστηριότητα": 1.375,
            "Μέτρια δραστηριότητα": 1.55,
            "Υψηλή δραστηριότητα": 1.725,
            "Πολύ υψηλή δραστηριότητα": 1.9
        }
        total_calories = bmr * activity_factors[activity_level]
        st.write(f"Πρέπει να καταναλώνετε περίπου {total_calories:.2f} θερμίδες την ημέρα.")
    else:
        st.write("Παρακαλώ συμπληρώστε όλες τις τιμές.")
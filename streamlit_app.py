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
if st.button("Get Weather Forecast (Limassol)"):
    # API endpoint for Open Meteo
    url = "https://api.open-meteo.com/v1/forecast"
    
    # Parameters for Limassol, Cyprus
    params = {
        "latitude": 34.68,
        "longitude": 33.04,
        "hourly": "temperature_2m,weathercode",
        "timezone": "Europe/Athens"
    }
    
    # Make the request to the Open Meteo API
    response = requests.get(url, params=params)
    
    # Check if the response was successful
    if response.status_code == 200:
        # Parse the response JSON
        weather_data = response.json()
        
        # Get the first forecasted hour (next 3-hour data)
        if "hourly" in weather_data and "temperature_2m" in weather_data["hourly"]:
            temperatures = weather_data["hourly"]["temperature_2m"]
            weather_codes = weather_data["hourly"]["weathercode"]
            time_stamps = weather_data["hourly"]["time"]
            
            # Display the first forecast
            st.write(f"Forecast for {time_stamps[0]}:")
            st.write(f"Temperature: {temperatures[0]}°C")
            st.write(f"Weather Code: {weather_codes[0]}")
        else:
            st.write("No hourly forecast data available.")
    else:
        st.write(f"Failed to retrieve weather data. Status code: {response.status_code}")


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
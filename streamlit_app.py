import streamlit as st
import requests

# Full width layout
st.set_page_config(layout="wide")

# Main title
st.title("🎈 Widgets App Dashboard")

# Creating a grid with 3 columns per row
col1, col2, col3 = st.columns(3)

# Random Useless Fact Generator in col1
with col1:
    st.subheader("Random Useless Fact Generator")
    if st.button("Get Random Fact"):
        response = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random")
        if response.status_code == 200:
            fact = response.json()["text"]
            st.write(f"Here's your random fact: {fact}")
        else:
            st.write(f"Failed to retrieve fact. Status code: {response.status_code}")

# Weather Forecast in col2
with col2:
    st.subheader("Weather Forecast (Limassol)")
    if st.button("Get Weather Forecast (Limassol)"):
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": 34.68,
            "longitude": 33.04,
            "hourly": "temperature_2m,weathercode",
            "timezone": "Europe/Athens"
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            weather_data = response.json()
            temperatures = weather_data["hourly"]["temperature_2m"]
            time_stamps = weather_data["hourly"]["time"]
            st.write(f"Forecast for {time_stamps[0]}:")
            st.write(f"Temperature: {temperatures[0]}°C")
        else:
            st.write(f"Failed to retrieve weather data. Status code: {response.status_code}")

# BMI Calculator in col3
with col3:
    st.subheader("Υπολογιστής Δείκτη Μάζας Σώματος (ΔΜΣ)")
    weight = st.number_input("Εισάγετε το βάρος σας σε κιλά:", min_value=0.0, step=0.1)
    height = st.number_input("Εισάγετε το ύψος σας σε εκατοστά:", min_value=0.0, step=0.1)

    if st.button("Υπολογισμός ΔΜΣ"):
        if weight > 0 and height > 0:
            height_m = height / 100
            bmi = weight / (height_m ** 2)
            st.write(f"Ο ΔΜΣ σας είναι: {bmi:.2f}")
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

# New row for BMR Calculator
col4, col5, col6 = st.columns(3)

with col4:
    st.subheader("Generate a Keanu Reeves Placeholder Image")

    # User inputs for image dimensions
    width = st.number_input("Enter the width of the image:", min_value=1, value=300, step=1)
    height = st.number_input("Enter the height of the image:", min_value=1, value=300, step=1)

    # Dropdown for optional effects: 'y' for grayscale or 'g' for color
    option = st.selectbox("Choose image style:", ["g - Grayscale", "y - Young Colored"])

    # Button to generate the image
    if st.button("Generate Keanu Image"):
        # Determine option from selection
        option_code = option.split(" - ")[0]
        
        # Build the URL based on the inputs
        if option_code == "y":  # Grayscale option
            image_url = f"https://placekeanu.com/{width}/{height}/{option_code}"
        else:  # Color option
            image_url = f"https://placekeanu.com/{width}/{height}"
        
        # Display the image in Streamlit without using column width
        st.image(image_url, caption=f"Keanu Reeves ({width}x{height})", width=width)


# BMR Calculator in col5
with col5:
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
            if gender == "Άνδρας":
                bmr = 10 * weight + 6.25 * height - 5 * age + 5
            else:
                bmr = 10 * weight + 6.25 * height - 5 * age - 161
            
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



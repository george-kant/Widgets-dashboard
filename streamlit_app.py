import streamlit as st
import requests

# Set up the page layout with a sidebar
st.set_page_config(layout="wide")

# Sidebar with navigation tabs
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", [
    "Intro",
    "Random Useless Fact Generator",
    "Keanu Reeves Placeholder Image",
    "Weather Forecast (Limassol)",
    "Υπολογιστής ΔΜΣ (BMI)",
    "Υπολογιστής Μεταβολισμού (BMR)",
    "Υπολογισμός Ημερήσιων Θερμίδων (TDEE)"
])

# Tab 1: Intro Page
if page == "Intro":
    st.title("🎈 Welcome to the Widgets App Dashboard")
    st.write("Use the sidebar to navigate between different widgets!")

# Tab 2: Random Useless Fact Generator
if page == "Random Useless Fact Generator":
    st.subheader("Random Useless Fact Generator")
    if st.button("Get Random Fact"):
        response = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random")
        if response.status_code == 200:
            fact = response.json()["text"]
            st.write(f"Here's your random fact: {fact}")
        else:
            st.write(f"Failed to retrieve fact. Status code: {response.status_code}")

# Tab 3: Keanu Reeves Placeholder Image
if page == "Keanu Reeves Placeholder Image":
    st.subheader("Generate a Keanu Reeves Placeholder Image")

    # User inputs for image dimensions
    width = st.number_input("Enter the width of the image:", min_value=1, value=300, step=1, key="keanu_width")
    height = st.number_input("Enter the height of the image:", min_value=1, value=300, step=1, key="keanu_height")

    # Dropdown for optional effects: 'g' for grayscale or 'y' for young colored
    option = st.selectbox("Choose image style:", ["g - Grayscale", "y - Young Colored"], key="keanu_option")

    # Button to generate the image
    if st.button("Generate Keanu Image"):
        option_code = option.split(" - ")[0]
        image_url = f"https://placekeanu.com/{width}/{height}/{option_code}"
        st.image(image_url, caption=f"Keanu Reeves ({width}x{height})", width=width)

# Tab 4: Weather Forecast (Limassol)
if page == "Weather Forecast (Limassol)":
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

# Tab 5: Υπολογιστής ΔΜΣ (BMI)
if page == "Υπολογιστής ΔΜΣ (BMI)":
    st.subheader("Υπολογιστής Δείκτη Μάζας Σώματος (BMI)")
    weight_bmi = st.number_input("Εισάγετε το βάρος σας σε κιλά:", min_value=0.0, step=0.1, key="bmi_weight")
    height_bmi = st.number_input("Εισάγετε το ύψος σας σε εκατοστά:", min_value=0.0, step=0.1, key="bmi_height")

    if st.button("Υπολογισμός BMI"):
        if weight_bmi > 0 and height_bmi > 0:
            height_m_bmi = height_bmi / 100  # Μετατροπή ύψους σε μέτρα
            bmi = weight_bmi / (height_m_bmi ** 2)  # Υπολογισμός ΔΜΣ
            st.write(f"To BMI σας είναι: {bmi:.2f}")
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

# Tab 6: Υπολογιστής Μεταβολισμού (BMR)
if page == "Υπολογιστής Μεταβολισμού (BMR)":
    st.subheader("Υπολογιστής Μεταβολισμού (BMR)")
    weight_bmr = st.number_input("Εισάγετε το βάρος σας σε κιλά:", min_value=0.0, step=0.1, key="bmr_weight")
    height_bmr = st.number_input("Εισάγετε το ύψος σας σε εκατοστά:", min_value=0.0, step=0.1, key="bmr_height")
    age_bmr = st.slider("Εισάγετε την ηλικία σας:", 1, 100, key="bmr_age")
    gender_bmr = st.selectbox("Επιλέξτε το φύλο σας:", ["Άνδρας", "Γυναίκα"], key="bmr_gender")

    if st.button("Υπολογισμός BMR"):
        if weight_bmr > 0 and height_bmr > 0 and age_bmr > 0:
            if gender_bmr == "Άνδρας":
                bmr = 10 * weight_bmr + 6.25 * height_bmr - 5 * age_bmr + 5
            else:
                bmr = 10 * weight_bmr + 6.25 * height_bmr - 5 * age_bmr - 161
            st.write(f"H ενέργεια που καταναλώνει το σώμα σας σε ηρεμία: {bmr:.2f} θερμίδες.")
        else:
            st.write("Παρακαλώ εισάγετε έγκυρες τιμές.")

# Tab 7: Υπολογισμός Ημερήσιων Θερμίδων (TDEE)
if page == "Υπολογισμός Ημερήσιων Θερμίδων (TDEE)":
    st.subheader("Υπολογισμός Ημερήσιων Θερμίδων (TDEE)")
    weight_tdee = st.number_input("Εισάγετε το βάρος σας σε κιλά:", min_value=0.0, step=0.1, key="tdee_weight")
    height_tdee = st.number_input("Εισάγετε το ύψος σας σε εκατοστά:", min_value=0.0, step=0.1, key="tdee_height")
    age_tdee = st.slider("Εισάγετε την ηλικία σας:", 1, 100, key="tdee_age")
    gender_tdee = st.selectbox("Επιλέξτε το φύλο σας:", ["Άνδρας", "Γυναίκα"], key="tdee_gender")
    activity_level_tdee = st.selectbox("Επίπεδο δραστηριότητας:", [
        "Καθιστική ζωή",
        "Ελαφριά δραστηριότητα",
        "Μέτρια δραστηριότητα",
        "Υψηλή δραστηριότητα",
        "Πολύ υψηλή δραστηριότητα"
    ], key="tdee_activity")

    activity_factors = {
        "Καθιστική ζωή": 1.2,
        "Ελαφριά δραστηριότητα": 1.375,
        "Μέτρια δραστηριότητα": 1.55,
        "Υψηλή δραστηριότητα": 1.725,
        "Πολύ υψηλή δραστηριότητα": 1.9
    }

    if st.button("Υπολογισμός TDEE"):
        if weight_tdee > 0 and height_tdee > 0 and age_tdee > 0:
            if gender_tdee == "Άνδρας":
                bmr_tdee = 10 * weight_tdee + 6.25 * height_tdee - 5 * age_tdee + 5
            else:
                bmr_tdee = 10 * weight_tdee + 6.25 * height_tdee - 5 * age_tdee - 161
            total_calories = bmr_tdee * activity_factors[activity_level_tdee]
            st.write(f"Πρέπει να καταναλώνετε περίπου {total_calories:.2f} θερμίδες την ημέρα.")
        else:
            st.write("Παρακαλώ εισάγετε έγκυρες τιμές για βάρος, ύψος και ηλικία.")

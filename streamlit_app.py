import streamlit as st
import requests

# Send a GET request to the API
response = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random")

st.title("🎈 Widgets App Dashboard")

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    fact = response.json()
    st.write(fact["text"])
else:
    st.write(f"Failed to retrieve fact. Status code: {response.status_code}")

st.write( " George ig For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/).")


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
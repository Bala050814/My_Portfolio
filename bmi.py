import streamlit as st

st.title("BMI Calculator")
st.subheader("Body mass index (BMI) is a value derived from the mass (weight) and height of a person. The BMI is defined as the body mass divided by the square of the body height, and is expressed in units of kg/m², resulting from mass in kilograms (kg) and height in meters (m).")

weight = st.number_input("Enter Your Weight (in Kgs)", min_value=0.0)

status = st.radio("Select your Height Format:", ['cms', 'meters', 'Feet'])

# Initialize BMI variable
bmi = None

if status == "cms":
    height = st.number_input("Centimeters:", min_value=0.0)
    if height > 0:
        bmi = weight / ((height / 100) ** 2)

elif status == "meters":
    height = st.number_input("Meters:", min_value=0.0)
    if height > 0:
        bmi = weight / (height ** 2)

elif status == "Feet":
    height = st.number_input("Feet:", min_value=0.0)
    if height > 0:
        # Convert feet to meters (1 foot = 0.3048 meters)
        height_in_meters = height * 0.3048
        bmi = weight / (height_in_meters ** 2)

if st.button("Calculate BMI"):
    if bmi is not None:
        st.write("Your BMI is:", round(bmi, 2))
        if bmi < 16:
            st.error("You are extremely underweight")
        elif 16 <= bmi < 18.5:
            st.warning("You are underweight")
        elif 18.5 <= bmi < 25:
            st.success("You have a healthy weight")
        elif 25 <= bmi < 30:
            st.warning("You are overweight")
        else:
            st.error("You are extremely overweight")
    else:
        st.error("Please enter valid height and weight values.")



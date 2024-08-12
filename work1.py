import streamlit as st

def calculate_bmi(weight_kg, height_m):
    """Calculate BMI."""
    return weight_kg / (height_m ** 2)

def main():
    st.title("BMI Calculator")
    
    # Input weight in kilograms
    weight_kg = st.number_input("Enter your weight in kilograms:", min_value=0.0, format="%.2f")
    
    # Input height in meters
    height_m = st.number_input("Enter your height in meters:", min_value=0.0, format="%.2f")
    
    if st.button("Calculate BMI"):
        # Calculate BMI
        bmi = calculate_bmi(weight_kg, height_m)
        
        # Display BMI
        st.write(f"Your BMI is: {bmi:.2f}")
        
        # Interpret BMI
        if bmi < 18.5:
            st.write("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.write("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.write("You are overweight.")
        else:
            st.write("You are obese.")

if __name__ == "__main__":
    main()

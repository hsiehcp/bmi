def calculate_bmi(weight_kg, height_m):
    # Calculate BMI
    bmi = weight_kg / (height_m ** 2)
    return bmi

def main():
    print("BMI Calculator")
    
    # Input weight in kilograms
    weight_kg = float(input("Enter your weight in kilograms: "))
    
    # Input height in meters
    height_m = float(input("Enter your height in meters: "))
    
    # Calculate BMI
    bmi = calculate_bmi(weight_kg, height_m)
    
    # Print BMI
    print(f"Your BMI is: {bmi:.2f}")
    
    # Interpret BMI
    if bmi < 18.5:
        print("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        print("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        print("You are overweight.")
    else:
        print("You are obese.")

if __name__ == "__main__":
    main()


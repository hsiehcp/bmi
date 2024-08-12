# Input weight in kilograms
weight_kg = float(input("Enter your weight in kilograms: "))
    
# Input height in meters
height_m = float(input("Enter your height in meters: "))
    
# Calculate BMI
bmi = weight_kg / (height_m)**2
    
    # Print BMI
print(f"Your BMI is: {bmi:.2f}")

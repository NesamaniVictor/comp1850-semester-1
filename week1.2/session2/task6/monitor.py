# Week 1.2, Session 2: Task 6

print("Welcome to the Monitor Program!")
print("Select an option:")
print("1. Input machine's temperature in degrees Celsius")
print("2. Input machine's pressure in PSI")
print("3. Input machine's operational status (1 for operating, 0 for stopped)")

# \u00B0 will print the Celsius character
if option == 1:
    print("You selected to input the machine's temperature.")
    temperature = float(input("Enter the temperature in degrees Celsius: "))
    if temperature > 80:
        print(f"Warning: The machine's temperature is too high at {temperature}\u00B0C! Recommended to shut down the machine.")
    elif  50 <= temperature <= 80:
        print(f"The machine's temperature {temperature}\u00B0C is within safe limits.")
    else: temperature < 50
        print(f"The machine's temperature {temperature}\u00B0C is low. No action needed.")
    
elif option == 2:
    print("You selected to input the machine's pressure.")
    pressure = float(input("Enter the pressure in PSI: "))
    if pressure >100:
        print(f"Warning: High pressure {pressure) PSI detected! Recommend maintenance check.")
    elif 70 <= pressure <= 100:
        print(f"The machine's pressure {pressure} PSI is stable.")
    else: pressure <70
        print(f"The machine's pressure {pressure} PSI is low. The system is operating normally.")

else option == 3:
    print("You selected to input the machine's operational status.")
    
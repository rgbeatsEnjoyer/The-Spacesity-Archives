unit = str(input("Choose the unit you want to convert to (Degrees Celcius (C) or Fahrenheit (F)):").upper())
temperature = float(input("Enter your temperature:"))
if unit == "F":
    temperature = temperature * 1.8 + 32
    print(f"Fahrenheit:{temperature}")
elif unit == "C":
    temperature = (temperature - 32) / 1.8
    print(f"Celcius:{temperature}")
else:
    pass
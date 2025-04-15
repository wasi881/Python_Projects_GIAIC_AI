import streamlit as st


# Ye function value ko aik unit se dosri unit main convert karta hai
def convert_units(value, from_units, to_units):
    # Dictionary main sari conversions ki values store ki gai hain
    conversions = {
        # Length
        "meters_kilometers": 0.001,
        "kilometers_meters": 1000,
        "centimeters_kilometers": 0.00001,
        "kilometers_centimeters": 100000,
        "centimeters_meters": 0.01,
        "meters_centimeters": 100,
        "millimeters_centimeters": 0.1,
        "centimeters_millimeters": 10,
        "millimeters_meters": 0.001,
        "meters_millimeters": 1000,
        "inches_centimeters": 2.54,
        "centimeters_inches": 0.393701,
        "feet_meters": 0.3048,
        "meters_feet": 3.28084,
        "yards_meters": 0.9144,
        "meters_yards": 1.09361,
        "miles_kilometers": 1.60934,
        "kilometers_miles": 0.621371,
        
        # Weight
        "grams_kilograms": 0.001,
        "kilograms_grams": 1000,
        "pounds_kilograms": 0.453592,
        "kilograms_pounds": 2.20462,
        "ounces_grams": 28.3495,
        "grams_ounces": 0.035274,
        "pounds_ounces": 16,
        "ounces_pounds": 0.0625,
        "pounds_grams": 453.592,
        "grams_pounds": 0.00220462,
        "ounces_kilograms": 0.0283495,
        "kilograms_ounces": 35.274,
        "milligrams_grams": 0.001,
        "grams_milligrams": 1000,
        "tons_kilograms": 1000,
        "kilograms_tons": 0.001,

        # Time
        "seconds_minutes": 1/60,
        "minutes_seconds": 60,
        "minutes_hours": 1/60,
        "hours_minutes": 60,
        "seconds_hours": 1/3600,
        "hours_seconds": 3600,
        "hours_days": 1/24,
        "days_hours": 24,
        "minutes_days": 1/1440,
        "days_minutes": 1440,
        "seconds_days": 1/86400,
        "days_seconds": 86400,
        "days_weeks": 1/7,
        "weeks_days": 7,
        "days_months": 1/30.44,
        "months_days": 30.44,
        "months_years": 1/12,
        "years_months": 12,

        # Volume
        "liters_milliliters": 1000,
        "milliliters_liters": 0.001,
        "gallons_liters": 3.78541,
        "liters_gallons": 0.264172,
        "cups_liters": 0.236588,
        "liters_cups": 4.22675,
        "milliliters_cups": 0.00422675,
        "cups_milliliters": 236.588,
        "gallons_milliliters": 3785.41,
        "milliliters_gallons": 0.000264172,
        "cups_gallons": 0.0625,
        "gallons_cups": 16,
        "fluid_ounces_milliliters": 29.5735,
        "milliliters_fluid_ounces": 0.033814,
        "cubic_meters_liters": 1000,
        "liters_cubic_meters": 0.001
    }

    # Temperature conversions ko alag handle karte hain
    formula_conversions = {
        "celsius_fahrenheit": lambda c: (c * 9/5) + 32,
        "fahrenheit_celsius": lambda f: (f - 32) * 5/9,
        "celsius_kelvin": lambda c: c + 273.15,
        "kelvin_celsius": lambda k: k - 273.15,
        "fahrenheit_kelvin": lambda f: ((f - 32) * 5/9) + 273.15,
        "kelvin_fahrenheit": lambda k: ((k - 273.15) * 9/5) + 32
    }

    from_units = from_units.lower().replace(" ", "_")
    to_units = to_units.lower().replace(" ", "_")
    key = f"{from_units}_{to_units}"

    # Check karta hai ke conversion possible hai ya nahi
    if from_units == to_units:
        return value
    elif key in conversions:
        conversion = conversions[key]
        return value * conversion
    elif key in formula_conversions:
        return formula_conversions[key](value)
    else:
        return "Conversion not supported"

# Main heading display karne ke liye
st.title("Unit Converter")

# User se value input lene ke liye
value = st.number_input("Enter the value:", min_value=None, step=0.1)

# Available units ko categories main organize karna
length_units = ["Meters", "Kilometers", "Centimeters", "Millimeters", "Inches", "Feet", "Yards", "Miles"]
weight_units = ["Grams", "Kilograms", "Pounds", "Ounces", "Milligrams", "Tons"]
time_units = ["Seconds", "Minutes", "Hours", "Days", "Weeks", "Months", "Years"]
volume_units = ["Liters", "Milliliters", "Gallons", "Cups", "Fluid Ounces", "Cubic Meters"]
temperature_units = ["Celsius", "Fahrenheit", "Kelvin"]

# Category selection with icons
category = st.selectbox("Select category:", ["📏 Length", "⚖️ Weight", "⏰ Time", "🥛 Volume", "🌡️ Temperature"])

# Units ko category ke hisab se filter karna
if category == "📏 Length":
    available_units = length_units
elif category == "⚖️ Weight":
    available_units = weight_units
elif category == "⏰ Time":
    available_units = time_units
elif category == "🥛 Volume":
    available_units = volume_units
else:  # Temperature
    available_units = temperature_units

# User se source aur target unit select karne ke liye dropdown
from_units = st.selectbox("Convert from:", available_units)
to_units = st.selectbox("Convert to:", available_units)

# Convert button ke click hone par ye code chalta hai
if st.button("Convert"):
    if not value:
        st.error("Please enter a value to convert")
    else:
        result = convert_units(value, from_units, to_units)
        # Agar result string hai to error dikhata hai
        if isinstance(result, str):
            st.error(result)
        # Warna conversion ka result dikhata hai
        else:
            st.success(f"{value} {from_units} = {result:.4f} {to_units}")

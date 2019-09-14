'''Converts temperatures units between Kelvins, Celsius and Fahrenheit.

Usage:
    ./temp_converter.py

Authorship, date:
    Susanna Werth, 2019
'''


# Global variables
# ----------------------------------------------------------------------
# this section is empty, as we do not assign any global variables, but they would go here



# Module import
# ----------------------------------------------------------------------
# this is empty, as we do not import any modules, but they would go here



# Classes
# ----------------------------------------------------------------------
# this is empty, as we do not define any classes, but they would go here



# Functions
# ----------------------------------------------------------------------

def celsiusToFahr(tempCelsius):
    return 9/5 * tempCelsius + 32

def kelvinsToCelsius(tempKelvins):
    return tempKelvins - 273.15

def kelvinsToFahrenheit(tempKelvins):
    tempCelsius = kelvinsToCelsius(tempKelvins)
    tempFahr = celsiusToFahr(tempCelsius)
    return tempFahr

def tempCalculator(tempK, convertTo):
    """
    Function for converting temperature in Kelvins to Celsius or Fahrenheit.

    Parameters
    ----------
    tempK: <numerical>
        Temperature in Kelvins
    convertTo: <str>
        Target temperature that can be either Celsius ('C') or Fahrenheit ('F'). Supported values: 'C' | 'F'

    Returns
    -------
    <float>
        Converted temperature.
    """

    # Check if user wants the temperature in Celsius
    if convertTo == "C":
        # Convert the value to Celsius using the dedicated function for the task that we imported from another script
        convertedTemp = kelvinsToCelsius(tempKelvins=tempK)
    elif convertTo == "F":
        # Convert the value to Fahrenheit using the dedicated function for the task that we imported from another script
        convertedTemp = kelvinsToFahrenheit(tempKelvins=tempK)
    # Return the result
    return convertedTemp



# Main Function
# ----------------------------------------------------------------------
def main():
    print("This is the main function.")
    tempKelvin = 30
    temperatureC = tempCalculator(tempK=tempKelvin, convertTo="C")
    print("Temperature", tempKelvin, "in Kelvins is", temperatureC, "in Celsius")

    
    
# Top-level script environment
# ----------------------------------------------------------------------
    
if __name__ == '__main__':
    # Code to run when this is the main program
    main()
    
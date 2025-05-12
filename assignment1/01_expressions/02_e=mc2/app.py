
"""
Program: mass_energy_converter
----------------------
This program calculates energy (E) using Einstein's mass-energy equivalence formula:

    E = m * c^2

The user provides mass in kilograms, and the program outputs the equivalent energy in joules.
"""

# Define the speed of light as a constant (in meters per second)
C: int = 299792458  # Speed of light (m/s)

def main():
    """
    Prompts the user for mass in kilograms, computes energy using Einstein's equation,
    and displays the result in joules.
    """
    # Get mass input from the user
    mass_in_kg: float = float(input("Enter kilos of mass: "))

    # Calculate energy using the formula E = m * C^2
    energy_in_joules: float = mass_in_kg * (C ** 2)

    # Display the calculation process and result
    print("\ne = m * C^2...")
    print(f"m = {mass_in_kg} kg")
    print(f"C = {C} m/s")
    print(f"{energy_in_joules} joules of energy!")

# Ensures the main() function runs when the script is executed
if __name__ == '__main__':
    main()


# Planetary Weight Calculator

def calculate_weight_on_planet(earth_weight, planet):
    # Dictionary of planetary gravity percentages relative to Earth
    gravity_factors = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }
    
    # Get the gravity factor for the selected planet
    if planet in gravity_factors:
        planet_weight = earth_weight * gravity_factors[planet]
        return round(planet_weight, 2)
    else:
        return None  # In case of an invalid planet name

def main():
    # Prompt user for input
    earth_weight = float(input("Enter a weight on Earth: "))
    planet = input("Enter a planet: ").strip()
    
    # Calculate weight on the selected planet
    weight_on_planet = calculate_weight_on_planet(earth_weight, planet)
    
    if weight_on_planet is not None:
        print(f"The equivalent weight on {planet}: {weight_on_planet}")
    else:
        print("Invalid planet name. Please enter a valid planet name from the solar system.")

# Run the program if executed directly
if __name__ == "__main__":
    main()

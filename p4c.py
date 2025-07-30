country_cities = {
    "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth"],
    "UAE": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"],
    "India": ["Mumbai", "Bangalore", "Chennai", "Delhi"]
}

def find_country(city_name):
    for country, cities in country_cities.items():
        if city_name in cities:
            return country
    return None

city1 = input("Enter the first city: ").strip()
city2 = input("Enter the second city: ").strip()

country1 = find_country(city1)
country2 = find_country(city2)

if country1 and country2:
    if country1 == country2:
        print(f"Yes, both {city1} and {city2} are in {country1}.")
    else:
        print(f"No, {city1} is in {country1} and {city2} is in {country2}.")
else:
    if not country1:
        print(f"{city1} not found in the database.")
    if not country2:
        print(f"{city2} not found in the database.")
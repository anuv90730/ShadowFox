country_cities = {"Australia": ["Sydney", "Melbourne", "Brisbane", "Perth"],
                  "UAE": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"], 
                  "India": ["Mumbai", "Bangalore", "Chennai", "Delhi"]
                  }

city = input("Enter a city name: ").strip()

found = False

for country, cities in country_cities.items():
    if city in cities:
        print(f"{city} is in {country}.")
        found = True
        break

if not found:
    print("City not found in the database.")
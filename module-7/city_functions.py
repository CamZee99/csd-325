def city_country(city, country, population=None, language=None):
    result = f"{city.title()}, {country.title()}"
    if population:
        result += f" - population {population}"
    if language:
        result += f", {language.title()}"
    return result


print(city_country("berlin", "germany"))
print(city_country("madrid", "spain", 3266000))
print(city_country("rome", "italy", 2873000, "italian"))


# This function formats city and country data into a readable string.
# Population and language are optional parameters that enhance the output.
# This file demonstrates calling the function in three ways:
# With just city and country
# With city, country, and population
# With all four parameters: city, country, population, and language
# dictionary comprehensions : Create dictionaries using an expression.
#                             Can replace for loops and certain lambda functions
# dictionary = {key: expression for (key, value) in iterable}

#cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}

#cities_in_C = {key: round((value - 32) * (5/9)) for (key, value) in cities_in_F.items()}

#print(cities_in_C)

# for if statements:
# dictionary = {key: expression for (key, value) in iterable if conditional}
#weather = {'New York': "Snowing", 'Boston': "Sunny", 'Los Angeles': "Sunny", 'Chicago': "Cloudy"}

#sunny_weather = {key: value for (key, value) in weather.items() if value == "Sunny"}

#print(sunny_weather)

# for if else statements:
# dictionary = {key: (if/else) for (key, value) in iterable}
#cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}

#desc_cities = {key: ("Warm" if value >= 40 else "Cold") for (key, value) in cities.items()}

#print(desc_cities)

# for functions:
# dictionary = {key: function(value) for (key, value) in iterable}
cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}

def check_temp(value):
    if value >= 70:
        return "Hot"
    elif 69 >= value >= 40:
        return "Warm"
    else:
        return "Cold"

desc_cities = {key: check_temp(value) for (key, value) in cities.items()}

print(desc_cities)
import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

countries = []
with open(os.path.join(__location__, 'Countries.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        countries.append(dict(r))

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
italy_temps = []
for city in cities:
    italy_temps.append(float(city['temperature']))
print(sum(italy_temps)/len(italy_temps))
print()

# Print all cities in Italy
italy_temps = []
my_country = 'Italy'
for city in cities:
    if city['country'] == my_country:
        italy_temps.append(city['city'])
print("All the cities in", my_country, ":")
print(italy_temps)
print()

# Print the average temperature for all the cities in Italy
# Write code for me
italy_temps = []
my_country = 'Italy'
for city in cities:
    if city['country'] == my_country:
        italy_temps.append(float(city['temperature']))
print("The average temperature of all the cities in", my_country, ":")
print(sum(italy_temps)/len(italy_temps))
print()

# Print the max temperature for all the cities in Italy
# Write code for me
italy_temps = []
my_country = 'Italy'
for city in cities:
    if city['country'] == my_country:
        italy_temps.append(float(city['temperature']))
print("The max temperature of all the cities in", my_country, ":")
print(max(italy_temps))
print()

# Let's write a function to filter out only items that meet the condition

def filter(condition, dict_list):
    filtered_list = []
    for item in dict_list:
        if condition(item):
            filtered_list.append(item)
    return filtered_list
x = filter(lambda x: float(x['latitude']) >= 60.0, cities)

for item in x:
    print(item)

# Let's write a function to do aggregation given an aggregation function and an aggregation key
def aggregate(aggregation_key, aggregation_function, dict_list):
    value = []
    for item in dict_list:
        value.append(item[aggregation_key])
    return aggregation_function(value)
# Let's write code to
# - print the average temperature for all the cities in Italy
# - print the average temperature for all the cities in Sweden
# - print the min temperature for all the cities in Italy
# - print the max temperature for all the cities in Sweden

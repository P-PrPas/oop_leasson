import csv
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Week 11 Assignment: OO-styled data processing code

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

class TableDB:
    def __init__(self):
        self.table_database = []

    def insert(self, table):
        for row in table:
            self.table_database.append(row)

    def search(self, table_name):
        searched = []
        for row in self.table_database:
            if table_name in row.keys():
                searched.append(row)
        return searched


class Table:
    def __init__(self, table_name, table):
        self.table = table[table_name]

    def filter(self, condition):
        filtered_list = []
        for item in self.table:
            if condition(item):
                filtered_list.append(item)
        return filtered_list

    def aggregate(self, aggregation_key, aggregation_function):
        value = []
        for item in self.table:
            value.append(item[aggregation_key])
        return aggregation_function(value)

    def __str__(self):
        return str(self.table)

# Lab Week 11

'''cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

countries = []
with open(os.path.join(__location__, 'Countries.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        countries.append(dict(r))'''


'''class DataBase:
    def __init__(self, file_name):
        self.table = []
        with open(os.path.join(__location__, file_name)) as f:
            rows = csv.DictReader(f)
            for r in rows:
                self.table.append(dict(r))

    def load_table(self):
        return self.table


class TableProcessing:
    def __init__(self, table):
        self.table = list(table)

    def filter(self, condition):
        filtered_list = []
        for item in self.table:
            if condition(item):
                filtered_list.append(item)
        return filtered_list

    def aggregate(self, aggregation_key, aggregation_function):
        value = []
        for item in self.table:
            value.append(item[aggregation_key])
        return aggregation_function(value)

    def average_temp(self, country: str = None):
        temp = []
        if country == None:
            for item in self.table:
                temp.append(float(item["temperature"]))
        else:
            temp = []
            for item in self.table:
                if item["country"] == country:
                    temp.append(float(item["temperature"]))
        return sum(temp) / len(temp)

    def all_city(self, country : str = None):
        city = []
        if country == None:
            for item in self.table:
                city.append(item["city"])
        else:
            for item in self.table:
                if item["country"] == country:
                    city.append(item["city"])
        return city

    def maxInfo(self, country:str = None, option:str = None):
        if option == None:
            raise ValueError("Please enter an option")
        temp = []
        if country == None:
            for item in self.table:
                temp.append(float(item[option]))
        else:
            for item in self.table:
                if item["country"] == country:
                    temp.append(float(item[option]))
        return max(temp)

    def minInfo(self, country:str = None, option:str = None):
        if option == None:
            raise ValueError("Please enter an option")
        temp = []
        if country == None:
            for item in self.table:
                temp.append(float(item[option]))
        else:
            for item in self.table:
                if item["country"] == country:
                    temp.append(float(item[option]))
        return min(temp)

city = DataBase('Cities.csv')
countries = DataBase('Countries.csv')

city_table = city.load_table()
countries_table = countries.load_table()

city_processor = TableProcessing(city_table)

min_latitude = city_processor.minInfo(option='latitude')
max_latitude = city_processor.maxInfo(option='latitude')

print(min_latitude, max_latitude)'''

'''# Print the average temperature of all the cities
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
    return aggregation_function(value)'''
# Let's write code to
# - print the average temperature for all the cities in Italy
# - print the average temperature for all the cities in Sweden
# - print the min temperature for all the cities in Italy
# - print the max temperature for all the cities in Sweden

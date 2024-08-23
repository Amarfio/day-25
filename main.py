
# get the data from weather_data.csz into a list called data

# with open("./weather_data.csv", mode="r") as file :
#     data = file.readlines();
#
#     # print(data)
#     for line in data:
#         print(line)

import csv

import pandas

# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     new_temperatures = []
#     for row in data:
#         if(row[1] != "temp"):
#             temperatures.append(int(row[1]))
#     print(temperatures)
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# # print(data["temp"])
# temp_list = data["temp"].to_list()
# print(temp_list)
# print()
# average = sum(temp_list ) /len(temp_list)
# print(average.__round__(2))
# print(data["temp"].mean())
# print(data["temp"].max())
#
#
# print(data[data.temp == data["temp"].max()])
# monday  = data[data.day == "Monday"]
# # print(monday.temp)
#
# # print(monday["temp"])
#
# def fahrenheit(celsius):
#     return (1.8 * celsius) +32
#
#
# print(fahrenheit(monday.temp[0]))

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# # print(data)
# # print(data["scores"].max())
# data.to_csv("new_data.csv")


#solve the squirrel problem
#import the data from the csv
#display the specified columns with their corresponding data
#and create the manipulations as specified
data = pandas.read_csv("squirrel_data.csv")
print(data["Primary Fur Color"].to_list())
print(type(data["Primary Fur Color"].value_counts()))

gray_count = len(data[data["Primary Fur Color"] == "Gray"]);
black_count = len(data[data["Primary Fur Color"] == "Black"]);
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"]);
# print(gray_count)
data_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [gray_count, black_count, cinnamon_count]
}

data = pandas.DataFrame(data_dict)
data.to_csv("squirrel_count.csv")
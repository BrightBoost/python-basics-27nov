temperature = 12.3
raining = True
description_weather = "Not great"
today_date = "2024-11-27"

print("Today the date is " + today_date + ". The temperature is " + str(temperature))

nr_eggs = 145
box_size = 12

boxes_of_eggs = nr_eggs // box_size
eggs_left = nr_eggs % box_size

print(boxes_of_eggs)
print(eggs_left)
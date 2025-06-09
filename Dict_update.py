food_time = {"breakfast":"8-9am" ,"lunch":"1-2pm", "dinner":"10-11pm"}
# lunch = food_time["lunch"]
# print(f"lunch = {lunch}")

# dinner = food_time["dinner"]
# print("dinner =" ,dinner)

food_time["snacks"] = "4-5pm"
print("updated_food_time: ", food_time)

# remove dinner from dictionary
# del food_time["dinner"]
# print("after removing dinner: ", food_time)

# b = food_time.pop()
# print(b)
# print(food_time)   it gives error becoz pop() has atleast one argument

a = food_time.pop("dinner")
print(a)
print(food_time)
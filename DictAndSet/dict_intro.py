vehicles = {
    'dream': 'Honda 250T',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
    'roadster': "Triump Street Triple",  # duplicate but replace with the latest value
}
# -------------------------------
# # finding with key
# my_car = vehicles['fiesta']
# print(my_car)
#
# # my_car = vehicles['Fiesta']
# # print(my_car)
#
# commuter = vehicles['virago']
# print(commuter)
#
# # using get methods
# learner = vehicles.get("er5")
# print(learner)
#
# # learner = vehicles.get("ER5")
# # print(learner)
# -------------------------------

# -------------------------------
# print dictionary key printed out
# for key in vehicles:
#     print(key)

# print dictionary key and values printed out
# for key in vehicles:
#     print(key, vehicles[key], sep=", ")
# -------------------------------


vehicles["starfigher"] = "Lockheed F-104"
vehicles["learjet"] = "Bombardier Learjet 75"
vehicles["toy"] = "Glider"

# ----------------------Updating the values in vehicle virago -------------------------------------
# upgrade the Virago model
vehicles['virago'] = "Yamaha XV535"

# remove item from dictionary if
del vehicles["starfigher"]

# remove item from dictionary, it does not exist
# del vehicles["f1"]
# result = vehicles.pop("f1", None)  # if None: if not sure if key exist and it will not crash if dont have key
result = vehicles.pop("f1", "You wish! Sell the Learjet and you might afford a racing car.") # if not sure if key exist and# if None: if not sure if key exist and it will not crash if dont have key
print(result)
plane = vehicles.pop("learjet")
print(plane)

bike = vehicles.pop("tenere", "not present")
print(bike)
print()

for key, value in vehicles.items():
    print(key, value, sep=", ")

vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
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
for key, value in vehicles.items():
    print(key, value, sep=", ")

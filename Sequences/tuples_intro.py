# t = ("a", "b", "c")
# print(type(t))
# print(t)

# welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
# bad = "Bad Company", "Bad Company", 1974
# budgie = "Nightflight", "Budgie", 1981
# imelda = "More Mayhem", "Emilda May", 2011
# metallica = "Ride the Lightning", "Metallica", 1984

# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])

# # using list to change the items
# metallica2 = list(metallica)
# print(metallica2)
#
# metallica2[0] = "Master of Puppets"
# print(metallica2)

# # =================================================================
# welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
# bad = "Bad Company", "Bad Company", 1974
# budgie = "Nightflight", "Budgie", 1981
# imelda = "More Mayhem", "Emilda May", 2011
# metallica = "Ride the Lightning", "Metallica", 1984
#
# title, artist, year = metallica
# print(title)
# print(artist)
# print(year)
#
# table = ("Coffee table", 200, 100, 75, 34.50)
# print(table[1] * table[2])
#
# # unpack the tuple to variable and use the variable name in code
# name, length, width, height, price = table
# print(length * width)

# =================================================================
albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]

print(len(albums))

for name, artist, year in albums:
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))

print("*" * 80)
for album in albums:
    name, artist, year = album
    print("Album: {}, Artist: {}, Year: {}"
          .format(name, artist, year))

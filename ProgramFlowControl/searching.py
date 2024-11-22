shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
# items_to_find = "spam"
items_to_find = "albatross"
found_at = None # None: to show it does not have value

# for index in range(6):
# for index in range(len(shopping_list)):
#     if shopping_list[index] == items_to_find:
#         found_at = index
#         break

if items_to_find in shopping_list:
    found_at = shopping_list.index(items_to_find)
if found_at is not None:
    print("Item found at position {}".format(found_at))
else:
    print("{} not found".format(items_to_find))

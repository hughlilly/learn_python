
# Get all the elements in a list — with indices

shopping_list = ["Tomatoes", "Bananas", "Crackers",
                 "Sugar", "Icecream", "Bread", "Bananas", "Chocolate"]

shopping_list.sort()

print("Itemised shopping list:")

# Pass the list object to an iterator function, enumerate()
# This allows us to access each item's position in the list
enumerated_list = enumerate(shopping_list)
for position, item in enumerated_list:
    print(f"{position}. {item}")

# So you can loop over objects, and you can loop over functions/iterators
# (To be more precise, you can loop over what a function returns)

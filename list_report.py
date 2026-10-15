
# Week 7 Assignment - Part C: List Report

items = ["bread", "avocado", "milk", "sweet potatoes", "tea"]

# 1. Print every item with its number
print("Shopping List Report")
print("--------------------")

number = 1

for item in items:
    print(str(number) + ". " + item)
    number = number + 1

# 2. Count item names with more than 4 letters
count = 0

for item in items:
    if len(item) > 4:
        count = count + 1

print("\nItems with more than 4 letters:", count)

# 3. Find the longest item name using a loop
longest = items[0]

for item in items:
    if len(item) > len(longest):
        longest = item

print("Longest item name:", longest)

expenses_in_months = [2200, 2350, 2600, 2130, 2190]

# 1. In Feb, how many dollars you spent extra compare to January?
print(expenses_in_months[1] - expenses_in_months[0])

# 2. Find out your total expense in first quarter (first three months) of the year.
quarter_expenses = 0
for expense in expenses_in_months[0:3]:
    quarter_expenses += expense
print(quarter_expenses)

# 3. Find out if you spent exactly 2000 dollars in any month

# for expense in expenses_in_months:
#     if expense == 2000:
#         print(True)
#     else: 
#         print(False)

print(2000 in expenses_in_months)

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expenses_in_months.append(1980)
print(expenses_in_months)


# 5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this

# expenses_in_months.remove(2130)
# expenses_in_months.insert(3, 1930)

expenses_in_months[3] -= 200
print(expenses_in_months)


heroes=['spider man','thor','hulk','iron man','captain america']

# 1. Length of the list
print(len(heroes))

# 2. Add 'black panther' at the end of this list
heroes.append("black panther")
print(heroes)

# 3. You realize that you need to add 'black panther' after 'hulk', so remove it from the list first and then add it after 'hulk'
heroes.remove("black panther")
heroes.insert(3, "black panther")
print(heroes)

# 4. Now you don't like thor and hulk because they get angry easily :) 
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
heroes[1:3] = ["doctor strange"]
print(heroes)

# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heroes.sort()
print(heroes)



# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
max = int(input("Enter the max number for the list of odds: "))
numbers = []

for i in range(max):
    if i % 2 != 0:
        numbers.append(i)

print(numbers)
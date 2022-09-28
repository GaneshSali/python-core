
# EX 1

# expenses = [2200,2350,2600,2130,2190]

# # 1. In Feb, how many dollars you spent extra compare to January?
# feb_jan_diff = expenses[1] - expenses[0]
# print(feb_jan_diff)


# # 2. Find out your total expense in first quarter (first three months) of the year.
# t = 0
# for i in expenses[:3]:
#     t += i
# print(t)
# print(expenses[0]+expenses[1]+expenses[2])


# # 3. Find out if you spent exactly 2000 dollars in any month
# if 2000 in expenses:
#     print("yes")
# else:
#     print("no")


# # 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# expenses.append(1980)
# print(expenses)


# # 5. You returned an item that you bought in a month of April and
# # got a refund of 200$. Make a correction to your monthly expense list
# # based on this

# expenses[3] = expenses[3] - 200
# print(expenses)








# EX 2

# heros=['spider man','thor','hulk','iron man','captain america']

# # 1. Length of the list
# print(len(heros))

# # 2. Add 'black panther' at the end of this list
# heros.append('black panther')
# print(heros)

# # 3. You realize that you need to add 'black panther' after 'hulk',
# #    so remove it from the list first and then add it after 'hulk'
# heros.remove('black panther')
# heros.insert(3,'black panther')
# print(heros)


# # 4. Now you don't like thor and hulk because they get angry easily :)
# #    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
# #    Do that with one line of code.
# # heros.
# heros[1:3]=['doctor strange']
# print(heros)


# # 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
# heros.sort()
# print(heros)







# EX 3

# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function

# def fun(n):
#     ll = []
#     for i in range(1,n):
#         if i%2 == 1:
#             ll.append(i)
#     return ll

# n = int(input("Enter num : "))
# print(fun(n))
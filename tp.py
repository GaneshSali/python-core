# def capital_indexes(word):
#     ll = []
#     for i,w in enumerate(word):
#         if w.isupper():
#             ll.append(i)
#     return ll
            
# c = capital_indexes("TEsT")
# print(c)


# def format_number(num):
#     n = str(num)
#     e = list(n)
#     for i in range(len(e))[::-3][1:]:
#         e.insert(i+1,",")
#     result = "".join(e)
#     return result

# def format_number(n):
#     result = ""
#     for i, digit in enumerate(reversed(str(n))):
#         if i != 0 and (i % 3) == 0:
#             result += ","
#         result += digit

#     return result[::-1]
    
# print(format_number(1234567))

# value = 1234567
# print ('{:,}'.format(value)) 


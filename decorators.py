# Closures

# def logger(msg):
#     def log_msg():
#         print(msg)
#     return log_msg

# a = logger("hi")
# a()


# Decorators

# def decorator_fun(ori_fun):
#     def wrapper_fun(*args):
#         print("before")
#         ori_fun(*args)
#         print("after")
#     return wrapper_fun

# @decorator_fun
# def display():
#     print("hello")

# # display = decorator_fun(display)
# display()

# @decorator_fun
# def display2(x):
#     print("hi",x)

# display2(2)



# Example Timer

# import time

# def timer(original_fun):
#     def wrapper(*args,**kwargs):
#         t1 = time.time()
#         res = original_fun(*args,**kwargs)
#         t2 = time.time() - t1
#         print("fun takes time : {}".format(t2))
#         return res 
#     return wrapper

# @timer
# def t1():
#     print("t1")
#     time.sleep(1)

# @timer
# def t2():
#     print("t2")
#     time.sleep(2)

# t1()
# t2()


# Example sum

# def smartdiv(func):
#     def wrapper(a,b):
#         if a < b:
#             a,b = b,a
#         return func(a,b)
#     return wrapper

# @smartdiv
# def div(a,b):
#     return a/b

# print(div(6,3))


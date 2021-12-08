import functools


#
# def start(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print("strat")
#         result=func(*args, **kwargs)
#         print("end")
#
#         return result
#
#     return wrapper
#
#
# @start
# def add5(x):
#     return x + 5
#
#
# a = add5(10)
# print(a)

# -------------------------------------------------------------------------

# class Count:
#     def __init__(self, func):
#         self.func = func
#         self.num_calls = 0
#
#     def __call__(self, *args, **kwargs):
#         self.num_calls += 1
#         print(self.num_calls)
#         return self.func(*args, **kwargs)
#
#
#
# @Count
# def say_hello():
#     print("hello")
#
#
# say_hello()
# say_hello()
# say_hello()

# ---------------------------------------------------------------------------------------------
# def repeat(number):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             global result
#             for _ in range(number):
#                 result=func(*args, **kwargs)
#             return result
#
#         return wrapper
#     return decorator
#
#
# @repeat(number=3)
# def greet(name):
#     print(f'Hello {name}')
#
# greet('hamed')
# ----------------------------------------------------------------------------------------
class Repeat:
    def __init__(self, number):
        self.number = number

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            global result
            for _ in range(self.number):
                result = func(*args, **kwargs)
            return result

        return wrapper


@Repeat(number=1)
def greet(name):
    print(f'Hello {name}')

greet('hamed')

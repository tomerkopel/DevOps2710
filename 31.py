import datetime
import requests


# print(datetime.datetime.now())

# response = requests.get("https://www.google.com")
# if 200 <= response.status_code <300:
#     print("The web is up")
# else:
#     print("The web is down")


# names = open('names.txt')
# print(names.readlines())

def save_name(name):
    try:
        names = open("name.txt", mode="r")
        names.write(name+'\n')
        names.close()
    except BaseException as e:
        print(e.args)

def read_names():
    try:
        names = open("name.txt")
        for name in names:
            print(name, end='')
    except BaseException as e:
        print(e.args)

save_name("Tomer")
save_name("Kopel")
read_names()

# def div_numbers(x, y):
#     try:
#         print(x / y)
#     except ZeroDivisionError:
#         print("You can't divide numbers by zero.")
#     except TypeError:
#         print("You can't devide numbers by string")
#     except BaseException as e:
#         print(f"Error 123 - {e.args}")
#
#
# div_numbers(10, 0)
# div_numbers(10, '2')

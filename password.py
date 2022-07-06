# Random password Generator using Python
import random
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
symbol = "!@#$%&*?.,:;}][{"
user_password = upper_case + lower_case + num + symbol
user_length = 8
password = "".join(random.sample(user_password,user_length))
print("Your password is", password)


# Creates a sorted dictionary (sorted by key)
# from collections import OrderedDict
#
# dict = {'ravi': '10', 'rajnish': '9', 'sanjeev': '15', 'yash': '2', 'suraj': '32'}
# dict1 = OrderedDict(sorted(dict.items()))
# print(dict1)
#------------------------------------------
from typing import OrderedDict

my_dict = {1: {"p": 350, "z": 750, "a": 170, "c": 110},
           6: {"p": 100, "z": 700, "a": 120, "c": 900},
           4: {"p": 300, "z": 200, "a": 450, "c": 130}}

sort_values = my_dict.items()
new_item = sorted(sort_values, key=lambda key_value: key_value[1]["c"], reverse=True)
list = OrderedDict(new_item)
print(list)

#--------------------------------------------

my_dict = [{"Country": "Germany", "Val": 40},
           {"Country": "England", "Val": 10},
           {"Country": "Japan", "Val": 60}]

print(sorted(my_dict, key=lambda i: i['Val']))
print("\r")
print(sorted(my_dict, key=lambda i: (i['Val'], i['Country'])))
print("\r")
print(sorted(my_dict, key=lambda i: i['Val'], reverse=True))  # descending order

#--------------------------------------------


from tokenize import String
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class University:
    _name = ""
    _location = ""

    def __init__(self, name, location):
        self.name = name
        self.location = location

    def display(self):
        print(f"The name of Institute is {self.name} and located in {self.location}")


class Departement(University):
    _name = ""
    _Students = 0

    def __init__(self, name, Students, u_name, u_location):
        super().__init__(u_name, u_location)
        self.name = name
        self.Students = Students

    def display(self):
        print(f"There are {self.Students} in {self.name} departement.")


object1 = University("FAST", "ISLAMABAD")
object1.display()

child_object = Departement("AI", 60, "FAST", "ISLAMABAD")
child_object.display()

enu_list = ["FAST", "NUST", "GIKI", "PIEAS", "PUCIT"]

for i in enumerate(enu_list, 5):
    print(i)

# STRING TASKS


Strings_list = ["tought", "ABBA", "FAST", "an", "aka", "light", "DELL"]


def Check_String(string):
    if (len(string) >= 2) and (string[0] == string[-1]):
        return True

    return False


for i in Strings_list:

    if Check_String(i):
        print(i)

# ----------------------------------------

String_list2 = ['xfam', 'abc', 'literals', 'pokemon', 'doreamon']


def Sorting_list(st_list):
    flist = []
    st_list = sorted(st_list)

    for i in st_list:
        if i[0].lower() != 'x':
            flist.append(i)

    return flist


fl = Sorting_list(String_list2)
print(fl)

# ----------------------------------------

tuple_list = [(1, 0, 3), (1, 2, 0), (6, 3, 6,), (1, 8, 4), (5, 8, 4)]
tuple_list = sorted(tuple_list, key=lambda x: x[-1])
print(tuple_list)

# ----------------------------------------

list1 = [1, 2, 3, 4, 4, 5, 5, 6, 7, 8]

list1 = list(dict.fromkeys(list1))
print(list1)

# ----------------------------------------

list11 = [2, 5, 3, 1, 7, 9, 7, 5, 4]
list22 = [2, 4, 3, 7, 8, 9, 0, 6, 5, 4, 5]

Final_list = sorted(sorted(list11) + sorted(list22))
print(Final_list)

# ----------------------------------------

df = pd.read_csv("drinks.csv")
Rows, Cols = df.shape
print(Rows)
df = df.dropna()


def Col_Data(Name):
    return df[Name]


Col_Data('country')

X = Col_Data('country')
Y = Col_Data('beer_servings')

plt.hist(Y)
plt.show()

plt.scatter(X[:5], Y[:5])
plt.show()

X = Col_Data('beer_servings')[:5]
Y = Col_Data('wine_servings')[:5]
plt.pie(X, labels=Y)
plt.show()

# plt.figure(figsize = (10, 5))
Y = Col_Data('country')[:5]
X = Col_Data('wine_servings')[:5]
plt.bar(Y, X, width=0.4)

plt.xlabel("Country")
plt.ylabel("wine_servings")
plt.show()

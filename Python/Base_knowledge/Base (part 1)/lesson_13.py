#  task_13
my_dict = dict(Name="Nameless", Age=-1)
for key in my_dict:
    print(key, "-", my_dict[key])
name = input("Enter your name:")
age = input("Enter your age:")
my_dict["Name"] = name
my_dict["Age"] = age
for key in my_dict:
    print(key, "-", my_dict[key])
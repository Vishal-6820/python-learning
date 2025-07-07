
def hello(*args, **kwargs):
    print(args)
    print(kwargs)


# hello("Vishal", "Parmar", age=26, dob=19.98)

lst = list(("Vishal","Parmar"))
dict_val = {'age': 26, 'dob': 1998}

# hello(*lst, **dict_val)

hello("vishal","parmar","1998","CSS", age=26, pos="developer", salary=1000000)
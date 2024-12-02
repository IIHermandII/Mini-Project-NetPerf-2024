# assign list
l = ['hello', 'geek', 'have', 'a', 'geeky', 'day']

# assign string
s = 'a'

# list comprehension
compare = [i for i in l if s in l]
print(compare)

# check if string is present in list
if len(compare) > 0:
    print(f'{s} is present in the list')
else:
    print(f'{s} is not present in the list')
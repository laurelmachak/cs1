# you can put multiple data types inside lists in python
# 2 dimensional array bc there is an array inside another array
some_list = ["Laurel", 21, True, ["layers"]]

another_list = [1,2,3,4,5,6]

# print from 3rd value until end
print(another_list[2:])

# add the values of a together
print(sum(another_list))

#print every 2nd thing starting from 0 and ending at 0
print(some_list[::2])

# print every 2nd num from index 2 until index 5
print(some_list[2:5:2])

# loop thru all the characters of a string
some_name = "Steve Buscemi"
for letter in some_name:
    print(letter)

#print a list of first & last name by splitting the white space 
print(some_name.split(" "))

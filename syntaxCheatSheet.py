#this is a single line comment

'''
This is a 
block
comment
'''

#declare a variable
some_variable = "hello world"
some_other_variable = 3
the_last_one = True

#data types can change too
some_variable = 4.5


#functions

def some_function():
    #put word pass to leave empty
    pass
    
def function_with_keyword_argument(some_arg=None):
    pass

    
def func_with_multiple_args(x, y, some_keyword=True):
    pass
    
    

#control flow example

if (x == 3 and y == True):
    if x % 3 == 0:
        print("yes)
elif x == 4:
    print("elif")
    


#don't do this:
if x == True:
    pass
#do this instead:
if x:
    print("x is true")
if not x:
    print("x is false")


#for loops

for i in range(10):
    print(str(i))
    








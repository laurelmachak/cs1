import sys

#you need the previous 2 numbers to figure out the third
def fibonacci(num):
    previous = 0
    current = 1
    #now loop through
    # use _ for variables that don't matter
    # _ doesn't mean anything. bc we won't be using it
    for _ in range(num):
        new_fib = previous + current
        print(new_fib)
        previous, current = current, new_fib
        # above line is equivalent too
        # previous = current
        # current = new_fib

# fibonacci(10)

if __name__ == "__main__":
    num = sys.argv[1:]
    fibonacci(int(num[0]))

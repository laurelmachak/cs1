#data_file = open("sales_data.txt", "r")

'''
1. what are the total amount of sales contained in this
data set?
2. which city had the highest sales in February?
3. Out of the entire data set, what is the total
amount of money people have paid in cash?
4. what is the most popular payment type in Oakland
in March?
5. How mnay sales were made on 4/20, and which city had
the highest sales value?
6. what is the average sales amount for credit card
purchases?
7. how many purchases were made by baseball cards?
'''

#with multiple readline, it will keep track for you
# and print next line. keeps track for you
#print(data_file.readline())
#data_file.close()


# with open('sales_data.txt', 'w') as f:
    # f.write("Hello World!")
with open('sales_data.txt','r') as f:
    #text = f.read() #gets whole thing, all lines
    total = 0
    for line in range(10):
        remove_chars = f.readline.strip('$')
        tab_split = f.readline().split("\t")
        remove_chars = f.readLine()
    '''
    for line in f:
        line_array = line.split("\t")
        money = (line_array[3].split("$")
        cost = float(money[0])
        total += cost
    '''
    #print(total)

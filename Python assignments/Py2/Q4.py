'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

def countCurrency(amount):
     
    notes = [2000, 500, 200, 100,
               50, 20, 10, 5, 1]
                
    noteCounter = [0, 0, 0, 0, 0,
                     0, 0, 0, 0]
     
    print ("Currency Count -> ")
     
    for i, j in zip(notes, noteCounter):
        if amount >= i:
            j = amount // i
            amount = amount - j * i
            print (i ," : ", j)
 

amount = 868
countCurrency(amount)



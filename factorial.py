fh = open('factorial.txt','w')
n = int(input("Enter a number: ")) 
fact = 1 
while (n>1) : 
    fact = fact*n 
    n = n - 1 

fh.write(str(fact))
fh.close()
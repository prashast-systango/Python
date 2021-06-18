# for1
for i in range(10):
    print(i) # 0-9
print()


# for2
for i in range(2,10):
    print(i) # 2 3 4 5 6 7 8 9
else: #This is executed when the condition of for becomes false
    print("else of for2")
print() 


# for3
for i in range(1,10,2):
    print(i) # 1 3 5 7 9
print()


# for4
for i in range(1,10,2):
    print(i) # 1 3 5
    if i==5:
      break
else: # this will not be executed
     print("else of for4")
print()


#for5
for i in range(1,10,2):
    if i==5:
     continue
    print(i) # 1 3 7 9
else: # this will be executed (else with for/while is only executed on successful termination of the loop)
     print("else of for5")

i=0
while i<5:
    # print("before pass")
    pass
    i+=1
    print("after pass")

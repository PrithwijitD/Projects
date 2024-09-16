n = int(input("Enter the desired number: "))
t1 = 0
t2 = 1
nextTerm = t1 + t2
print(t1)
print(t2)
for i in range (0,n):
    t1 = t2
    t2 = nextTerm
    nextTerm = t1 + t2
    print(nextTerm)

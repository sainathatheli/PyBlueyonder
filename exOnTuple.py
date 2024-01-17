
         #     -4      -3    -2      -1
t1 = tuple(("apple","orange","mango","kiwi")) # initialize with constructor
           #0         1        2       3
t2=(10,True,"ram",10,30.0,"ram")

print("All elements")
print(t1);

print("Displaying based on index")
print(t2[0])
print(t2[1])
print(t2[2])

#t1[1]="grapes"
#print(t1)

print("index range");
print(t1[0:3]) #apple orange mango

print("gegative index range");
print(t1[-4:-1])


print("count of times the element occurs");
print(t2.count(10))



print("print using for loop")
for x in t2:
    print(x)




l1=list(t2) #this will convert the tuple into list
print("after convert to list")
print(l1)


s2=set(t2)
print(s2)
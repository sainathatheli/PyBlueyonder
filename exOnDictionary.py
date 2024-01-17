#to represent Key:value
d1={
    "emid":101,
     "ename":"raju",
      "sal":3000
}
print("Displaying elements")
print(d1)

#initialize the constructor
d2=dict(name="ramu",salary=300,address="hyd")
print("Displaying elements from d2 constructor")
print(d2)

#accessing the item using index[key]
print("Accessing the item using key")
print(d1["ename"])

print("Displaying  elementsb before add")
print(d1)

#add the element
d1[10]="ten"

print("Displaying  elementsb after add")
print(d1)




#accessing the item using get()
print("Accessing the item using get()")
print(d1.get("ename") )


#get the onlye keys 
#keys() it return in the form of list

l1=d1.keys();
print("Keys are from d1 dictionary :")
print(l1)

#get the only values
#values() it will return list

l2=d1.values();
print("values are from d1 dictionary :")
print(l2)



d2.pop("address")
print("after deleted :")
print(d2)

print("Displaying the elements from d1 using for loop :")
for x in d1:
    print(d1[x])

print("Displaying the elements from d1 (key)using for loop :")
for x in d1.keys():
    print(x)


print("Displaying the elements from d1 (values)using for loop :")
for x in d1.values():
    print(x)


print("search based on key (ename)")
for x in d1.keys():
    if x == "ename":
        print("search is found and it will return the value  ",d1[x])
        break



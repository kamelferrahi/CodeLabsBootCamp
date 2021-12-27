list =[]
for i in range(2,300,2):
    list.append(i)

print("Length of list: "+str(len(list))+"\n")

i = 0

for x in list:
    print(str(x**2)+"\n")
   

print("\n\nis 57 in the list? Answer: ",57 in list)

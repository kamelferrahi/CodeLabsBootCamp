list =[]
for i in range(2,300,2):
    list.append(i)

print("Length of list: "+str(len(list))+"\n")

i = 0

while (list[i]**2<list[len(list)-1]):
    print(list[i]**2)
    i += 1

print("\n\nis 57 in the list? Answer: ",57 in list)

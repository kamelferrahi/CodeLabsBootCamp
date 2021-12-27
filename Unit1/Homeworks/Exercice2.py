file = open("student_names.txt")
student = file.read()

file = open("student_names.txt",'w')
student = "Lionel Messi\nYoucef Belaili\nAdolf Hitler\nAbdelaziz Bouteflika\nFerrahi Kamel\n"
file.write(student)

n = 3

file = open ("student_names.txt","r")

for line in file.readlines()[0:n]:
    print(line)

file = open ("student_names.txt","r")

for line in (file.readlines() [-n:]):
    print(line)

file.close()

c = 'A'

while  (ord(c)<=ord("Z")):
    filename= c+".txt"
    file = open(filename,"w")
    c = chr(ord(c)+1);

file=open('Details.txt','r')
#print(file.read())
#file_content=file.read()
#print(file_content.upper())
#print(file.readline())
print(file.readlines())
file.close()

#style1
with open('Details.txt','r') as file:
    print(file.readlines())
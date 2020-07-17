"""
In this project to find the most used key word in the text
"""
##accesing the file
file=open("file.txt","r")
data=file.read()

##conversion of the string into list
l=data.split(" ")

countl=[]
    
##fltering the non alphabets in the list
for i in l:
    if not i.isalpha():
       l.pop(l.index(i))

#counting the presence of each element in the list
for i in l:
    count=l.count(i)
    countl.append([i,count])

#filtering out the list by removing the list having the value less than 5
countl=list(filter(lambda l: l[-1]>5 ,countl))
countl=list(filter(lambda l: l[0].isalpha() ,countl))

newlist=list(countl[0])

#filtering out the duplicate values
for i in countl[1:]:
    if i not in newlist:
        newlist.append(i)
    
#sorting based on send value of the list
newlist.pop(0)
newlist.pop(0)

def takeSecond(ele):
    return ele[-1]

#telling to sort in decending order with second element in a lis
newlist.sort(reverse=True,key=takeSecond)

for i in newlist:
    print(i)
            





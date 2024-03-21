#1. Write a Python program to read an entire text file.
'''
f=open("C:\\Users\\JaswanthReddyYamasan\\OneDrive - Xyenta Limited\\Documents\\adv join subq ans.txt","r")
print(f.read())
f.close()
'''

#2. Write a Python program to read first n lines of a file.
'''
n=int(input("No of Lines :"))
f=open("C:\\Users\\JaswanthReddyYamasan\\OneDrive - Xyenta Limited\\Documents\\adv join subq ans.txt","r")
l=f.readlines()
for i in range(0,n):
    print(l[i],end=" ")
f.close()
'''
'''
f=open("C:\\Users\\JaswanthReddyYamasan\\OneDrive - Xyenta Limited\\Documents\\adv join subq ans.txt","r")
n=int(input("Enter No of Lines :"))
lines=0
for i in f:
    if lines<n:
        print(i,end=" ")
        lines+=1
    else:
        break
f.close()

'''
#3. Write a Python program to append text to a file and display the text.
'''
f=open("C:\\Users\\JaswanthReddyYamasan\\OneDrive - Xyenta Limited\\Documents\\adv join subq ans.txt","a")
f.write("hi im appended text \n")
f.close()
f=open("C:\\Users\\JaswanthReddyYamasan\\OneDrive - Xyenta Limited\\Documents\\adv join subq ans.txt","r")
print(f.read())
f.close()
'''

#4. Write a Python program to read last n lines of a file.
'''
n=int(input("Enter no of last lines :"))
f=open("C:\\Users\\JaswanthReddyYamasan\\OneDrive - Xyenta Limited\\Documents\\adv join subq ans.txt","r")
l=f.readlines()
for i in l[len(l)-n::]:
    print(i,end=" ")
f.close()
'''

#5. Write a Python program to read a file line by line and store it into a list.
'''
f=open("C:\\Users\\JaswanthReddyYamasan\\OneDrive - Xyenta Limited\\Documents\\adv join subq ans.txt","r")
l=f.readlines()
print(l)
print(type(l))
f.close()
'''

#6. Write a Python program to count the number of lines in a text file.
'''
f=open("C:\\Users\\JaswanthReddyYamasan\\OneDrive - Xyenta Limited\\Documents\\adv join subq ans.txt","r")
l=f.readlines()
lines=len(l)
print("No of lines :",lines)
f.close()
'''

#7. Write a Python program to count the frequency of words in a file.
'''
f=open("C:\\Users\\JaswanthReddyYamasan\\OneDrive - Xyenta Limited\\Documents\\adv join subq ans.txt","r")
d = {} 
for line in f: 
	line = line.strip() 
	line = line.lower()  
	words = line.split(" ") 					
	for word in words: 
		if word in d: 
			d[word] = d[word] + 1
		else:
			d[word] = 1
for key in list(d.keys()): 
	print(key, ":", d[key])
'''

#8 Write a Python program to get the file size of a plain file.
'''
import os
c=os.path.getsize("C:\\Users\\JaswanthReddyYamasan\\OneDrive - Xyenta Limited\\Documents\\adv join subq ans.txt")
print(c," bytes")
'''
#9 Write a Python program to write a list to a file.
'''
l=['a','b','c','d','e','f']
s=''.join(l)
f=open("C:\\data\\test.txt",'w')
f.write(s)
f.close()
f=open("C:\\data\\test.txt",'r')
print(f.read())
f.close()
'''
#10. Write a Python program to copy the contents of a file to another file
'''
f=open("C:\\data\\test.txt",'r')
s=f.read()
f.close()
f=open("C:\\data\\test1.txt",'w')
f.write(s)
f.close()
f=open("C:\\data\\test1.txt",'r')
print(f.read())
f.close()
'''
#11. Write a Python program to read a random line from a file.
'''
import random
f=open("C:\\Users\\JaswanthReddyYamasan\\OneDrive - Xyenta Limited\\Documents\\adv join subq ans.txt","r")
l=f.readlines()
print(l[random.randint(0,len(l))])
'''

#12. Write a Python program to assess if a file is closed or not.
'''
f=open("C:\\Users\\JaswanthReddyYamasan\\OneDrive - Xyenta Limited\\Documents\\adv join subq ans.txt","r")
print(f.closed)
f.close()
print(f.closed)
'''



#13. Write a Python program that takes a text file as input and returns the number of words of a given text file. 
#Note: Some words can be separated by a comma with no space.
'''
f=open("C:\\Users\\JaswanthReddyYamasan\\OneDrive - Xyenta Limited\\Documents\\adv join subq ans.txt","r")
count=0
for i in f:
    for j in i.split():
        count+=1
print("No of words :",count)
f.close()
'''
        
    


#14. Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
'''
for i in range(ord('A'),ord('Z')+1):
    ch=chr(i)
    s='C:\\data\\'+ch+'.txt'
    f=open(s,'w')
    f.write(ch)
    f.close()
'''    
    





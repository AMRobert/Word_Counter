#WORD COUNTER USING PYTHON

#Reads the text file
file = open(r"file path")

Words=[]
for i in file:
    Words.append(i.split(" "))
    print(Words

          )
#Count the Number of Words
Word_Count=0
for line in Words:
    for x in line: 
        Word_Count = Word_Count + 1
print(Word_Count)

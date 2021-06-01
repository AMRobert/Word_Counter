#WORD COUNTER USING PYTHON

#Read the text file
file = open(r"file path")

Words = []
for i in file:
    Words.extend(i.split(" "))
    print(Words)

#Count the Number of Words
Word_Count=0
for x in range(len(Words)):
    Word_Count = Word_Count + 1
print(Word_Count)

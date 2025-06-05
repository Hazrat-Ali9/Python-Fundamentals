sentence ='The fox jumps over the dog'
words = sentence.split()
print(words)
print(len(words))
print(words[0])

for word in words:
    print(word.title())

line = "A lot of spaces"
sline = line.split()
print(sline)

wordswithmark = 'first;second;third'
print(wordswithmark)
print (len(wordswithmark))
words = wordswithmark.split(';')
print(words)
print(len(words))

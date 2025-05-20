fname = input("Enter file name: ")
if(fname == ""):
    fname = 'mbox-short.txt'
fopen = open(fname)
emails = list()
for line in fopen:
    # print(line)
    line = line.rstrip()
    #print(line)
    if not line.startswith('From '):continue
    words = line.split()
    # print(words)
    email = words[1]
    # print(email)
    emails.append(email)
print("The number of emails in the file: ", len(emails))
print("The whole list of the emails in the file: \n",emails,"\n")

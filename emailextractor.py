fname = input("Enter file name: ")
if(fname == ""):
    fname = 'mbox-short.txt'
fopen = open(fname)
emails = list()
senders = list()
domains = list()
for line in fopen:
    # print(line)
    line = line.rstrip()
    #print(line)
    if line.startswith('From '):
        words = line.split()
        # print(words)
        email = words[1]
        senderdomain = email.split('@')
        senders.append(senderdomain[0])
        domains.append(senderdomain[1])
        print(email)
        emails.append(email)
print("The number of emails: ", len(emails))
print("The emails: \n",emails,"\n")
print("The senders: \n", senders,"\n")
print("The domains: \n",domains,"\n")

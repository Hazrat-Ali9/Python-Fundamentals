web = ['HTML','CSS','JavaScript','Bootstrap','ReactJS','Angularjs','Python','PHP','MongoDB', 'SQL','Nodejs']

for i in range(len(web)):
    frontend = web[:6]
    backend = web[7:]
    fullstack = web[:]
print ("You are a front-end Hazrat --> ", frontend)
print ("You are a back-end Hazrat --> ",backend)
print ("You are a full-stack Hazrat --> ",fullstack)

for wblang in web:
    print("I am good at",wblang,". If you like to learn", wblang,"stayed tune. I will start tutorial about",wblang)

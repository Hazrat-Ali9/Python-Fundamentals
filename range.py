print(range(4))
company = ['NASA','Microsoft','Google','Facebook','Tesla','SpaceX',]
print (len(company))
print(range(len(company)))
for i in range(len(company)):
    if(company[i]!='BBC' and company[i]!='CNN'):
        print ("I like to work in ",company[i].title())

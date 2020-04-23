
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
action = True
lst = []
print('Welcome to The Z Search! we scrap a wikipidea page of choice for all related links.')

while action:
    search = input('Enter your target - ')
    print("Here we goo !")
    search = search.replace(" ","_")
    url = "https://en.wikipedia.org/wiki/"+search
    try:
        html = urlopen(url,context=ctx).read()
        soupObject = BeautifulSoup(html,'html.parser')

        tags = soupObject('a')
        for tag in tags:
            print(tag.get('href',None))
            lst.append(str(tag.get('href',None))+"\n")
    except:
        print("No results found :(, make sure of your target, spelling & case..etc")
    decision = input('Would you like to save the links?')
    if decision == "yes":
        filename = search.strip() +".txt"
        handle = open(filename,"w+")
        for item in lst:
            handle.write(item)
        handle.close()
        lst = []
    decision = input('Do you have other targets?')
    if decision != "yes":
        action = False
    print("Thank you for using The Z search, goooooooood bye!")
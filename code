import requests
import json
import threading
from time import sleep


email_list=[]

def addEmail(url):
    pages = requests.get(url)
    dict_text = json.loads(pages.text)
    for cel in dict_text:
        email_list.append(cel['email'])

def run(begin,end):
    for i in range(begin,end+1):
        url = "https://jsonplaceholder.typicode.com/posts/%s/comments" %i
        addEmail(url)

t1 = threading.Thread(target=run,args=(1,25,))
t2 = threading.Thread(target=run,args=(26,50,))
t3 = threading.Thread(target=run,args=(51,75,))
t4 = threading.Thread(target=run,args=(76,100,))
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()

with open("emailfile.txt", "w") as f:
    f.write(str(email_list))

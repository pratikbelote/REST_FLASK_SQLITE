
import requests

base = "http://127.0.0.1:5000/"

data = [{'name':'pank','views':23,'likes':34},
    {'name':'pratik','views':34,'likes':23},
    {'name':'anika','views':123,'likes':12},
    {'name':'antik','views':78466,'likes':9344}]

for i in range(len(data)):
    response = requests.put(base + "video/"+str(i),data[i])
    print(response.json())
input()

response = requests.delete(base + "video/1")
print(response.json())
input()

response = requests.get(base + "video/5")
print(response.json())
input()

response = requests.patch(base + "video/2",{"views":100000})
print(response.json())
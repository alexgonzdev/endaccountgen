import requests
import json

headers = {
"Accept":"application/json",
"Accept-Encoding":"gzip, deflate, br",
"Accept-Language":"en-US,en;q=0.5",
"Access-Control-Allow-Credentials":"true",
"Cache-Control":"no-cache",
"Connection":"keep-alive",
"Content-Type":"application/json; charset=UTF-8",
"Host":"launches-api.endclothing.com",
"Origin":"https://launches.endclothing.com",
"Pragma":"no-cache",
"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:74.0) Gecko/20100101 Firefox/74.0"
}

registerurl = "https://launches-api.endclothing.com/api/account"

registerpayload = {"email":"jfjwaoijoiajio@gmail.com","firstName":"xacjwdiaji","lastName":"vhdihviuwq","password":"xncihiH38","websiteId":1,"optIn":0}

session = requests.Session()

register = session.post(registerurl, json=registerpayload, headers=headers)

print(register.text)

import requests, json, urllib







# [  TEST ERROR VALUE  ]
# n = 0
# try:
#     if int(input(">>>")) == 3:
#         print("l")
#     else:
#         n += 5
# except:
#     n+=1
# print(n)







# [  GET UPDATE APP API  ]
# url = 'http://mobile-mining.tk/api/app_update/av2-2/main.py'
# r = requests.get(url, allow_redirects=True)
# open('main.py', 'wb').write(r.content)







# [  GET SETTING API  ]
# url = "http://mobile-mining.tk/api/v1/get-read-all.php"
# receive = requests.get(url)
# s = receive.json()

# i = 0
# while True:
#     if s[i]['tag_name'] == "R16":
#         print(f"cd ccminer_mmv && ./ccminer -a verus -o {s[i]['pool']} -u {s[i]['wallet']}.test -p {s[i]['password']},ID=test -t 1")
#     i+=1

# print(s[50]["tag_name"])

# try:
#     i = 0
#     while True:
#         # print(s[i]['tag_name'])
#         i+=1
#         if s[i]['tag_name'] == "R":
#             print("R16 ACTIVE")
#             break
# except:
#     print("haedddd")

# if "R16" in s[0]['tag_name']:
#     print("R16 ACTIVE")

# import os


# print(dir(os))
# print(os.getcwd())
# os.chdir("C://Users/kushwaha/PycharmProjects")


# print(os.getcwd())
# print(os.listdir())
# print(os.listdir(".idea"),"Its inside idea folder")


# os.mkdir("this")
# os.makedirs("thes/that/the/are/1/32")


# print(os.environ.get('Path'))
# print(os.path.isdir("C://Users/kushwaha/PycharmProjects"))




















                        #   request module practice


import requests
# r=requests.get("https://www.pexels.com/photo/photography-of-fall-trees-1591447/")
# print(r.headers)

# payload={'page':3,'count':32}
# r=requests.get('https://www.pexels.com/get',params=payload)
# # print(r.text)
# print(r.url)

payload={'username':'abhishek','password':'kushwaha'}
r=requests.post('https://www.blogger.com/u/0/onboarding/post',data=payload)
r_dict=r.json()
# print(r_dict())
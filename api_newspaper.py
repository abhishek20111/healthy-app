# import requests
# import json
#
# # python -m pip install pywin32
#
# def speak(str):
#     from win32com.client import Dispatch
#     speak=Dispatch("SAPI.spVoice")
#     speak.speak(str)
#
# if __name__ == '__main__':
#     speak("News for today")
#     print("News for today")
#     url="https://newsapi.org/v2/top-headlines?country=in&apiKey=21e5a42c692541039e7ad6a0f9ecb7a6"
#     news=requests.get(url).text
#     new_dict=json.loads(news)
#     arts=new_dict['articles']
#     for desc in arts:
#         speak(desc['title'])
#         print(desc['title'])
#         speak(desc['description'])
#         print(desc['description'])
#         speak("Moving to next news")
#
#
#     speak("Thanks for lisenting")









                                         # Practice

import requests
import json
from win32com.client import Dispatch

def speak(str):
    speak=Dispatch("SAPI.spVoice")
    speak.speak(str)

if __name__ == '__main__':
    speak("News for today")
    print("News for today")
    url="https://newsapi.org/v2/top-headlines?country=in&apiKey=21e5a42c692541039e7ad6a0f9ecb7a6"
    news=requests.get(url)
    new=news.text
    news_dict= json.loads(new)
    arts=news_dict['articles']
    for describe in arts:
        # print(describe(source['name'+"is name of newspaper"]))
        # speak(describe(source['name'+"is name of newspaper"]))
        print(describe['title'])
        speak(describe['title'])
        print(describe['description'])
        speak(describe['description'])
        speak("moving to next")
        print("\nmoving to next")
    speak("Thanks for lisenting")

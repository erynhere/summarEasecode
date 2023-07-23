import json
from flask import Flask, jsonify
from flask_cors import CORS
from flask import request

app = Flask(__name__)
cors = CORS(app)

from bs4 import BeautifulSoup
import requests

import openai

# import urllib.parse

# url = "https://www.tutorialspoint.com/tableau_online_training/index.asp"


@app.route('/')
def home():
    return json.dumps({'home': 'page'})

@app.route('/getText')
def getText():
    args = request.args

    # url = "https://www.tutorialspoint.com/tableau_online_training/index.asp"

    url = args.get("url")
    # urllib.parse.unquote(url)

    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    text = ""
    print(soup.title)

    # allPTags = soup.body.find(class_="content-top").find(class_="container px-xl-4 mt-4").find(class_="row").find(class_="col-sm-12 col-md-7 col-xl-8 npr").find(class_="card border mb-3").find(class_="course-descrp").find(class_="panel rounded").find(class_="course-description-content").find(class_="text").find_all("p")
    allPTags = soup.body.find(class_="flex-shrink-0").find(class_="container pb-5 pt-5 mt-5").find(class_="row").find(class_="col-lg-9 blog-main").find_all("p")
    for ptag in allPTags:
        text = text + ptag.text
    



    openai.api_key = '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'
    msgApnd = {
        "role": "system", 
        "content": "You can summarize all my information."
    }
    messages = [
        {"role": "system", "content": "You can summarize all my information."}
    ]


    message = "summarize the following text in under 70 words: " + text
    msgApnd = {"role": "user", "content": message}
    messages.append(msgApnd)
    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    reply = chat.choices[0].message.content
    print(reply)
    msgApnd = {"role": "assistant", "content": reply}
    messages.append(msgApnd)

    return json.dumps(reply)

if __name__ == '__main__':
   app.run(port="8080")



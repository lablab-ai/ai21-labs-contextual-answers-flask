from flask import Flask, request
import requests as req
import os

app = Flask(__name__)

# load form env API_KEY
API_key = os.environ.get('API_KEY')


@app.route("/")
def get_answer():

    context = request.args.getlist('context')[0]
    question =  request.args.getlist('question')[0]


    url = "https://api.ai21.com/studio/v1/experimental/answer"

    payload = {
        "context": context,
        "question": question
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": f'Bearer {API_key}'
    }

    response = req.post(url, json=payload, headers=headers)
    return response.text


app.run()
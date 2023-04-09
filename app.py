import os
import requests
import urllib3
import openai
from flask import Flask, redirect, render_template, request, url_for

# Disable insecure HTTPS request warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        move = request.form["animal"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(move),
            temperature=0.6,
        )
        # send the response to another server with the same information
        result = response.choices[0].text # example response: '\n\nWhite response move: B4'
        result = result.split(": ")[1] # example result: 'B4'
        url = f"https://localhost:8123/{result}"
        post_response = requests.post(url, data=result, verify=False)
        print("POST request sent with data:", result)
        print("Response from server:", post_response.text)

        return redirect(url_for("index", result=result))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(move):
    return f"""Provide a valid chess move of the pawns on the white side in response to the following input move from the black side, respond only with a letter and a number:

Input move on the black side: {move}"""

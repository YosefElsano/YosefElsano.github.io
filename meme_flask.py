from flask import Flask, render_template
import requests
import random

app = Flask(__name__)

def get_memes():
    url = "https://api.imgflip.com/get_memes"  # Replace with the actual API URL
    response = requests.get(url).json()

    if response.get("success"):
        memes = response.get("data", {}).get("memes", [])
        return memes
    else:
        return []

def get_random_meme(memes):
    return random.choice(memes) if memes else None

def get_joke():
    url = "https://v2.jokeapi.dev/joke/Any?type=single"
    response = requests.get(url).json()

    if response.get("type") == "single":
        return response.get("joke")
    else:
        return None

@app.route("/")
def home():
    return render_template("test.html")

@app.route("/memes")
def memes():
    return render_template("test2.html", memes=get_memes())

@app.route("/jokes")
def jokes():
    joke = get_joke()
    return render_template("test3.html", joke=joke)

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=8080)
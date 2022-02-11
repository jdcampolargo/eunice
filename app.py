import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            engine="text-davinci-001",
            prompt=generate_prompt(animal),
            temperature=0.6,
            ##max_tokens=64,
            #top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)

    # response = openai.Completion.create(
        # engine="text-davinci-001",
        # prompt="ML Tutor: I am a ML/AI language model tutor\nYou: What is a language model?\nML Tutor: A language model is a statistical model that describes the probability of a word given the previous words.\nYou: What is a statistical model?",
        # temperature=0.3,
        # max_tokens=60,
        # top_p=1.0,
        # frequency_penalty=0.5,
        # presence_penalty=0.0,
        # stop=["You:"]
    # )

def generate_prompt(animal):
    return """Answer the CS 225 Data Structures and Algorithms question:

Question: What is BFS?
Answer: A graph traversal algorithm that uses a queue to visit each node in the graph.
Question: I'm getting a seg fault. What should I do?
Answer: Make sure you have the correct version of the CS225 library.
Question: I thought operator= is a must when implementing iterators. If not how can you assign one iterator to another when iterating? say for(list<int>::iterator it = mylist.begin(); it != mylist.end(), it++)
Answer: It is not. I should have pulled the iterator stuff from the practice exam. What is required of an iterator is operator++(), operator*, and operator!=.
Question: {}
Answer:""".format(
        animal.capitalize()
    )

from flask import Flask, render_template, Blueprint


talk = Blueprint(
    "talk",
    __name__,
    template_folder="templates",
    static_folder="static",
)


@talk.route("/")
def index():
    return render_template("talk/index.html")

@talk.route("/friends")
def friends():
    return render_template("talk/friends.html")


@talk.route("/chats")
def chats():
    return render_template("talk/chats.html")

@talk.route("/chat")
def chat():
    return render_template("talk/chat.html")

@talk.route("/chat/data")
def data():
    pass

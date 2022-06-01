"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html", title = "Hi There!")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("player")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment,
                           title = "Play Game?")


@app.route("/game")
def show_madlib_form():

    player = request.args.get("player")

    answer = request.args.get("option")

    if answer == "no":
        return render_template("goodbye.html", title = "Goodbye!", player=player)

    else:
        return render_template("game.html", title = "Madlib Form", player=player)
    

@app.route("/madlib")
def show_madlib():
    color = request.args.get("color")
    noun = request.args.get("noun")
    person = request.args.get("person")
    adjective = request.args.get("adjective")
    return render_template("madlib.html", color=color, noun=noun, person=person, adjective=adjective)



if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")

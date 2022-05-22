from flask import Flask
import random

GIPHY_ROOT = 'https://media.giphy.com/media/'
GIPHY_SUFFIX = '/giphy.gif'
GIF_FOR_NUMBER = {
    '0': 'hiTLhDX1ni6kg',
    '1': 'Ntk9jRGOmfyi3FtqTA',
    '2': 'S5f8queNOCP33HFWw7',
    '3': 'l0HlIZNLEvJXVQBgY',
    '4': 'gHblD3xO087UGnpitk',
    '5': 'LnEOfj24TFB5QYqnmH',
    '6': 'y4y2tPp5damibthJmy',
    '7': 'l378atCG9uQQa1Fy8',
    '8': 'uloqNVF6WziqUY41v4',
    '9': 'teH5FYeHPe6vZ72qhs',
}
NUMBER_TO_MATCH = str(random.randint(0, 9))

app = Flask(__name__)
print(__name__)


def make_heading(function):
    def wrapper():
        print(NUMBER_TO_MATCH)
        return f"<h1>{function()}</h1>"
    return wrapper


def display_image(function):
    def wrapper(**kwargs):
        num = function(kwargs['number'])
        content = f"<img src={GIPHY_ROOT}{GIF_FOR_NUMBER[num]}{GIPHY_SUFFIX}><br>"
        if num > NUMBER_TO_MATCH:
            content += f"<h1 style='color: red'>TOO HIGH, try again!</h1>"
        elif num < NUMBER_TO_MATCH:
            content += f"<h1 style='color: blue'>TOO LOW, try again!</h1>"
        else:
            content += f"<h1 style='color: green'>YOU GUESSED IT!</h1>"
        return content
    wrapper.__name__ = function.__name__
    return wrapper


@app.route("/")
@make_heading
def guess_a_number():
    return "Guess a number between 0 and 9"


@app.route("/<number>")
@display_image
def your_number(number):
    return number

if __name__ == "__main__":
    app.run(debug=True)

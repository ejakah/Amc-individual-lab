from flask import Flask, request, render_template
import socket
import random

app = Flask(__name__)


# List of recognized colors
recognized_colors = ['aqua', 'blue', 'green', 'red', 'yellow']

# Define your welcome message and group members' names here
welcome_message = "Winter Semester 2023/2024 AMC-LAB Project"
member1_name = "Md Hazrat Ali"
member2_name = "Ejike Patrick Aka"

def random_color():
    return random.choice(recognized_colors)

@app.route('/')
def index():
    # Choose random color for text
    text_color = random_color()

    # Choose a random color for the background
    background_color = random_color()

    return render_template('index.html', text_color=text_color, background_color=background_color, welcome_message=welcome_message, member1_name=member1_name, member2_name=member2_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

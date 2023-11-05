from flask import Flask, send_file, render_template, request, redirect, session, send_from_directory

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/maps')
def maps():
    return render_template('maps.html')

@app.route('/game')
def game():
    return render_template('game.html')


if __name__ == '__main__':
   app.run()
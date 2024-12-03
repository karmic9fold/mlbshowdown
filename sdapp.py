from flask import Flask, render_template, jsonify
from mlbsd_game import MLB_Showdown

app = Flask(__name__)

# Initialize the game
game = MLB_Showdown()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/play_game', methods=['GET'])
def play_game():
    while game.scoreboard.inning < 9:
        MLB_Showdown.away_inning()
        if game.scoreboard.inning > 8.5:
            if game.scoreboard.home_score > game.scoreboard.away_score:
                break
            else:
                MLB_Showdown.home_extra_inning()
        else:
            MLB_Showdown.home_inning()
    while game.scoreboard.home_score == game.scoreboard.away_score:
        MLB_Showdown.away_inning()
        MLB_Showdown.home_extra_inning()
        if game.scoreboard.home_score != game.scoreboard.away_score:
            break
    return jsonify(game.scoreboard.display_final())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

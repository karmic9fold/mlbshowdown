from flask import Flask, render_template, jsonify
from mlbsd_game import MLB_Showdown
from time import sleep
from home_team import home_lineup as HL, home_pitching_staff as HPS
from away_team import away_lineup as AL, away_pitching_staff as APS
from mlb_scoreboard import Scoreboard as SB
from at_bat import At_Bat as AB
from inning import Inning

app = Flask(__name__)

# Initialize the game
game = MLB_Showdown()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/play_game', methods=['GET'])
def play_game():
    mlb_game = MLB_Showdown()  # Create a new game instance
    while mlb_game.scoreboard.inning < 9:
        mlb_game.away_inning()
        if mlb_game.scoreboard.inning > 8.5:
            if mlb_game.scoreboard.home_score > mlb_game.scoreboard.away_score:
                break
            else:
                mlb_game.home_extra_inning()
        else:
            mlb_game.home_inning()
    while mlb_game.scoreboard.home_score == mlb_game.scoreboard.away_score:
        mlb_game.away_inning()
        mlb_game.home_extra_inning()
        if mlb_game.scoreboard.home_score != mlb_game.scoreboard.away_score:
            break
    return jsonify({"final_score": mlb_game.scoreboard.display_final()})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

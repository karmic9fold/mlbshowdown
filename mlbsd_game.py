from random import randint
from time import sleep
from home_team import home_lineup as HL, home_pitching_staff as HPS
from away_team import away_lineup as AL, away_pitching_staff as APS
from mlb_scoreboard import Scoreboard as SB
from at_bat import At_Bat as AB
from inning import Inning

class MLB_Showdown:

    def __init__(self):
        self.scoreboard = SB(self)
        self.inning = Inning(self)
        self.outs = 0
        self.HL = HL
        self.HPS = HPS
        self.AL = AL
        self.APS = APS

    def away_inning(self):
        self.scoreboard.display_scoreboard()
        while self.inning.outs < 3:
            batter = self.AL.pop(0)
            pitcher = self.HPS[0]
            ab = AB(pitcher, batter, self)
            ab.check_advantage()
            ab.swing_result()
            self.AL.append(batter)
            sleep(1)
        self.scoreboard.update_away_score()
        ab.away_inning_pitched()  # Track innings pitched
        self.inning.outs = 0  # Reset the outs count
        self.inning.first = 0  # Reset first base
        self.inning.second = 0  # Reset second base
        self.inning.third = 0  # Reset third base
        self.inning.runs = 0  # Reset runs scored
        self.scoreboard.update_inning()
        sleep(2.5)

            

    def home_inning(self):
        self.scoreboard.display_scoreboard()
        while self.inning.outs < 3:
                batter = self.HL.pop(0)
                pitcher = self.APS[0]
                ab = AB(pitcher, batter, self)
                ab.check_advantage()
                ab.swing_result()
                self.HL.append(batter)
                sleep(1)
        self.scoreboard.update_home_score()
        ab.home_inning_pitched()  # Track innings pitched
        self.inning.outs = 0  # Reset the outs count
        self.inning.first = 0  # Reset first base
        self.inning.second = 0  # Reset second base
        self.inning.third = 0  # Reset third base
        self.inning.runs = 0  # Reset runs scored
        self.scoreboard.update_inning()
        sleep(2.5)

    def home_extra_inning(self):
        self.scoreboard.display_scoreboard()
        while self.inning.outs < 3:
            if self.scoreboard.home_score > self.scoreboard.away_score:
                break
            else:
                batter = self.HL.pop(0)
                pitcher = self.APS[0]
                ab = AB(pitcher, batter, self)
                ab.check_advantage()
                ab.swing_result()
                self.HL.append(batter)
                self.scoreboard.check_game_over()
                sleep(1)
        self.scoreboard.update_extra_home_score()
        ab.home_inning_pitched()
        self.inning.outs = 0  # Reset the outs count
        self.inning.first = 0  # Reset first base
        self.inning.second = 0  # Reset second base
        self.inning.third = 0  # Reset third base
        self.inning.runs = 0  # Reset runs scored
        self.scoreboard.update_inning()
        sleep(2.5)
        
# Game Loop
# mlb_game = MLB_Showdown()
# i = mlb_game.inning
# sb = mlb_game.scoreboard
# while sb.inning < 9:
#     MLB_Showdown.away_inning()
#     if sb.inning > 8.5:
#         if sb.home_score > sb.away_score:
#             break
#         else:
#             MLB_Showdown.home_extra_inning()
#     else:
#         MLB_Showdown.home_inning()
# while sb.home_score == sb.away_score:
#     MLB_Showdown.away_inning()
#     MLB_Showdown.home_extra_inning()
#     if sb.home_score != sb.away_score:
#         break
# sb.display_final()



    









# mysite
Summary
----------

BasketBall Mgmt System : a management system to monitor games statistics and rankings of a recent tournament.
Inspired from following sources 

https://docs.djangoproject.com/en/3.1/intro/
https://github.com/rajhiren/django-bms


Backend Development 
-------------------

Tools/Tehnologies used: 
- Python (3.1 latest stable version)
    -Faker
    -Crispy Forms
- Django
- Sqlite
- git




Number of Teams : 16 teams  > 8 > 1

A Team - coach + 10 players

Users - The League Admin, Coach, Player.


functions 
----------

login  (site)       
logout (Site)
view Scoreboard - list games and final results 
 - games
 - final scores
 - brakdown of progression to winner stage
view Team 
 - Show plyer profile
   player’s name, height, average score, and the number of games he participated in. 
  - showPlayerWith90Percentile() : Show Players with 90 percentiles                  - Only for Coach 


view  stats : for Admin
  - #userLoggedIn

View Site Statistics : showSiteStatistics() : for Admin
  user #timesVisited,#timeSpentPerUser , #currentLoggedInUsers

View Team Stat : for Admin

 PGSnipe
---------

PGSnipe is a command line tool for snipping Pokemon in Pokemon Go.


 Requirements
--------------
- Python 2.7
- virtualenv
- pip
- git


 Instructions
--------------
- Clone the git: git clone https://github.com/rawgni/pgsnipe
- Go into the new directory: cd pgsnipe
- Install virtualenv and activate it
- Run ```pip install -r requirements.txt```
- Run ```python snipe.py``` with the required parameters


 Example
---------

```
(pgsnipe) pgsnipe git:(master) ✗ python snipe.py -a ptc -u xxxx -p xxxx -e encrypt.so -g "xxx" -l "xxx"
... debugging info...
Location ->  34.014583, -118.496477
Name ->  Hitmonlee
Line 83,snipe.py- 2016-08-16 23:28:37,004- INFO- Found.. HITMONLEE
Line 39,snipe.py- 2016-08-16 23:28:37,614- INFO- Using Razz Berry
Line 50,snipe.py- 2016-08-16 23:28:37,855- INFO- Using GREAT_BALL
Line 39,snipe.py- 2016-08-16 23:28:41,225- INFO- Using Razz Berry
Line 50,snipe.py- 2016-08-16 23:28:41,467- INFO- Using GREAT_BALL
Line 55,snipe.py- 2016-08-16 23:28:44,794- INFO- Success. Caught a HITMONLEE
Line 58,snipe.py- 2016-08-16 23:28:45,052- INFO- id: xxx
pokemon_id: HITMONLEE
cp: 288
stamina: 40
stamina_max: 40
move_1: ROCK_SMASH_FAST
move_2: LOW_SWEEP
height_m: 1.46379435062
weight_kg: 47.6890029907
individual_attack: 15
individual_defense: 11
individual_stamina: 15
cp_multiplier: 0.349212676287
pokeball: ITEM_GREAT_BALL
...
```
 
 Thanks
--------
- https://github.com/rubenvereecken/pokemongo-api for the API
- https://github.com/earshel/PokeyPySnipe cool UI

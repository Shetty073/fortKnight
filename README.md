# fortKnight-bot

### What is this?
*A discord bot for [Fortnite Battle Royale](https://www.epicgames.com/fortnite/en-US/buy-now/battle-royale) players* 

### How to use this?
*You can deploy this and run from your pc. See "requirements" and "How to run?" sections for more details*

### Why did you create this?
*So that there would be less fight between the players regarding where to go/land 😉. Just kidding, I created this because I like python and always wanted to write a bot*

### How does it work?
##### Just '.ask' for help 😉
![Help Menu](https://i.imgur.com/TtHI6LO.png)
##### The random location list command
![ft command](https://i.imgur.com/c7q7Wzg.png)
##### Get player statistics like total wins, last match played, etc
![st command](https://i.imgur.com/phh8VEK.png)
##### Get the latest Fortnite server status
![Server status](https://i.imgur.com/W9BM0vn.png)
##### Get latest in-game shop items with cost images
![Shop items](https://i.imgur.com/rnx40VV.png)
##### Get the list of in-game weapons
![Weapons list](https://i.imgur.com/EYG1HPf.png)
##### Get the stats of a particular weapon
![Weapon stat](https://i.imgur.com/fw2nWWC.png)
##### Get latest tweets from [FortniteGame](https://twitter.com/FortniteGame)
![tweet's from Fortnite official](https://i.imgur.com/r9uHLLP.png)
##### Get information for a particular Movie/TV Series
![Movie/TV series ](https://i.imgur.com/aOWEVGd.png)
##### Exception handling done with expected results
![Exception handling](https://i.imgur.com/Wy6MUFH.png)
##### Toss a coin
![toss a coin](https://i.imgur.com/fisjA1v.png)
##### Roll a die
![roll a die](https://i.imgur.com/l2NkgK4.png)
##### Bored waiting for a member to leave a squad, play Rock, Paper, Scissor with the bot till then
![rps game command](https://i.imgur.com/Vn1g9cp.png)
##### Say Good Night to the bot He will appreciate it 😂
![gn to bot](https://i.imgur.com/px5od8Y.png)

### Commands
* `.ft` - This will geta random fortnite game location name for the players to decide to jump to
* `.toss` - Toss a coin
* `.roll` - Roll a die
* `.tweet` - Grab the last three tweets by Fortnite's [official twitter](https://twitter.com/FortniteGame)
* `.rps` - Play rock, paper, scissor with the bot
* `gn` - Say good night to the bot
* `st` - Get the fortnite player data. Usage: `.st "epic_username"` Version 1.0
* `.svr` - Get fortnite server status
* `.shp` - Get today's items in item shop
* `.wlist` - Get list of all available in-game weapons
* `.wstat` - Get details of fortnite battle royale in-game weapons by specifying name and rarity. Usage: `.wstat legendary scar` or `.wstat epic hand cannon`
* `.mv` - Get movie/TV series information. Usage: `.mv` 'movie name' for e.g. `.mv the mentalist`

### Version:

## 1.0.0:
* '.st' command added with other improvements
## 1.1.0:
* `.svr` command added
* `.shp` command added with some minor improvements
## 2.0.0:
* `.wlist` command added
* `.wstat` command added
* Major improvements made and exceptions handled properly
* Officially not a work in progress anymore
* `.mv` command added

<br/><br/>

### Requirements
* Python 3.6.5 or newer
* Important ones are discord.py and python-twitter (you can check requirements.txt)

<br/><br/><br/><br/>

### How to run?
* `git clone` or download this project as .zip
* Extract and open the file "fortKnight.py" in a code/text editor
* In the last line `bot.run("secret goes here")` replace the text `secret goes here` with your discord app token
  * Above step is important as the token is bots password and without it the bot will not log in and will be unusable
* Once done save and close the file
* Open commandline go to the folder where "fortKnight.py" is located then type and enter `python fortKnight.py`(python3 for Linux users) to run this bot
* Close the commandline to make the bot go offline
* For help on discord bot account and invitation refer [this](https://github.com/Chikachi/DiscordIntegration/wiki/How-to-get-a-token-and-channel-ID-for-Discord)*
* Since this bot is revamped and work is being done from a fresh start you will need a free [twitter app account](https://apps.twitter.com/) so that you can get the four needed keys for the new tweet function to work

<br/><br/><br/><br/>

Ignore the file named "Procfile" it is not required to run the bot from local machine.

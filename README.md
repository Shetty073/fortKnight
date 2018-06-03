# fortKnight-bot

### What is this?
*A discord bot for [Fortnite Battle Royale](https://www.epicgames.com/fortnite/en-US/buy-now/battle-royale) players* 

### How to use this?
*You can deploy this and run from your pc. See "requirements" and "How to run?" sections for more details*

### Why did you create this?
*So that there would be less fight between the players regarding where to go/land 😉. Just kidding, I created this because I like python and always wanted to write a bot*

### How does it work?
![Bot in Action](https://i.imgur.com/HJEEjqB.png)

<br/><br/><br/><br/>

### Requirements
* Python 3.5.x or newer
* Important ones are discord.py and python-twitter (you can check requirements.txt)

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

### Commands
`.ft` - This will geta random fortnite game location name for the players to decide to jump to
`.toss` - Toss a coin
`.roll` - Roll a die
`.tweet` - Grab the last three tweets by Fortnite's [official twitter](https://twitter.com/FortniteGame)



Ignore the file named "Procfile" it is not required to run the bot from local machine.

This is a Work In Progress

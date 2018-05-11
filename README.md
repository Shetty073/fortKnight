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
* discord.py 0.16.6 or newer
* & other modules as listed in requirements.txt

### How to run?
* `git clone` or download this project as .zip
* Extract and open the file "fortKnight.py" in a code/text editor
* In the last line `bot.run("secret goes here")` replace the text `secret goes here` with your discord app token
  * Above step is important as the token is bots password and without it the bot will not log in and will be unusable
* Once done save and close the file
* Open commandline go to the folder where "fortKnight.py" is located then type and enter `python fortKnight.py`(python3 for Linux users) to run this bot
* Close the commandline to make the bot go offline
* For help on discord bot account and invitation refer [this](https://github.com/Chikachi/DiscordIntegration/wiki/How-to-get-a-token-and-channel-ID-for-Discord)*

<br/><br/><br/><br/>

## Imporvements:

### New command added:
##### `.st` - *gives the status of fortnite servers*
##### ![Bot in action](https://i.imgur.com/o3Msw3X.png)

### Version 1.0
#### Features:
* `.ft` - Shows a random location on battle royale map for players to land on
* `.st` - Shows the status of Fortnite Battle Royale Servers

### Version 1.1
#### Features:
* `.ask` - Help menu added (has problems)
* `.list` - Shows the list of in-game shootable wespons along with their respective rarity
* `.wd` - Provides the details of weapons (Use: .wd "name of the wespon" "rarity")

#### What next?
* Major improvements/fixes (help menu and .wd result format)
* New features


Ignore the file named "Procfile" it is not required to run the bot from local machine.

This is a Work In Progress

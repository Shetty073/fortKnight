#Fortknight-bot by Shetty073

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import discord.client
import asyncio
import random
from bs4 import BeautifulSoup as bs
import requests as req
import string

#status grabber code starts
page = req.get("https://lightswitch-public-service-prod06.ol.epicgames.com/lightswitch/api/service/bulk/status?serviceId=Fortnite")
soup = bs(page.content, "html.parser")
status = soup.prettify()
update = "UP"
#status grabber code ends

#weapons list
weapon_st = "Following is a list of all the \"available weapons\" in the game along with their \"rarity\"::"
weapon_list = " Scar: legendary, epic \n Scoped Rifle: epic, rare \n M4: rare, uncommon, common \n Burst Rifle: uncommon, common, rare \n Bolt-Action Sniper: epic, legendary, rare \n Auto Sniper: legendary, epic \n Crossbow: rare, epic \n Hunting Rifle: rare, uncommon \n Pump Shotgun: rare, uncommon \n Heavy Shotgun: epic, legendary \n Tactical Shotgun: common, uncommon, rare \n Minigun: legendary, epic \n Tactical Submachine Gun: epic, rare, uncommon \n Silenced SMG: common, uncommon, rare \n Silenced Pistol: legendary, epic \n Hand Cannon: epic, legendary \n Pistol: rare, uncommon, common \n Revolver: common, uncommon, rare \n Rocket Launcher: legendary, epic, rare \n Guided Missile: epic, legendary \n Grenade Launcher: rare, epic, legendary \n Grenade: common \n Light Machine Gun: epic, rare"

bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
	print("Let the battle begin")

@bot.command(pass_context=True)
async def ft():
	places = ["Lucky Landing", "Factories near Dusty Depot", "Motel", "Somewhere between Retail, Jail and Factories", "Football Ground", "Between Shifty and Flush", "Container", "Jail", "North of Wailing Woods", "Anarchy Acres", "Dusty Depot", "Fatal Fields", "Flush Factory", "Greasy Grove", "Haunted Hills", "Junk Junction", "Lonely Lodge", "Loot Lake", "Moisty Mire", "Pleasant Park", "Retail Row", "Salty Springs", "Shifty Shafts", "Snobby Shores", "Tilted Towers", "Tomato Town", "Wailing Woods"]
	await bot.say(random.choice(places))

#status grabber command code
@bot.command(pass_context=True)
async def st():
	if update in status:
		await bot.say("Grab your guns! 'cause Fortnite servers are UP and running!")
	else:
		await bot.say("Fortnite servers are DOWN!")

#weapon list command
@bot.command(pass_context=True)
async def list():
	await bot.say(weapon_st)
	await bot.say(weapon_list)

#weapon details code starts here
@bot.command(pass_context=True)
async def wd():
	read = req.get("https://www.fortnitechests.info/api/weapons")
	rawData = read.json()
	nameOfWeapon = input("Weapon Name: ")
	rarityOfTheWeapon = input("Weapon rarity: ")
	for i in rawData:
		if i["name"] == nameOfWeapon and i["rarity"] == rarityOfTheWeapon:
			await bot.say("Weapon Type:", i["type"])
			await bot.say("Weapon Rarity:", i["rarity"])
			await bot.say("Weapon Damage:", i["damage"])
			await bot.say("Weapon Headshot Damage:", i["headshotdamage"])
			await bot.say("Weapon Damage per Second:", i["dps"])
			await bot.say("Weapon Rate of Fire:", i["firerate"])
			await bot.say("Weapon Magazine Size:", i["magsize"])
			await bot.say("Weapon Range:", i["range"])
			await bot.say("Weapon Durability:", i["durability"])
			await bot.say("Weapon Reloadtime:", i["reloadtime"])
			await bot.say("Weapon Ammocost:", i["ammocost"])
			await bot.say("Weapon Impact:", i["impact"])
			break

@bot.command(pass_context=True)
async def ask():
	await bot.say(".ft: Get a random location to drop-into ingame")
	await bot.say(".st: Get the latest fortnite server status")
	await bot.say(".list: Gives you the list of all available weapons along with rarity")
	await bot.say(".wd: Gives all details of the specified weapon \nTo use this command type .wd \"name of the weapon\" and \"rarity of the weapon\" and press enter")
	await bot.say("New features incoming....till then enjoy!")

bot.run("secret goes here")

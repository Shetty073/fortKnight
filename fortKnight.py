#Fortknight-bot by Shetty073/AlphaSierra
#version: 1.1

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
@bot.command()
async def wd(nameOfWeapon, rarityOfTheWeapon):
	read = req.get("https://www.fortnitechests.info/api/weapons")
	rawData = read.json()
	for i in rawData:
		if i["name"] == nameOfWeapon and i["rarity"] == rarityOfTheWeapon:
			weaponType = "Weapon Type:", i["type"]
			weaponRarity = "Weapon Rarity:", i["rarity"]
			weaponDamage = "Weapon Damage:", i["damage"]
			weaponHeadDamage = "Weapon Headshot Damage:", i["headshotdamage"]
			weaponDpS = "Weapon Damage per Second:", i["dps"]
			weaponRoF = "Weapon Rate of Fire:", i["firerate"]
			weaponMagSize = "Weapon Magazine Size:", i["magsize"]
			weaponRange = "Weapon Range:", i["range"]
			weaponDurable = "Weapon Durability:", i["durability"]
			weaponReload = "Weapon Reloadtime:", i["reloadtime"]
			weaponAmmocost = "Weapon Ammocost:", i["ammocost"]
			weaponImpact = "Weapon Impact:", i["impact"]
			final = weaponType + weaponRarity + weaponDamage + weaponHeadDamage + weaponDpS + weaponRoF + weaponMagSize + weaponRange + weaponDurable + weaponReload + weaponAmmocost + weaponImpact
			await bot.say(final)
			break

@bot.command()
async def ask(what):
	if what == "":
		await bot.say(".ft: Get a random location to drop-into ingame")
		await bot.say(".st: Get the latest fortnite server status")
		await bot.say(".list: Gives you the list of all available weapons along with rarity")
		await bot.say(".wd: Gives all details of the specified weapon \nTo use this command type .wd \"name of the weapon\" and \"rarity of the weapon\" and press enter")
		await bot.say("This is a Work In Progress. New features/improvements incoming....till then enjoy!")
	elif what == "wd":
		await bot.say("How to use the .wd command: \n.wd Scar epic => gives the information on \"epic Scar\" \nIf the name of the weapon is made up of two words the use \"\" inverted comas to write it.\nFor example .wd \"Scoped Rifle\" rare\nIf you need any more assistance contact AlphaSierra")

bot.run("secret goes here")

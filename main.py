import discord
from discord.ext import commands
import asyncio
import os

token=os.getenv("DCtoken")

#  設定bot權限
intents=discord.Intents.all()#  設定權限：所有權限
DCbot=commands.Bot(command_prefix="/",intents=intents)
#  command_prefix：指令前綴，例如：/help（這和discord的/ command 不一樣）
#  intents：權限，例如：發送訊息、管理訊息、管理伺服器、管理使用者等等，視需要而定

@DCbot.event
async def on_ready():#  當DCbot啟動
	print(f"DCbot已啟動，目前登入身分為：{DCbot.user.name}")

async def load_file():#  cogs檔案讀取
	for fname in os.listdir("./cogs"):
		try:
			if fname.endswith(".py"):
				await DCbot.load_extension(f"cogs.{fname[:-3]}")#  載入cogs
			pass
		except:
			print(f"載入./cogs{fname}時發生錯誤")
			pass

async def main(DCbot):
	await load_file()

asyncio.run(main(DCbot))#  執行bot
DCbot.run(token)


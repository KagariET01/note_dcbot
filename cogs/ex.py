enable=True

import discord
from discord.ext import commands
from discord import app_commands#  增加DC / 指令支援

class cog_ex(commands.Cog):
	bot:commands.Bot
	def __init__(self,bot:commands.Bot):
		#  self: 代表這個class，可以使用class.n的方式呼叫class內的變數
		#  bot: 這個class的變數，代表DCbot
		#  commands.Bot: 代表DCbot的class
		self.bot=bot

	@commands.Cog.listener()
	async def on_ready(self):
		print("如果你看到這則訊息，代表cogs/ex.py成功被載入")

async def setup(bot:commands.Bot):
	#  將Cog加入Bot中
	if(not enable):
		return	
	await bot.add_cog(cog_ex(bot))
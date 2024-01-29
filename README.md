# 基本樣板
## 單檔案架構
`main.py`
```py
import discord
from discord.ext import commands
import asyncio

token=os.getenv("DCtoken")
logchannel=int(os.getenv("logchannel"))

#  設定bot權限
intents=discord.Intents.all()#  設定權限：所有權限
DCbot=commands.Bot(command_prefix="/",intents=intents)
#  command_prefix：指令前綴，例如：/help（這和discord的/ command 不一樣）
#  intents：權限，例如：發送訊息、管理訊息、管理伺服器、管理使用者等等，視需要而定

@DCbot.event
async def on_ready():#  當DCbot啟動
	slash=await DCbot.tree.sync()#  將 / 指令同步到DC

async def load_file():#  cogs檔案架構
	for fname in os.listdir("./cogs"):
		try:
			if fname.endswith(".py"):
				await DCbot.load_extension(f"cogs.{fname[:-3]}")#  載入cogs
			pass
		except:
			print(f"載入./cogs{fname}時發生錯誤")
			pass

async def main():
	async with DCbot:
		await load_file()
		await DCbot.start(token)

asyncio.run(main())#  執行bot
```

## cogs檔案架構
p.s. cogs檔案不能單獨存在，必須使用main.py來驅動（範例中的main.py有驅動cogs檔案的程式碼，可以直接使用）
p.s. 僅管是不同的cog檔，class名稱也不能重複
`cogs/filename.py`
```py
enable=False#  debug用，設定為True時，會載入這個cogs
cogname="cogname"#  debug用，可用來檢測是哪個cogs出錯ㄡ

import discord
from discord.ext import commands
from discord import app_commands#  增加DC / 指令支援

class classname(commands.Cog):
	bot:commands.Bot
	def __init__(self,bot:commands.Bot):
		self.bot=bot

	#  write your code here
	@commands.Cog.listener()
	async def on_ready(self):#  當DCbot啟動
		pass

async def setup(bot:commands.Bot):#  cogs被載入時，會執行這個函式
	if(not enable):
		return	
	await bot.add_cog(classname(bot))
```

# event 事件
## on_ready 當DCbot啟動成功
`main.py`
```py
@DCbot.event
async def on_ready():#  當DCbot啟動
	#  command here
	pass
```
`cogs/filename.py`
```py
@commands.Cog.listener()
async def on_ready(self):#  當DCbot啟動
	#  command here
	pass
```




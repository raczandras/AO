from discord.ext import tasks
import discord
import os.path

token = ""
imagepath = ""
channelnum = 0

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def setup_hook(self) -> None:
        self.my_background_task.start()

    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print("------")

    @tasks.loop(seconds=60)  
    async def my_background_task(self):
        if os.path.isfile(imagepath) :
            channel = self.get_channel(channelnum)  
            await channel.send("A strategic point has been created!",file=discord.File(imagepath))
            os.remove(imagepath)

    @my_background_task.before_loop
    async def before_my_task(self):
        await self.wait_until_ready()  


client = MyClient(intents=discord.Intents.default())
client.run(token)

from discord.ext import commands 
TOKEN = " 

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
  print(f'{bot.user} Onnistuneesti kirjauduttu sisaan!')
  
  
  @bot.event
  async def on_messsage(message):
    if message.author == bot.user:
      return
    
    if message.content == 'hello':
      await message.channel.send(f'Hi {message.author}')
      if message.content == 'bye':
        await message.channel.send(f'Goodbye {message.author}')
        
        
        
        await bot.process_commands(message)
  
  
  
  @bot.commands()
  async def square(ctx, arg):
    print(arg)
    await ctx.send(int(arg) ** 2)
    
    @bot.commands()
    async def scrabblepoints(ctx, arg):
      score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}
      points = 0
      for c in arg:
        points += score[c]
         await ctx.send(points)
  
  
  bot.run(TOKEN)

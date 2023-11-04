import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='^', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Здравствуйте! Я  {bot.user} и я обьясню вам как долго разлагается какой-либо материал.')

@bot.command()
async def bottle(ctx):
    await ctx.send("бутылка разлагается от 100 до 200 лет")

@bot.command()
async def paper(ctx):
    await ctx.send("бумага разлагается несколько месяцев")

@bot.command()
async def glass(ctx):
    await ctx.send("Стекло разлагается около тысячи лет")

@bot.command()
async def paperboard(ctx):
    await ctx.send("Картон разлагается за 1-2 месяца")

@bot.command()
async def WhatIf(ctx):
    await ctx.send("Брошенный в природе мусор разлагается образуя Метан. Образование метана не может контролироваться, он постоянно поступает в атмосферу и часто самовоспламеняется ")

@bot.command()
async def brick(ctx):
    await ctx.send("Кирпичи разлагаются до 100 лет")

@bot.command()
async def batteries(ctx):
    await ctx.send("Батарейки разлагаются 200 лет")


@bot.command()
async def Why(ctx):
    await ctx.send("Зачем я создан? Я создан для того, чтобы помогать незнающим людям и говорить доступную информацию чтобы люди знали что выкинуть всякие бутылки в урну это прекрасное действие а выкинуть эту же бутылку на улице это сильный вред всеё природе")


bot.run("")

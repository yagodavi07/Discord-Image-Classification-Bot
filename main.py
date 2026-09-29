import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá, eu sou o {bot.user}!')

@bot.command()
async def heh(ctx, count_heh=5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url

            await attachment.save(f"./{attachment.filename}")

            resultado = get_class(
                model_path="./keras_model.h5",
                labels_path="labels.txt",
                image_path=f"./{attachment.filename}"
            )

            await ctx.send(resultado)
    else:
        await ctx.send("You forgot to upload the image :(")

bot.run("COLOQUE_SEU_NOVO_TOKEN_AQUI")

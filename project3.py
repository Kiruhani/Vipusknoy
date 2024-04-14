import random
import time
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def привет(ctx):
    await ctx.send(f'Привет! Я бот который поможет избежать глобального потепления!')

@bot.command()
async def команды(ctx):
    await ctx.send(f'''1./презентация-отпровляю презентацию
2./привет-что я делаю
3./пароль-выдаю рандомний пароль
4./совет-выдаю совет как избежать потепления
5./инфа-выдаю статью с информацыей о потеплении
6./мем-кидаю мем чтобы розбавить обстановку
7./видео-видео о защите природы
8./назовичисло-рандомное число''')
    
@bot.command()
async def презентация(ctx):
    lst = [
        'https://studfile.net/preview/16447678/'
    ]
    p = random.choice(lst)
    await ctx.send(p)


@bot.command()
async def совет(ctx):
    help = [
        'Экономьте энергию дома,значительная часть электричества и тепла вырабатывается с использованием угля, нефти и газа', 'Ходите пешком, ездите на велосипеде или пользуйтесь общественным транспортом потомучто дороги мира заполонили автомобили, большинство из которых работают на дизельном топливе или бензине', 'Употребляйте больше овощей употребляя больше овощей, фруктов, цельнозерновых продуктов, бобовых, орехов и семян, и меньше мяса и молочных продуктов, можно значительно снизить свое воздействие на окружающую среду.'
    ]
    y = random.choice(help)
    await ctx.send(y)

@bot.command()
async def мем(ctx):
    mem = [
        'image\\5.png', 'image\\6.jfif', 'image\\7.jfif', 'image\\8.jpg', 'image\\9.jfif', 'image\\10.jpg', 'image\\1663080501142412172.jpg'
    ]
    i = discord.File(random.choice(mem))
    await ctx.send(file=i)
    time.sleep(5)
    await ctx.send('Тебе понравился мем?')

@bot.command()
async def да(ctx):
    await ctx.send(f'Круто мне тоже')

@bot.command()
async def нет(ctx):
    await ctx.send(f'Жалко ну нечего я еще расмешу тебя')



@bot.command()
async def инфа(ctx):
    await ctx.send(f'https://ru.wikipedia.org/wiki/%D0%93%D0%BB%D0%BE%D0%B1%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%B5_%D0%BF%D0%BE%D1%82%D0%B5%D0%BF%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5')

@bot.command()
async def видео(ctx):
    await ctx.send(f'https://www.youtube.com/watch?v=hRAqE1I-AAI&ab_channel=%D0%92%D0%B8%D0%B4%D0%B5%D0%BE%D1%83%D1%80%D0%BE%D0%BA%D0%B8%D0%B2%D0%98%D0%BD%D1%82%D0%B5%D1%80%D0%BD%D0%B5%D1%82')

@bot.command()
async def пароль(ctx, count=8):
    await ctx.send(f'Ваш пароль -{gen_pass(count)} ')

@bot.command()
async def назовичисло(ctx, dice: str):
    """Rolls a dice in N.N format."""
    try:
        rolls, limit = map(int, dice.split('.'))
    except Exception:
        await ctx.send('Format has to be in N.N!')
        return
    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)
    
@bot.group()
async def cool(ctx):
    """Says if a user is cool.

    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')


bot.run('MTE1MjkwNzQyMDM1MjM4OTE4MQ.GOakW_.NuPy5gR1i1nI3KfQlbcdQLTsL4wr8lkIuU6VBQ')

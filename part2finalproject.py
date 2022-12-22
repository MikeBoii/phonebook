import discord
from credits import bot_token
from discord.ext import commands,tasks
import requests
import asyncio
import time
import os
import random
from random import randint

client = discord.Client()
bot = commands.Bot(command_prefix='!')
token = bot_token

API_URL = 'https://7015.deeppavlov.ai/model'

victorinaPhrases = ["It is flying , but it is a human , who is this?" , "It can be small or big , but it is a human, who is this?" , "A game with blocks", "shooting game with cartoon graphics" , "when was stalin born?", "What's the name of the river that runs through Egypt?" , "In meters, how long is an Olympic swimming pool?"]
ran1 = (random.choice(victorinaPhrases))
words = ['ПРИКОЛ', 'МЕМБРАНА', 'КОДЛЭНД', 'PYTHON','WELCOME','COOLGAME']
members = []  
lives = 0  
running = 'none'  
current_player = 0  
word = []  
display_word = []  
original_word = ''

running1 = 'none'
members1 = []  
lives1 = 5  
current_player1 = 0
wins = 0
loses = 0
coins = 0

x = random.randint(1,10)
running2 = 'none'
members2 = []  
lives2 = 10  
current_player2 = 0
wins2 = 0
loses2 = 0
tries = 0

game_dictionary = {}
member_list = []
screen_dictionary = {}

@bot.command(name='start0')
async def start0(ctx):
    await ctx.send("Bot is working")
    await ctx.send("if you know the commands , go and have fun")
    await ctx.send("if you dont know the commands, type !help1")
    
@bot.command(name='help1')
async def help1(ctx):
    await ctx.send("Active commands: !duck , !joke , !help1, !hello, !addgame ,!showmygames , !question [any question] , !weather [any city] , !start0 , !timer[time in seconds], !pcreminder [how much time you weant to play in seconds], !reminder [time you want to remind yourself in seconds]")
    await ctx.send("Game 'Viselnitsa' commands = !start , !join , !play")
    await ctx.send("Game 'Ping Pong' commands = !ping")
    await ctx.send("Game 'Victorina' commands = !startvictorina , !joinvictorina , !playvictorina , !guessv , !vwlc")
    await ctx.send("Game 'Random Game' commands = !randomgameeasy , !randomgameregular , !randomgamehard")
    await ctx.send("Game 'Random Number Multiplayer' commands = !joinrandom , !playrandom , !startrandom , !guessr , !rwl")
    await ctx.send("if you want help with the games , type !gamehelp")
    
    
@bot.command(name="gamehelp")
async def gamehelp(ctx):
    await ctx.send("Viselnitsa: in your turn , youll have to type an letter , and if you guessed it , it will be shown , then its other players letter , they need to do the same thing.")
    await ctx.send("Ping Pong: this game is basic , type !ping , and you will be answered pong.")
    await ctx.send("Victorina: like Viselnitsa , you need to guess the answer of the questions that will be showed up in your turn.")
    await ctx.send("Random Game: there are stages , you need to write a number that is higher than bots number , then youll win.")
    await ctx.send("Random Number Multiplayer: like viselnitsa and victorina , youll have to guess a number in your turn , then the other player will guess.")

@bot.command(name="joke")
async def joke(ctx):
    jokes = ["What’s the best thing about Switzerland? I don’t know, but the flag is a big plus" , "I invented a new word! Plagiarism!", "Did you hear about the mathematician who’s afraid of negative numbers? He’ll stop at nothing to avoid them." , "Hear about the new restaurant called Karma? There’s no menu: You get what you deserve."]
    await ctx.send(random.choice(jokes))

@bot.command(name="ping")
async def ping(ctx):
    await ctx.channel.send("pong")
    

def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url'] 


@bot.command('duck')
async def duck(ctx):
    global coins
    image_url = get_duck_image_url()
    if coins == 0:
        await ctx.send("Go win some victorinas then come back here")
    if coins > 0:
        coins = coins - 5
        await ctx.send(image_url)
        await ctx.send("coins left " + str(coins) + " .")
    
    
def init2():
    global members1, lives1, running1, current_player1
    members1 = []
    lives1 = 5
    running1 = 'none'
    current_player1 = 0
    wins = 0
    loses = 0
    coins = 0
    
def init3():
    global members2, lives2, running2, current_player2
    members2 = []
    lives2 = 10
    running2 = 'none'
    current_player2 = 0
    wins2 = 0
    loses2 = 0
    tries = 0

@bot.command(name="startvictorina")
async def startvictorina(ctx):
    global running1, members1
    if running1 != 'none':
        await ctx.send('game had began!')
    else:
        running1 = 'joining'
        members1.append(ctx.author.name)
        lives1 = 5
        await ctx.send('game had began! type !joinvictorina, if you want to join.')

@bot.command(name='joinvictorina')
async def joinvictorina(ctx):
    global members1
    if running1 == 'none':
        await ctx.send('theres nowhere to join... type !startvictorina, to create game.')
    elif running1 == 'joining':
        if ctx.author.name not in members1:
            members1.append(ctx.author.name)
            await ctx.send('your in game! enter !playvictorina to play.')
        else:
            await ctx.send('your in game! enter !playvictorina to play.')
    else:
        await ctx.send('the game has been started, enter !playvictorina to play.')
        
@bot.command(name='playvictorina')
async def playvictorina(ctx):
    global running1, word1, ran1, victorinaPhrases , wins
    if running1 == 'none':
        await ctx.send('The game didnt start yet , Enter !startvictorina to enter')
    elif running1 == 'joining':
        running1 = 'running'
        ran1 = (random.choice(victorinaPhrases))
        await ctx.send(
            'The game has began! the word is: ' + ran1 + ', first goes: ' + str(
                members1[current_player1]) + ", Type !guessv and your answer")
    else:
        await ctx.send('the game has started! first goes: : ' + str(
            members1[current_player1]) + ', enter command !gueesv and your answer , the word: ' + ran1)
        
@bot.command(name='guessv')
async def guessv(ctx, *args):
    global current_player1, running1, lives1, victorinaPhrases , ran1 , wins , loses , coins
    g = args[0]
    if running1 == 'running':
        if ctx.author.name in members1:
            if ctx.author.name == members1[
                current_player1]:
                if ran1 == victorinaPhrases[0] and g == "spiderman" or ran1 == victorinaPhrases[1] and g == "antman" or ran1 == victorinaPhrases[2] and g == "minecraft" or ran1 == victorinaPhrases[3] and g == "fortnite" or ran1 == victorinaPhrases[4] and g == "1878" or ran1 == victorinaPhrases[5] and g == "thenile" or ran1 == victorinaPhrases[6] and g == "50":
                    await ctx.send('GoodJob!')
                    await ctx.send('you get 1 win!')
                    wins += 1
                    coins += 5
                    await ctx.send("you have " + str(wins) + " wins and " + str(coins) + " coins")
                    await ctx.send('The character/game has been guessed , game over.')
                    running1 = 'none'
                    init()
                else:
                    lives1 = lives1 - 1
                    await ctx.send('Not Right...')
                if current_player1 == len(members1) - 1:
                    current_player1 = 0
                else:
                    current_player1 += 1
            else:
                await ctx.send('now goes: ' + str(members1[current_player1]))
        else:
            await ctx.send('Error , Log in please.')
        if lives1 <= 0:
            await ctx.send('The character/game hasnt been guessed , game over.')
            await ctx.send('you get 1 loses!')
            loses = loses + 1
            await ctx.send("you have "+ str(loses) + " loses")
            running1 = 'none'
            init()
        else:
            await ctx.send('The Word: ' +  ran1 + ', Now its ' + members1[
                current_player1] + ' turn , lives left: ' + str(lives1))
    elif running1 == 'none':
        await ctx.send('the game didnt start yet , Enter !startvictorina, to start.')
    else:
        await ctx.send('the game didnt start yet , waiting for players ... to start - Enter !playvictorina')
        
@bot.command(name="vwlc")
async def vwinsandloses(ctx):
    global wins , loses
    await ctx.send("you have " + str(wins) + " wins and " + str(loses) + " loses in victorina game , also you have " + str(coins) + " coins.")

@bot.command(name="startrandom")
async def startrandom(ctx):
    global running2, members2 
    if running2 != 'none':
        await ctx.send('game had began!')
    else:
        running2 = 'joining'
        members2.append(ctx.author.name)
        lives2 = 10
        await ctx.send('game had began! type !joinrandom, if you want to join.')

@bot.command(name='joinrandom')
async def joinrandom(ctx):
    global members2 
    if running2 == 'none':
        await ctx.send('theres nowhere to join... type !startrandom, to create game.')
    elif running2 == 'joining':
        if ctx.author.name not in members2:
            members2.append(ctx.author.name)
            await ctx.send('your in game! enter !playrandom to play.')
        else:
            await ctx.send('your in game! enter !playrandom to play.')
    else:
        await ctx.send('the game has been started, enter !playrandom to play.')
        
@bot.command(name='playrandom')
async def playrandom(ctx):
    global running2, word2, ran2, wins2 , x
    if running2 == 'none':
        await ctx.send('The game didnt start yet , Enter !startrandom to enter')
    elif running2 == 'joining':
        running2 = 'running'
        x = random.randint(1,10)
        await ctx.send(
            'The game has began! , first goes: ' + str(
                members2[current_player2]) + ", Type !guessr and your answer")
    else:
        await ctx.send('the game has started! first goes: : ' + str(
            members2[current_player2]) + ', enter command !guessr and your answer')
        
@bot.command(name='guessr')
async def guessr(ctx, *args):
    global current_player2, running2, lives2, x , wins2 , loses2 , tries
    g = int(args[0])
    if running2 == 'running':
        if ctx.author.name in members2:
            if ctx.author.name == members2[
                current_player2]:
                if g == x:
                    await ctx.send('GoodJob!')
                    tries += 1
                    await ctx.send('you get 1 win in ' + str(tries) + ' tries!')
                    wins2 += 1
                    await ctx.send("you have " + str(wins2) + " wins.")
                    await ctx.send('The number has been guessed , game over.')
                    running2 = 'none'
                    init()
                    tries -= tries
                    lives2 = 10
                elif g > x:
                    tries += 1
                    lives2 = lives2 - 1
                    await ctx.send('too high , try lower number , tries: ' + str(tries) + '.')
                elif g < x:
                    tries += 1
                    lives2 = lives2 - 1
                    await ctx.send('too low , try higher number , tries: ' + str(tries) + '.')
                else:
                    lives2 = lives2 - 1
                    await ctx.send('Not Right...')
                if current_player2 == len(members2) - 1:
                    current_player2 = 0
                else:
                    current_player2 += 1
            else:
                await ctx.send('now goes: ' + str(members2[current_player2]))
        else:
            await ctx.send('Error , Log in please.')
        if lives2 <= 0:
            await ctx.send('The character/game hasnt been guessed , game over.')
            await ctx.send('you get 1 loses!')
            loses2 = loses2 + 1
            await ctx.send("you have "+ str(loses2) + " loses")
            running2 = 'none'
            init()
            tries -= tries
            lives2 = 10
        else:
            await ctx.send('Now its ' + members2[
                current_player2] + ' turn , lives left: ' + str(lives2))
    elif running2 == 'none':
        await ctx.send('the game didnt start yet , Enter !startrandom, to start.')
    else:
        await ctx.send('the game didnt start yet , waiting for players ... to start - Enter !playrandom')

@bot.command(name='rwl')
async def guessr(ctx):
    global wins2 , loses2 , tries
    await ctx.send('youve won in random game ' + str(wins2) + ' times and lost ' + str(loses2) + ' times.')
    await ctx.send('tried ' + str(tries) + ' times')
    
@bot.command(name="hello")
async def hello(ctx):
    global member_list
    if ctx.author.name in member_list:
        await ctx.send("Ты уже со мной здоровался - я тебя знаю " + ctx.author.name)
    else:
        member_list.append(ctx.author.name)
        if not os.path.exists(ctx.author.name):
            os.mkdir(ctx.author.name)
        await ctx.send("Привет, " + ctx.author.name + "! Добро пожаловать ко мне!")
    global game_dictionary
    if ctx.author.name not in game_dictionary.keys():
        game_dictionary[ctx.author.name] = []
    global screen_dictionary
    if ctx.author.name not in screen_dictionary.keys():
        screen_dictionary[ctx.author.name] = []

@bot.command(name="addgame")
async def addgame(ctx, message):
    if ctx.author.name not in game_dictionary:
        await ctx.send('Мы с тобой пока не знакомы. Отправь команду !hello в чат, чтобы зарегистрироваться :)')
    else:
        game_list = game_dictionary.get(ctx.author.name)
        game_list.append(str(message))
        game_dictionary[ctx.author.name] = game_list
        await ctx.send("Игра добавлена в список")

@bot.command(name="showmygames")
async def showmygames(ctx):
    if ctx.author.name not in game_dictionary:
        await ctx.send('Мы с тобой пока не знакомы. Отправь команду !start в чат, чтобы зарегистрироваться :)')
    else:
        result = 'Cписок игр, в которые ты играешь: '
        for game in game_dictionary.get(ctx.author.name):
            result += game + ', '
        result = result[::-1].replace(',', '', 1)
        result = result[::-1]
        await ctx.send(result)

@bot.command(name="timer")
async def timer(ctx, number):
    number = int(number)
    message = await ctx.send(number)
    while number != 0:
        number -= 1
        await message.edit(content=number)
        await asyncio.sleep(1)
    await message.edit(content='timer ended!')

@bot.command(name="pcreminder")
async def pcreminder(ctx, *args):
    number = int(args[0])
    message = await ctx.send(number)
    while number != 0:
        number -= 1
        await message.edit(content=number)
        await asyncio.sleep(1)
    await message.edit(content='неплохо было бы встать и размяться')
    number3 = 20
    message = await ctx.send(number3)
    while number3 != 0:
        number3 -= 1
        await message.edit(content=number3)
        await asyncio.sleep(1)
    await ctx.send("Reminder Ended")

@bot.command(name='randomgameeasy')
async def randomgameeasy(ctx, *args):
    x = random.randint(1,100)
    num = int(args[0])
    num2 = 101
    if num > x and num < num2:
        message = await ctx.send(x)
        await ctx.send("youve won :)")
    elif num == x and num < num2:
        message = await ctx.send(x)
        await ctx.send("draw -_-")
    elif num < x and num < num2:
        message = await ctx.send(x)
        await ctx.send("youve lost :(")
    elif num <= num2:
        await ctx.send("Hey! too high...")
    

@bot.command(name='randomgameregular')
async def randomgameregular(ctx, *args):
    x = random.randint(1,1000)
    num = int(args[0])
    num2 = 1001
    if num > x and num < num2:
        message = await ctx.send(x)
        await ctx.send("youve won :)")
    elif num == x and num < num2:
        message = await ctx.send(x)
        await ctx.send("draw -_-")
    elif num < x and num < num2:
        message = await ctx.send(x)
        await ctx.send("youve lost :(")
    elif num <= num2:
        await ctx.send("Hey! too high...")
        
@bot.command(name='randomgamehard')
async def randomgamehard(ctx, *args):
    x = random.randint(1,10000)
    num = int(args[0])
    num2 = 10001
    if num > x and num < num2:
        message = await ctx.send(x)
        await ctx.send("youve won :)")
    elif num == x and num < num2:
        message = await ctx.send(x)
        await ctx.send("draw -_-")
    elif num < x and num < num2:
        message = await ctx.send(x)
        await ctx.send("youve lost :(")
    elif num <= num2:
        await ctx.send("Hey! too high...")

@bot.command(name="reminder")
async def reminder(ctx, *args):
    number = int(args[0])
    message = await ctx.send(number)
    while number != 0:
        number -= 1
        await message.edit(content=number)
        await asyncio.sleep(1)
    await message.edit(content='The reminder ended!')
    s = ""
    for i in range(1,len(args)):
        s = s+  " "  +args[i]
    message = await ctx.send(s)

    
@bot.command(name='weather')
async def start_handler(ctx, *args):
    city = args[0]
    print(city)
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+ city + "&appid=ede30749ae7f851ee08571386f08fded&units=metric&lang=ru")
    temp = response.json()['main']
    temp = temp['temp']
    await ctx.send(temp)

def init():
    global members, lives, running, current_player, word, display_word, original_word
    members = []
    lives = 0
    running = 'none'
    current_player = 0
    word = []
    display_word = []
    original_word = ''
    
@bot.command(name='start')
async def start(ctx):
    global running, members, lives
    if running != 'none':
        await ctx.send('Игра уже началась! Чтобы завершить игру - введите команду !stop')
    else:
        running = 'joining'
        members.append(ctx.author.name)
        lives = 5
        await ctx.send('Игра началась! Пишите !join, если хотите присоединиться.')
        await ctx.send('note: this game contains 3 russian words and 3 english words! so be ready.')

@bot.command(name='join')
async def join(ctx):
    global members
    if running == 'none':
        await ctx.send('Пока некуда присоединяться. Введите !start, чтобы начать игру.')
    elif running == 'joining':
        if ctx.author.name not in members:
            members.append(ctx.author.name)
            await ctx.send('Вы в игре!')
        else:
            await ctx.send('Вы уже в игре!')
    else:
        await ctx.send('Игра уже начата :(')
        
@bot.command(name='play')
async def play(ctx):
    global running, word, display_word, original_word
    if running == 'none':
        await ctx.send('Игра пока не началась. Введите !start, чтобы начать')
    elif running == 'joining':
        running = 'running'
        a = random.choice(words)
        original_word = a 
        for i in a:
            word.append(i)
            display_word.append('-')
        await ctx.send(
            'Игра запущена! Загаданное слово: ' + ''.join(display_word) + ' Первым ходит ' + str(
                members[current_player]) + '. Введите команду !guess и букву.')
    else:
        await ctx.send('Игра запущена! Первым ходит ' + str(
            members[current_player]) + '. Введите команду !guess и букву.\
Загаданное слово: ' + ''.join(display_word))
        
@bot.command(name='guess')
async def guess(ctx, letter):
    global display_word, word, current_player, running, lives
    letter = letter.upper()
    if running == 'running':
        if ctx.author.name in members:
            if ctx.author.name == members[
                current_player]:
                if letter in word:
                    while letter in word:
                        display_word[word.index(letter)] = letter
                        word[word.index(letter)] = '*'
                    await ctx.send('Есть такая буква!')
                else:
                    lives -= 1
                    await ctx.send('Такой буквы нет :(')
                if current_player == len(members) - 1:
                    current_player = 0
                else:
                    current_player += 1
            else:
                await ctx.send('Ошибка! Сейчас ходит ' + str(members[current_player]))
        else:
            await ctx.send('Ошибка! Вы не зарегистрировались :(')
        if word.count('*') == len(word):
            await ctx.send('Слово отгадано, игра окончена. Чтобы начать новую - введите !start.')
            running = 'none'
            init()
        elif lives <= 0:  
            await ctx.send('Слово не отгадано, а жизни кончились. Игра окончена. Чтобы начать новую - введите !start.')
            running = 'none'
            init()
        else:
            await ctx.send('Загаданное слово: ' + ' '.join(display_word) + '. Сейчас ходит ' + members[
                current_player] + '. Жизней осталось: ' + str(lives))
    elif running == 'none':
        await ctx.send('Игра пока не началась. Введите !start, чтобы начать')
    else:
        await ctx.send('Игра пока не запущена, ждем пока все подключатся. Чтобы начать игру - введите !play')
        
bot.run(token)
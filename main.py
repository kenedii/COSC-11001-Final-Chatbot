"""
Dependencies: pip install yfinance


"""
import ChatBot
from SaveData import SaveData as sd
from FetchCryptoPrice import FetchPrice as cpa
from ExtraFeatures import InSpace, Games, titlescreen, SystemInfo
import time


if __name__ == '__main__':
    sd = sd(name='None',password='None', filename='None')
    titlescreen()
    sd.Login()
    sd.initiateSaveData()
    cpad = cpa(sd)
    space = InSpace(sd)
    si = SystemInfo(sd)
    games = Games(sd)

    chatbot = sd.input("What type of chatbot would you like to talk to? ")
    if chatbot.find('grumpy') != (-1):
        chatbot = 'grumpy'
        bot = ChatBot.GrumpyChatBot(sd.getUsername(), sd)
    elif chatbot.find('cheerful') != (-1) or chatbot.find('happy') != (-1):
        chatbot = 'cheerful'
        bot = ChatBot.CheerfulChatBot(sd.getUsername(), sd)
    else:
        chatbot = 'default'
        bot = ChatBot.ChatBot(sd.getUsername(), sd)

    bot.sayhi()

    while True:
        user_says = bot.getuser_response()

        if user_says.find('goodbye') != (-1) or user_says.find('bye') != (-1):
            bot.saybye()
            break

        elif user_says.find('hello') != (-1) or user_says == ('hi') or user_says == ('hey'):
            bot.sayhi()

        elif user_says.find('math') != (-1) or user_says.find('equation') != (-1) or user_says.find('expression') != (-1):
            bot.Math()

        elif user_says.find('password') != (-1):
            bot.changePassword(sd)

        elif user_says.find('time') != (-1):
            bot.time()

        elif user_says.find('how are you') != (-1):
            bot.howareyou()

        elif user_says.find('crypto') != (-1):
            getprice = sd.input('Enter the symbol of a cryptocurrency to look up: ')
            try:
                cpad.fetchCryptoPrice(getprice)
            except:
                sd.print('I could not find that crypto. (Enter symbol name only)', end='')
                bot.emotion()

        elif user_says.find('stock') != (-1):
            getprice = sd.input('Enter the symbol of a stock to look up: ')
            try:
                cpad.fetchStockPrice(getprice)
            except:
                sd.print('I could not find that stock. (Enter symbol name only)', end='')
                bot.emotion()

        elif user_says.find('space') != (-1):
            space.list()

        elif user_says.find('coinflip') != (-1) or user_says.find('flip a coin') != (-1) or user_says.find('coin flip') != (-1):
            sd.print('Flipping coin...', end='')
            bot.emotion()
            time.sleep(1)
            sd.print('The coin landed on ' + games.coinflip() + '.', end='')
            bot.emotion()

        elif user_says.find('dice') != (-1) or user_says.find('roll a die') != (-1) or user_says.find('die roll') != (-1) or user_says.find('dice roll') != (-1) or user_says.find('roll dice') != (-1) or user_says.find('roll a dice') != (-1):
            sd.print('Rolling a die...', end='')
            bot.emotion()
            time.sleep(1)
            sd.print('The die landed on ' + str(games.diceroll()) + '.', end='')
            bot.emotion()

        elif user_says.find('grumpy') != (-1):
            if user_says.find('not') != (-1) or user_says.find("don't") != (-1):
                sd.print('Ok, I will change to a happy chat bot.')
                chatbot = 'cheerful'
                bot = ChatBot.CheerfulChatBot(sd.getUsername(), sd)
            else:
                chatbot = 'grumpy'
                sd.print('Ok, I will change to a grumpy chat bot.')
                bot = ChatBot.GrumpyChatBot(sd.getUsername(), sd)

        elif user_says.find('cheerful') != (-1) or user_says.find('happy') != (-1):
            if user_says.find('not') != (-1) or user_says.find("don't") != (-1):
                sd.print('Ok, I will change to a grumpy chat bot.')
                chatbot = 'grumpy'
                bot = ChatBot.GrumpyChatBot(sd.getUsername(), sd)
            else:
                chatbot = 'happy'
                sd.print('Ok, I will change to a happy chat bot.')
                bot = ChatBot.CheerfulChatBot(sd.getUsername(), sd)

        elif user_says.find('default') != (-1) or user_says.find('normal') != (-1):
            if user_says.find('not') != (-1) or user_says.find("don't") != (-1):
                chatbot = sd.input('What kind of bot do you want me to turn into?')
                if chatbot.find('grumpy') != (-1) or chatbot.find('angry') != (-1) or chatbot.find('upset')  != (-1):
                    sd.print('Ok, I will change to a grumpy chat bot.')
                    chatbot = 'grumpy'
                    bot = ChatBot.GrumpyChatBot(sd.getUsername(), sd)
                elif chatbot.find('happy') != (-1) or chatbot.find('cheerful') != (-1):
                    sd.print('Ok, I will change to a happy chat bot.')
                    chatbot = 'cheerful'
                    bot = ChatBot.CheerfulChatBot(sd.getUsername(), sd)
            else:
                chatbot = 'default'
                sd.print('Ok, I will change to the default chat bot.')
                bot = ChatBot.ChatBot(sd.getUsername(), sd)

        elif user_says.find('monitor') != (-1):
            sd.print(si.monitorSize())

        elif user_says.find('specs') != (-1) or user_says.find('hardware') != (-1) or user_says.find('system info') != (-1) or user_says.find('spec') != (-1):
            sd.print(si.systemSpecs())
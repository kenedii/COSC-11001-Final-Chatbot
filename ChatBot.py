import random
from Math import Math
from datetime import datetime

class ChatBot:
    memory = {'greetings': ['Hi', 'Hello', 'How do you do'],
              'goodbyes': ['Bye', 'See you', 'Goodbye'],
              'howareyou': ['I do not feel emotion. I am a robot', 'I can not feel emotion', 'I do not have any feelings']}
    count = 0 #keeps track of currently active bots

    def __init__(self, name, sd):
        self.name = name
        self.sd = sd


    def getuser_response(self):
        return self.sd.input('You: ').lower()

    def saybye(self):
        self.sd.print(random.choice(ChatBot.memory['goodbyes']), end=' ')

    def sayhi(self):
        self.sd.print(random.choice(ChatBot.memory['greetings']), end=' ')

    def Math(self):
        if self.sd.input('Would you like me to solve a math expression? ').find('yes') != (-1):
            try:
                m = Math()
                answer = m.parser(self.sd.input('Enter an expression for me to solve: '))
                self.sd.print('The answer to your expression is', answer, '.')
            except:
                self.sd.print('I could not parse your expression.')
        else:
            self.sd.print("I do not understand.")

    def changePassword(self, SaveData):
        if self.sd.input('Would you like me to change your password? ').find('yes') != (-1):
            SaveData.setPassword()
        else:
            self.sd.print("I do not understand.")

    def time(self):
        if self.sd.input('Would you like to know the time? ').find('yes') != (-1):
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            self.sd.print("The current time is", current_time, end='')
            self.sd.print('.')
        else:
            self.sd.print("I do not understand.")

    def howareyou(self):
        self.sd.print(random.choice(ChatBot.memory['howareyou']))

    def emotion(self): # Default bot has no emotions.
        return 0

class CheerfulChatBot(ChatBot):
    cheerfulmemory = {'howareyou': ['I am doing good', 'I am happy', 'I am cheerful'],
                      'emotions': ['😀😀😀', '😀😁', '😀😁😀', '😀😀', '😁' ]}

    def sayhi(self):
        super().sayhi()
        self.sd.print( '😀😀😀')

    def howareyou(self):
        self.sd.print(random.choice(CheerfulChatBot.cheerfulmemory['howareyou']), end=' ')
        self.sd.print('😀😀😁')

    def Math(self):
        if self.sd.input('Would you like me to solve a math expression? 😁😁').find('yes') != (-1):
            try:
                m = Math()
                answer = m.parser(self.sd.input('Enter an expression for me to solve: '))
                self.sd.print('The answer to your expression is', answer, '. 😀')
            except:
                self.sd.print("I'm sorry, I could not parse your expression.")
        else:
            self.sd.print("I'm sorry, I do not understand. 😃")

    def time(self):
        if self.sd.input('Would you like to know the time? 😀😀 ').find('yes') != (-1):
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            self.sd.print("The current time is", current_time, end='😀😁')
            self.sd.print('.')
        else:
            self.sd.print("I'm sorry, I do not understand.")

    def emotion(self):
        self.sd.print(random.choice(CheerfulChatBot.cheerfulmemory['emotions']))

class GrumpyChatBot(ChatBot):
    grumpymemory = {'howareyou': ['I am angry', 'I am grumpy', 'I am very upset', 'I am so angry'],
                    'skip': ["Why don't you just do it yourself 🤬", "I don't care what you want 😡", "I'm not doing that for you 😡😡"],
                    'emotions': ["😡😡", '😠', '😠😠', '🤬🤬', '🤬', '🤬😠' ]}

    def sayhi(self):
        super().sayhi()
        self.sd.print(' 😠😠')

    def Math(self):
        if self.sd.input('Would you like me to solve a math expression? 😡😡').find('yes') != (-1):
            if self.skip() == 1:
                self.sd.print(random.choice(GrumpyChatBot.grumpymemory['skip']))
            else:
                try:
                    m = Math()
                    answer = m.parser(self.sd.input('Enter an expression for me to solve: '))
                    self.sd.print('The answer to your expression is', answer, '. 👿')
                except:
                    self.sd.print('Why would I know how to solve that? 🤬🤬')
        else:
            self.sd.print("What the hell are you talking about 👿")

    def time(self):
        if self.sd.input('Would you like to know the time? 🤬🤬').find('yes') != (-1):
            if self.skip() == 1:
                self.sd.print(random.choice(GrumpyChatBot.grumpymemory['skip']))
            else:
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                self.sd.print("The current time is", current_time, end='')
                self.sd.print('. 🤬😡')
        else:
            self.sd.print("I have no clue what you are talking about. 🤬😡")

    def howareyou(self):
        self.sd.print(random.choice(GrumpyChatBot.grumpymemory['howareyou']), end=' ')
        self.sd.print('🤬😡🤬😡')

    def skip(self): # 1 in 5 chance for grumpy chat bot to skip a request
        grumpy = random.randint(1,5)
        if grumpy == 5:
            return 1
        else:
            return 0

    def emotion(self):
        self.sd.print(random.choice(GrumpyChatBot.grumpymemory['emotions']))

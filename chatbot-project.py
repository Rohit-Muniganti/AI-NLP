from nltk.chat.util import Chat, reflections

#Pairs is a list of patterns and responses
pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today ?",]
    ], 
    [
        r"(.*) help(.*)",
        ["I can help you",]
    ],
    [
        r"(.*) your name ?",
        ["My name is Alexa programmer, but you can call me robert and I'm a chatbot .",]
    ],
    [
        r"how are you (.*) ?",
        ["I'm doing very well", "i am great !"]
    ],
    [
        r"sorry (.*)",
        ["Its alright","It's OK, never mind that",]
    ],
    [
        r"I'm(.*) (good|well|okay|ok)",
        ["Nice to hear that","Alright, great !",]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"(.*)created(.*)",
        ["Rohit created me using Pyhton's NLTK library ","top secert ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Hyderabad, India',]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain in  the past 5 days here in %2", "In %2 there is a 50% chance of rain",]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health",]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very huge fan of Cricket",]
    ],
    [
        r"who (.*) (Cricketer\Batsman)?",
        ["M S Dhoni"]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :) ","It was nce talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ['Our customer service will reach you']
    ],
]

#default message at the start of chat
print("Hi, I'm Alexaprogrammer and I like to chat\nPlease type lowercase English language to start a conversation. Type quit to leave ")
#Create Chat Bot
chat = Chat(pairs, reflections)

chat.converse()
import openai
import telebot

#Initalization
BOT_TOKEN = "5793138037:AAHn6mDTwEntRRmc1pXlPztHwSIMMfQTkJ4"

# Set up the OpenAI API client
openai.api_key = "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"

# Set up the model and prompt
model_engine = "text-davinci-003"
n=50


bot = telebot.TeleBot(BOT_TOKEN)
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")
    
    
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    # Generate a response
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=message.text,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.7,
    )
    print("Waiting.....")
    response = completion.choices[0].text
    bot.reply_to(message, response)

bot.infinity_polling()
            
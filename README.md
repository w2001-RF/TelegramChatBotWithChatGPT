# TelegramChatBotWithChatGPT
This repository contains a Telegram chat bot implemented in Python that integrates OpenAI's ChatGPT, an advanced language model, to provide intelligent and interactive conversations. The bot utilizes the telebot library to communicate with the Telegram Bot API.

Features:
- Seamless integration with the Telegram API, allowing the bot to receive and send messages.
- Utilizes the OpenAI API to generate human-like responses using the ChatGPT model.
- Initalizes with the provided BOT_TOKEN and OpenAI API key for authentication.
- Responds to commands like '/start' and '/hello' with a welcoming message.
- Generates responses to user messages by utilizing the ChatGPT model through the OpenAI API.
- Supports dynamic conversation length by setting the 'n' parameter.
- Implements a temperature of 0.7 for controlling response randomness.
- Handles incoming messages using the telebot library's message handler.

Dependencies:
- Python (version X.X.X)
- [telebot](https://github.com/eternnoir/pyTelegramBotAPI): A Python wrapper for the Telegram Bot API.
- [openai](https://github.com/openai/openai-python): OpenAI Python library for interacting with the OpenAI API.

Getting Started:
1. Clone the repository: `git clone https://github.com/your-username/TelegramChatBotWithChatGPT.git`
2. Install the necessary dependencies: `pip install -r requirements.txt`
3. Obtain a Telegram Bot API token from the [BotFather](https://core.telegram.org/bots#botfather) and an OpenAI API key.
4. Set the BOT_TOKEN and openai.api_key variables in the code with your respective tokens.
5. Run the bot: `python main.py`

Contributing:
Contributions to this project are welcome! If you encounter any issues or have suggestions for improvement, please open an issue or submit a pull request.

License:
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

Feel free to modify and extend this description to accurately reflect the specific features and details of your repository.

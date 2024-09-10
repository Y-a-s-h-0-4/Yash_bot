# Yash_bot

Yash_bot is a Discord bot that uses the LangChain library and the Ollama language model to generate conversational responses to user input.

## Features

- Responds to user messages in Discord channels
- Supports private messaging by prefixing messages with '?'
- Uses the LangChain library with the Ollama language model for response generation
- Implements logging for better debugging and monitoring

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7+
- A Discord account and a registered Discord application/bot
- An Ollama setup with the "llama3.1" model

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/yash-bot.git
   cd yash-bot
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   Create a `.env` file in the project root and add your Discord token:
   ```
   DISCORD_TOKEN=your_discord_token_here
   ```

## Usage

To start the bot, run:

```
python main.py
```

The bot will now be online and responsive in your Discord server.

To send a private message to the bot, prefix your message with '?'.

## Project Structure

- `main.py`: The main script that sets up and runs the Discord bot
- `responses.py`: Contains the `get_response` function that generates responses using LangChain and Ollama

## Contributing

Contributions to Yash_bot are welcome. Please feel free to submit a Pull Request.

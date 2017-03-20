# Magic8Ball

## Description
Magic8Ball is a simple Telegram Bot written on Python that can answer on all your question. For each your question it generate random answer on your question. In the `main.py` I wrote handlers for each image. `functions.py` consist all responses on users questions. `configuration.py` is used to save and separate token for your bot from other code. Now, bot run via Heroku and can be found in Telegram by @somethingdoingbot

## Technology
* Python
* PyTelegramBotAPI

## Usage
To run your own Telegram bot you need to registrate your bot in Telegram and generate token, that I wrote in `configuration.py`. After that type the following commands:

```
pip install -r requirements.txt
```

```
python main.py
```

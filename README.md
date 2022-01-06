# Keyword News Filter

The scripts simply scrapes the news aggregator website and sends me links to the articles if their titles contain
keywords from my keyword list.

### Run
```
python main.py
```

### Prerequisites
1) `pip install requirements.txt`
2) A telegram bot should be created and its token should be stored in .env file. Also user id (to whom links
are sent) should be obtained by running the bot in the polling mode.
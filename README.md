# twi-cord  

TwitterのタイムラインをDiscordに表示させるだけのbot

## usage

○ tweepyをインストール  
 
```sh
$ pip install tweepy
```
  
 
○ config.py　　
　config.pyの中身に取得したConsumer API key, Consumer API secret key, Access token, Access token secret, Webhook URLを記入　　
 
```python config.py
CONFIG = {
   "CONSUMER_KEY": "xxxxxxxxxxxxxxxxxxxxxxxxxxx",
   "CONSUMER_SECRET": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
   "ACCESS_TOKEN": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
   "ACCESS_SECRET": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
   "WEBHOOK_URL": "https://discord.com/api/webhooks/xxxxxxxxxxxxxxx",
}
```  
 
○ 実行  
 
``` sh
python twi-cord.py
```  

import tweepy
import requests
import json
from config import CONFIG

auth = tweepy.OAuthHandler(CONFIG["CONSUMER_KEY"], CONFIG["CONSUMER_SECRET"])
auth.set_access_token(CONFIG["ACCESS_TOKEN"], CONFIG["ACCESS_SECRET"])
# APIインスタンスを作成
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

webhook_url = CONFIG["WEBHOOK_URL"]

# フォローしているユーザーのwatch_listを作成
followee_ids = api.friends_ids(screen_name=api.me().screen_name)
watch_list = [str(user_id) for user_id in followee_ids]
watch_list.append(str(api.me().id))

# デフォルトのアクセスレベルではfollowには5000人まで指定できるため
assert(len(watch_list) <= 5000)


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        # @ツイートは表示しない．
        if "@" in status.text:
            pass
        else:
            # ユーザーの情報を取得
            user_id = status.user.id
            user = api.get_user(user_id)
            main_content = {
                   'username': status.user.name,
                   'avatar_url': user.profile_image_url_https,
                   'content': status.text
            }
            headers = {'Content-Type': 'application/json'}
            response = requests.post(webhook_url, json.dumps(main_content), headers=headers)

            print('-------------------------------------------')
            print('name:' + status.user.name)
            print(status.text)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
myStream.filter(follow=watch_list) 

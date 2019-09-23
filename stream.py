from login import *
from tweepy import Stream

#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print(tweet.text)
with open('hashtag.txt', 'r') as file:
    lista_hashtag = [linea.replace('\n','') for linea in file]

class MyStreamListener(tweepy.StreamListener):

    #Agrego funcion para guardar tweets
    def on_data(self,data):
        print('Guardando datos...')
        try:
            with open('tweets.json','a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print('Error on data:',str(e))
        return True

    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return False

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track=lista_hashtag)
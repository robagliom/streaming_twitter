#!/usr/bin/env python
# coding: utf-8
import time
import os
import codecs

from login import *
from tweepy import Stream

with open('hashtag.txt', 'r') as file:
    lista_hashtag = [linea.replace('\n','') for linea in file]

class MyStreamListener(tweepy.StreamListener):

    #Agrego funcion para guardar tweets
    def on_data(self,data):
        print('Guardando datos...')
        try:
            new_data = codecs.unicode_escape_decode(data)[0].encode('utf-16', 'surrogatepass').decode('utf-16')
        except:
            new_data = data
        try:
            directorio = 'tweets/'
            try:
                os.stat(directorio)
            except:
                os.mkdir(directorio)
            name = '{}/{}.json'.format(directorio,time.strftime('%Y-%m-%d_%H-%M-%S'))
            with open(name,'w') as f:#open('tweets.json','a') as f:
                f.write(new_data)
                return True
        except BaseException as e:
            print('Error on data:',str(e))
        return True

    def on_status(self, status):
        print(status.text)

    def on_error(self, status_code):
        print('Error:',status_code)
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return False

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track=lista_hashtag)

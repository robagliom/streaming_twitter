#!/usr/bin/env python
# coding: utf-8
from login import *
from tweepy import Stream

import time
import os

with open('hashtag.txt', 'r') as file:
    lista_hashtag = [linea.replace('\n','') for linea in file]

class MyStreamListener(tweepy.StreamListener):

    #Agrego funcion para guardar tweets
    def on_data(self,data):
        print('Guardando datos...')
        try:
            directorio = 'tweets/'
            try:
                os.stat(directorio)
            except:
                os.mkdir(directorio)
            name = '{}/{}.json'.format(directorio,time.strftime('%Y-%m-%d_%H-%M-%S'))
            with open(name,'w') as f:#open('tweets.json','a') as f:
                f.write(data)
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

<h2>Recolección de datos de Twiter</h2>

<h5>Archivo de configuración: login.py</h5>
<b>Crearr app <a href="https://developer.twitter.com/en/apps">https://developer.twitter.com/en/apps</a></b>
<p>
import tweepy

consumer_key = 'TU-CONSUMER-KEY'
consumer_secret = 'TU-CONSUMER-SECRET'
access_token = 'TU-ACCESS-TOKEN'
access_secret = 'TU-ACCESS-SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
</p>

<h5>Para poner los hashtag a buscar:</h5>
<b>En hashtag.txt</b>
<p>Ponerlos uno debajo del otro. Ejemplo:</p>
<p>hashtag1</p>
<p>hashtag2</p>
<p>hashtag3</p>

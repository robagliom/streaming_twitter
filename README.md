<h2>Recolección de datos de Twiter</h2>

<h5>Archivo de configuración: login.py</h5>
<b>Crearr app <a href="https://developer.twitter.com/en/apps">https://developer.twitter.com/en/apps</a></b>
<p>
import tweepy

<p>consumer_key = 'TU-CONSUMER-KEY'</p>
<p>consumer_secret = 'TU-CONSUMER-SECRET'</p>
<p>access_token = 'TU-ACCESS-TOKEN'<p>
<p>access_secret = 'TU-ACCESS-SECRET'</p>

<p>auth = tweepy.OAuthHandler(consumer_key, consumer_secret)</p>
<p>auth.set_access_token(access_token, access_token_secret)</p>

api = tweepy.API(auth)
</p>

<h5>Para poner los hashtag a buscar:</h5>
<b>En hashtag.txt</b>
<p>Ponerlos uno debajo del otro. Ejemplo:</p>
<p>hashtag1</p>
<p>hashtag2</p>
<p>hashtag3</p>

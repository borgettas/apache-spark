import socket
import tweepy

HOST = 'localhost'
PORT = 9010

s = socket.socket()
s.bind((HOST, PORT))
print(f'Waiting connection: {PORT}')


s.listen(5)
conn, address = s.accept()
print(f'Received solicitation from {address}')

token = 'AAAAAAAAAAAAAAAAAAAAAMhAUgEAAAAAS7U1rBo4zXyB9b3GFpn9Hv4psvA%3DJhv9aHd1Bb4M49KNouQWWBlv3l2DiKp982ufq74BHVR2jv3Br0'

keyword_for_filter = 'futebol'


class GetTweets(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(tweet.text)
        print('*'*50)
        conn.send(tweet.text.encode('utf-8', 'ignore'))


printer = GetTweets(token)
printer.add_rules(tweepy.StreamRule(keyword_for_filter))
printer.filter()

conn.close()
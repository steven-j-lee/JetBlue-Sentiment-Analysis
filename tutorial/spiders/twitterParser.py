from nltk.twitter import Twitter

#export TWITTER="twitterFiles"

data = Twitter()
data.tweets(keywords='Jetblue', to_screen = False, stream = False, limit = 30)

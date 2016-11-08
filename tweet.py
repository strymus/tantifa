from twython import Twython
# Your Tweet belongs here 
tweet = "Example Tweet, "
# Your Api Credentials
apiKey = 'xxx'
apiSecret = 'xxx'
accessToken = 'xxx'
accessTokenSecret = 'xxx'
api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)
api.update_status(status=tweet)

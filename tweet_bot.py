'''
DESCRIPTION :
     Tweet bot script using ChatGPT.

     A developer account of Twitter (currently X) is required to run this script.
     Using ChatGPT in any browser, assuming google here, needs the ChatGPT account to log in.
  
     To use ChatGPT via API function, we have to create an OpenAI API account. 
     Note that in this case,some billing is required.

TO-DO :
     Modify the script with class.
'''

import tweepy
import configparser
import sys

from config_path import config_path

import use_gpt as ugpt

import api_chatgpt as agpt
import gui_chatgpt as ggpt

##
## Read twitter developer info. from the config.ini
##
config = configparser.ConfigParser(interpolation = None)
config.read(config_path,encoding = 'utf-8')

BEARER_TOKEN = config['TWITTER_DEV_INFO']['BEARER_TOKEN']
API_KEY = config['TWITTER_DEV_INFO']['API_KEY']
API_SECRET = config['TWITTER_DEV_INFO']['API_SECRET']
ACCESS_TOKEN = config['TWITTER_DEV_INFO']['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = config['TWITTER_DEV_INFO']['ACCESS_TOKEN_SECRET']

def main():
    if (ugpt.api == True and ugpt.gui == True):
        print(f'Both API and GUI GPT are valid. Set eigher one to True.')
        sys.exit()
    elif (ugpt.api == False and ugpt.gui == False):
        print(f'Both API and GUI GPT are invalid. Set eigher one to True.')
        sys.exit()
    #end if
    
    #schedule.every(1).hours.do(CreateTweet)
    cnt=0
    
    ##create web_chatgpt 
    while True:
        cnt+=1
        CreateTweet()
        #schedule.run_pending()
        if(cnt>=1):
            sys.exit()
        #end if
        sleep(20)
    #end while
    return 0
#end main

def ClientInfo():
    client = tweepy.Client(bearer_token    = BEARER_TOKEN,
                           consumer_key    = API_KEY,
                           consumer_secret = API_SECRET,
                           access_token    = ACCESS_TOKEN,
                           access_token_secret = ACCESS_TOKEN_SECRET,
                           )
    return client
#end ClientInfo

def CreateTweet():
    if (ugpt.gui == True):
        message = ggpt.gui_chatgpt(get_tweet())
    else:
        message = agpt.api_chatgpt(get_tweet())
    #end if
    #message=message+dt.now().strftime('%Y-%m-%d %H:%M:%S')
    
    tweet = ClientInfo().create_tweet(text=message)
    return tweet
#end CreateTweet


def get_tweet():

    tweet = "Where do you think the development of OpenAI is headed?"
    instruct = "Please consider and answer in 40 tokens."
    
    tweet = f"{tweet}{instruct}"  
    return tweet
#end get_tweet
'''
def reply_tweet():
#end reply_tweet

def ref_tweet():
#end ref_tweet

def follow_back():
#end follow_back

def do_retweet():
#end retweet
'''

if __name__=='__main__':
    main()
    

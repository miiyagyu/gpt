'''
DESCRIPTION :
     The script to use ChatGPT via OpenAI API (charge).

TO-DO :
     Modify the script with class.
'''

import openai
import configparser
import sys

from config_path import config_path

##
## Read OpenAI API info. from the config.ini
##
config = configparser.ConfigParser(interpolation = None)
config.read(config_path,encoding = 'utf-8')

openai.api_key = config['OPENAI_API_INFO']['KEY']
'''

'''
def api_chatgpt(prompt):
    messages=[
    {"role":"system","content":"You're the influencer on twitter."},
    {"role":"user","content":prompt}
]
    #print(messages)
    reply=get_completion(messages)
    return reply
#end api_chatgpt

def get_completion(messages,model='gpt-3.5-turbo'):
    response=openai.ChatCompletion.create(
        model = model,
        messages = messages,
        #n = 3          # the resopnse number
        #stop = 'test'  # Strings to stop generating tokens.
        max_tokens = 40,
        frequency_penalty = 1., # -2.0 to 2.0
        temperature=0.8
        #logit_bias = ?
    )
    return response.choices[0].message["content"]
    #response.choices[0].message["content"]
#end



'''
DESCRIPTION :
     The script to use ChatGPT on google browser (free).

TO-DO :
     Modify the script with class.
'''

from chatgpt_client import ChatGPT_Client
import configparser
import sys

import use_gpt as ugpt

from config_path import config_path
#class web_chatgpt:
#    def create_...:


###
### Read user info. to login chatgpt from config.ini
###
config = configparser.ConfigParser(interpolation = None)
config.read(config_path,encoding = 'utf-8')

passwd = config['OPENAI_GUI_INFO']['passwd'] 
email  = config['OPENAI_GUI_INFO']['email']

if (ugpt.api == False and ugpt.gui == True):
    chatgpt = ChatGPT_Client(email,passwd,headless=False)
#end if
def gui_chatgpt(prompt):

    answer=chatgpt.interact(prompt)

    return answer
    #chatgpt.reset_thread()
#end gui_chatgpt

#end class web_chatgpt




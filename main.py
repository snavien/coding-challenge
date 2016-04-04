import json
import os
import unicodedata


def load_jsons():
    sixty_stack = []
    with open(os.getcwd() + '/data-gen/tweets.txt ', 'r', encoding='utf-8') as j_file:
         init_time = 0
         for line in j_file:

            json_dict = json.loads('['+line+']')
            try:
                init_time = json_dict[0]['created_at'].split(' ')[3].split(':')[2])
                print(json_dict[0]['entities']['hashtags'])
            except KeyError:
                print(json_dict)



load_jsons()
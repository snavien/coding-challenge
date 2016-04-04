import json
import os
import unicodedata


def load_jsons():
    sixty_stack = []
    with open(os.getcwd() + '/data-gen/tweets.txt ', 'r', encoding='utf-8') as j_file:
         json_block = []
         init_time = 0
         for line in j_file:

            json_dict = json.loads('['+line+']')
            try:
                print(json_dict[0]['created_at'].split(' ')[3])
                time = json_dict[0]['created_at'].split(' ')[3]
                init_time = int(time.split(':')[0])*60 * 60 + int(time.split(':')[1])*60 + int(time.split(':')[0])
                print(init_time)
                print(json_dict[0]['entities']['hashtags'])
            except KeyError:
                print(json_dict)



load_jsons()
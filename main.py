import json
import os

class ht:
    def __init__(self):
        self.hashtag_pair = []
        self.first_degree = 0


def load_jsons():
    hashtag_q = []
    avg_degree = 0
    hashtag_set = set()
    time_set = False
    with open(os.getcwd() + '/data-gen/tweets.txt ', 'r', encoding='utf-8') as j_file:
         json_block = []
         init_time = 0
         for line in j_file:

            json_dict = json.loads('['+line+']')
            try:
                print(json_dict[0]['created_at'].split(' ')[3])
                time = json_dict[0]['created_at'].split(' ')[3]
                time = int(time.split(':')[0])*60 * 60 + int(time.split(':')[1])*60 + int(time.split(':')[0])
                print(time)
                print(json_dict[0]['entities']['hashtags'])
                curr_ht = json_dict[0]['entities']['hashtags']
                if init_time == 0:
                    init_time = time
                    time_set = True
                    num_elem = len(curr_ht)
                    print(num_elem)
                    print(curr_ht)


                    if len(hashtag_q) >= 1 and num_elem >= 1:   #has items to update
                        hashtag_q.pop(0)                        #pop old
                    else:

                # if time_set:
                #     if time - init_time < 60:
                #         sixty_stack
                #     elif time - init_time == 60:
                #


            except KeyError:
                print(json_dict)



load_jsons()
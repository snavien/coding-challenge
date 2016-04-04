import json
import os
import itertools

class ht:
    def __init__(self, time, text, indices):
        self.text = text
        self.indices = indices
        self.time = time


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
                time = json_dict[0]['created_at'].split(' ')[3]
                time = int(time.split(':')[0])*60 * 60 + int(time.split(':')[1])*60 + int(time.split(':')[0])
                # print(time)
                # print(json_dict[0]['entities']['hashtags'])
                curr_ht = json_dict[0]['entities']['hashtags']


                if init_time == 0:
                    init_time = time
                    time_set = True
                    num_elem = len(curr_ht)
                    # print(num_elem)
                    # print(curr_ht)

                    build_window(hashtag_q, curr_ht, avg_degree)

                if time_set:
                    if time - init_time < 60 and time - init_time >= 0:
                        build_window(hashtag_q, curr_ht, avg_degree)
                    elif time - init_time == 60:
                        build_window(hashtag_q)
                    else:
                        if time - init_time < 0:
                            pop_old(hashtag_q, hashtag_set, curr_ht, avg_degree)


            except KeyError:
                print(json_dict)

def build_window(hashtag_q, hashtag_set, curr_ht, avg_degree):
    len_curr_q = 0
    for h in curr_ht:
        hashtag = ht(time, h['text'], h['indices'])
        print(hashtag.text)
        hashtag_q.append(hashtag)
        if hashtag.text in hashtag_set:
            len_curr_q += 1
        hashtag_set.add(hashtag.text)
    return len_curr_q

def pop_old(hashtag_q, hashtag_set, curr_ht, avg_degree):
    if len(hashtag_q) > 0 and num_elem <= 1:  # has items to update
        old = hashtag_q.pop(0)  # pop old
        avg_degree - ((old.indices[0] + old.indices[1]) / 2.0)


load_jsons()
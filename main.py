import json
import os
from itertools import combinations    
class ht:
    def __init__(self, time, text):
        self.text = text
        self.time = time
        self.degree = 1
    def inc_degree(self):
        self.degree += 1

class edge:
    def __init__(self, pair, indices):
        self.pair = pair

def build_window(curr_ht, time, ht_set, avg_degree, num_nodes, ht_q):
    text_list = []
    edge_list = []
    for h in curr_ht:
        hashtag = ht(time, h['text'])
        text_list.append(hashtag.text)

    comb = combinations(text_list, 2)
    for c in comb:
        if len(c) == 2:
            edge_list.append(c)
            if c not in ht_set:
                ht_set.add(c)   #adding a check for edges already in the graph
                num_nodes += 1  #incrementing nodes for each edge that is added
                make_degree(c[0], ht_q, time)
                make_degree(c[1], ht_q, time)

    print(edge_list)

def make_degree(text, ht_q, time):
    text = str(text)
    if any(x.time != time and x.text != text for x in ht_q):
        ht_q.append(ht(time, text))
    else:
        for x in ht_q:
            if x.time == time and x.text == text:
                x.inc_degree()

# def pop_old(hashtag_q, hashtag_set, curr_ht, avg_degree):
#     if len(hashtag_q) > 0 and num_elem <= 1:  # has items to update
#         old = hashtag_q.pop(0)  # pop old
#         avg_degree - ((old.indices[0] + old.indices[1]) / 2.0)



def load_jsons():
    ht_q = []
    avg_degree = 0
    hashtag_set = set()
    time_set = False

    with open(os.getcwd() + '/data-gen/tweets.txt ', 'r', encoding='utf-8') as j_file:
         init_time = 0
         num_nodes = 0
         ht_q = []
         for line in j_file:

            json_dict = json.loads('['+line+']')
            try:
                time = json_dict[0]['created_at'].split(' ')[3]
                time = int(time.split(':')[0])*60 * 60 + int(time.split(':')[1])*60 + int(time.split(':')[0])
                curr_ht = json_dict[0]['entities']['hashtags']

                ht_set = set()

                if init_time == 0:
                    init_time = time
                    time_set = True

                    build_window(curr_ht, time, ht_set, avg_degree, num_nodes, ht_q)


                    #     build_window(hashtag_q, curr_ht, avg_degree, time)
                #
                # if time_set:
                #     if time - init_time < 60 and time - init_time >= 0:
                #         build_window(hashtag_q, curr_ht, avg_degree, time)
                #     elif time - init_time == 60:
                #         build_window(hashtag_q, curr_ht, avg_degree, time)
                #     else:
                #         continue
                #         # if time - init_time < 0:
                #         #     pop_old(hashtag_q, hashtag_set, curr_ht, avg_degree)


            except KeyError:
                continue


load_jsons()
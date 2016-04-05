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

def build_window(curr_ht, time, ht_set, ht_q):
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
                make_degree(c[0], ht_q, time)
                make_degree(c[1], ht_q, time)


def make_degree(text, ht_q, time):
    text = str(text)
    if not any(x.time == time and x.text == text for x in ht_q):
        ht_q.append(ht(time, text))
    else:
        for x in ht_q:
            if x.time == time and x.text == text:
                x.inc_degree()

def pop_htq(ht_q):
    if len(ht_q) > 0:
        ht_q.pop(0)

def calculate_avg(ht_q):
    num_nodes = 0
    degree = 0
    for h in ht_q:
        degree += h.degree
        num_nodes += 1
    # print("num nodes, degree: ")
    # print(num_nodes)
    # print(degree)
    return degree/float(num_nodes)

def load_jsons():

    avg_degree = 0
    time_set = False

    with open(os.getcwd() + '/data-gen/tweets.txt ', 'r', encoding='utf-8') as j_file:
        ht_set = set()
        init_time = 0
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

                    build_window(curr_ht, time, ht_set, ht_q)

                if time_set:
                    if time - init_time <= 60 and time - init_time >= 0:
                        build_window(curr_ht, time, ht_set, ht_q)
                    else:
                        init_time = 0
                        time_set = False
                        print(calculate_avg(ht_q))
                        # print("hello")
                        if time - init_time > 60:
                            pop_htq(ht_q)
                        # if time - init_time < 0:
                        #     pop_old(hashtag_q, hashtag_set, curr_ht, avg_degree)


            except KeyError:
                continue


load_jsons()
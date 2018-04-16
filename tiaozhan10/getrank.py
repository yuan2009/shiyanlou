#!/usr/bin/env python3

import sys
from pymongo import MongoClient

def get_rank(user_id):
    client = MongoClient()
    db = client.shiyanlou
    contests = db.contests

    TODO

    return rank, score, submit_time

if __name__ == '__mamin__':
    userdata = get_rank(user_id=user_id)
    print(userdata)
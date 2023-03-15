#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_res = [len(sentence)]
    if (len(sentence) == 0):
        tuple_res.append(None)
    else:
        tuple_res.append(sentence[0])
    tuple_res = tuple(tuple_res)
    return (tuple_res)

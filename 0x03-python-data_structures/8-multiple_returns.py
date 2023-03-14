#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_res = [len(sentence)]
    for mem in sentence:
        tuple_res.append(mem)
        break
    tuple_res = tuple(tuple_res)
    return (tuple_res)

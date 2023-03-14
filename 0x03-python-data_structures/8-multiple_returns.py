#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_res = [len(sentence)]
    for mem in sentence:
        if (len(sentence) == 0):
            tuple_res.append(None)
        else:
            tuple_res.append(mem)
        break
    tuple_res = tuple(tuple_res)
    return (tuple_res)

from typing import List, Dict
from collections import OrderedDict
from copy import deepcopy
import json

from php_whisperer import read_php, generate_php

def load_text_from_dict(d, texts) -> List:
    for v in d.values():
        if type(v) == dict:
            load_text_from_dict(v, texts)
            continue
        if type(v) == list:
            for i in v:
                if type(i) == dict:
                    load_text_from_dict(i, texts)
                else:
                    texts.append(i)
        else:
            texts.append(v)

def pack_text_to_dict(d, texts) -> Dict:
    for k, v in d.items():
        if type(v) == dict:
            pack_text_to_dict(v, texts)
            continue
        if type(v) == list:
            if type(v[0]) == dict:
                [pack_text_to_dict(_, texts) for _ in v]
            else:
                d[k] = pack_texts_to_list(texts, len(v))
        else:
            d[k] = texts.pop(0)
    return d

def pack_texts_to_list(texts, length):
    return [texts.pop(0) for _ in range(length)]

def unpack(source):
    source_dict = OrderedDict(read_php(source, variable='data'))
    texts = []
    load_text_from_dict(source_dict, texts)
    return json.dumps(texts)

def pack(source, translated_texts):
    source_dict = OrderedDict(read_php(source, variable='data'))
    dest_dict = dict(pack_text_to_dict(deepcopy(source_dict), translated_texts))
    return generate_php(dest_dict, modern=True)

__all__ = ['pack', 'unpack']
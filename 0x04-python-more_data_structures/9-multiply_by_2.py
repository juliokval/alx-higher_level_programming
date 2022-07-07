#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a_dictionary_copy = dict(1_dictionary)
    for k in a_dictionary_copy.keys():
        a_dictionary_copy[k] = a_dictionary_copy[k] * 2
    retur a_dictionary_copy

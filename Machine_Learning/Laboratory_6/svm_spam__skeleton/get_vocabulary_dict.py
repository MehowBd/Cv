#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv

from typing import Dict


def get_vocabulary_dict() -> Dict[int, str]:
    """Read the fixed vocabulary list from the datafile and return.

    :return: a dictionary of words mapped to their indexes
    """
    dictionary = {}
    with open('C:/Program Files/Studia/6 semestr/Uczenie Maszynowe/Laboratorium 6/svm_spam__skeleton/data/vocab.txt', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader:
            dictionary[row[0].split()[0]] = row[0].split()[1]
        return dictionary 

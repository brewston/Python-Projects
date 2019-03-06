#!/usr/bin/env python
import os
import sys
from collections import Counter

def main():
    results_directory = '/home/tpjones/python/results'
    result_files = os.listdir(results_directory)
    results=[]
    for file in result_files:
        file_day = open(results_directory + '/' + file).read().splitlines()
        for person in file_day:
            results.append(person)
    counter = Counter(results)
    print counter.most_common(50)

if __name__ == "__main__":
    main()


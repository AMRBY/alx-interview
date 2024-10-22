#!/usr/bin/python3
""" process log file """

import sys

i = 0
total = 0
exit_code = {"200": 0, "301": 0, "400": 0, "401": 0,
             "403": 0, "404": 0, "405": 0, "500": 0}
for line in sys.stdin:
    if i == 10:
        print(f"File size: {total}")
        for k, v in exit_code.items():
            print(f"{k}: {v}")
        i = 0

    i += 1
    exit = line.split(" ")[7]
    if exit in exit_code.keys():
        exit_code[exit] += 1
        total += int(line.split(" ")[8])

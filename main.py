#!/usr/bin/env python3
import time
import sys
from on_time_pie import OnTimePie

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("You need to give the token in args")
        sys.exit()
    on_time_pie = OnTimePie(sys.argv[1])
    while True:
        on_time_pie.update_time()
        print(on_time_pie.next_passages)
        time.sleep(60)

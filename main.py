#!/usr/bin/env python3
from on_time_pie import OnTimePie
import time

if __name__ == '__main__':
    onTimePie = OnTimePie()
    while True:
        onTimePie.updateTime()
        time.sleep(60)

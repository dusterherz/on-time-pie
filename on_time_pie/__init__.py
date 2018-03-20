import datetime
import math
import time
import requests
import dateutil.parser
from .display import Display


class OnTimePie():
    def __init__(self, token):
        self.stop_id = "stop_point:OLI:SP:CDO001"  # Canon d'or -> Lille Flandres
        self.region_id = "fr-ne"  # Nord, France
        self.duration = 3600  # in seconds
        self.number_passage = 2  # number of next passage per line
        self.url = 'https://api.navitia.io/v1/coverage/{region}/stop_points/{stop}/stop_schedules'.format(
            region=self.region_id, stop=self.stop_id)
        self.token = token
        self.next_passages = []
        self.display = Display()
        self.display.start()

    def display_times(self):
        for next_passage in self.next_passages:
            self.display.numbers = next_passage['line'] + next_passage['time']
            time.sleep(15)

    def update_times(self):
        response = requests.get(
            self.url,
            params={
                'duration':
                self.duration,
                'items_per_schedule':
                self.number_passage,
                'data_freshness':
                'realtime',
                'from_datetime':
                datetime.datetime.now().isoformat(timespec='seconds')
            },
            auth=(self.token, '')).json()
        self.next_passages = []
        for line in response['stop_schedules']:
            line_number = line['display_informations']['code']
            for date in line['date_times']:
                date_passage = dateutil.parser.parse(date['date_time'])
                now = datetime.datetime.now()
                minutes = math.trunc((date_passage - now).total_seconds() / 60)
                if minutes > 99:
                    minutes = 99
                self.next_passages.append({
                    'time': str(minutes).zfill(2),
                    'line': line_number[:2].zfill(2)
                })

import datetime
import math
import requests
import dateutil.parser


class OnTimePie():
    def __init__(self, token):
        self.stop_id = "stop_point:OLI:SP:CDO001"  # Canon d'or -> Lille Flandres
        self.region_id = "fr-ne"  # Nord, France
        self.duration = 3600  # in seconds
        self.url = 'https://api.navitia.io/v1/coverage/{region}/stop_points/{stop}/stop_schedules'.format(
            region=self.region_id, stop=self.stop_id)
        self.token = token
        self.next_passages = []

    def update_time(self):
        response = requests.get(
            self.url,
            params={
                'duration': self.duration
            },
            auth=(self.token, '')).json()
        self.next_passages = []
        for line in response['stop_schedules']:
            print("first\n {}", line)
            line_number = line['display_informations']['code']
            for date in line['date_times']:
                date_passage = dateutil.parser.parse(date['date_time'])
                now = datetime.datetime.now()
                minutes = math.trunc((date_passage - now).total_seconds() / 60)
                self.next_passages.append({
                    'time': minutes,
                    'line': line_number
                })

import json
import re
from collections import defaultdict
import itertools

class DataManagement:
    def __init__(self, path):
        self.bus_information = None
        self.path= path
        self.errors = {
            'bus_id': 0,
            'stop_id': 0,
            'stop_name': 0,
            'next_stop': 0,
            'stop_type': 0,
            'a_time': 0
        }

    def load_data(self):
        with open(self.path, 'r') as f:
            bus_data = json.load(f)
            self.bus_information = bus_data

    def validate_type_and_empty(self):
        for info in self.bus_information:
            for key, value in info.items():
                match key:
                    case 'bus_id' | 'stop_id' | 'next_stop':
                        if not isinstance(value, int):
                            self.errors[key] += 1
                    case 'stop_name' | 'a_time':
                        if not isinstance(value, str) or value == '':
                            self.errors[key] += 1
                    case 'stop_type':
                        if not isinstance(value, str) or len(value) > 1:
                            self.errors[key] += 1

    def validate_data(self):
        stop_name_pattern = r'[A-Z][\w\s]+(Road|Avenue|Boulevard|Street)'
        stop_type_pattern = r'[SOF]?'
        a_time_pattern = r'[0-2][0-9]:[0-5][0-9]'

        for info in self.bus_information:
            for key, value in info.items():
                match key:
                    case 'bus_id' | 'stop_id' | 'next_stop':
                        continue
                    case 'stop_name':
                        if not isinstance(value, str):
                            continue
                        match = re.fullmatch(stop_name_pattern, value)
                        if not match:
                            self.errors[key] += 1
                    case 'stop_type':
                        if not isinstance(value, str):
                            continue
                        match = re.fullmatch(stop_type_pattern, value)
                        if not match:
                            self.errors[key] += 1
                    case 'a_time':
                        if not isinstance(value, str):
                            continue
                        match = re.fullmatch(a_time_pattern, value)
                        if not match:
                            self.errors[key] += 1

    def count_number_of_stops(self):
        bus_dict = {}
        for info in self.bus_information:
            value = info['bus_id']
            bus_dict[value] = bus_dict.get(value, 0) + 1

        return bus_dict

    def check_start_stop(self):
        lines = ""
        SF_dict = defaultdict(list)
        for info in self.bus_information:
            key = info['bus_id']

            if not isinstance(key, int):
                continue

            value = info['stop_type']
            SF_dict[key].append(value)

        for key, value in SF_dict.items():
            if value.count('S') != 1 or value.count('F') != 1:
                lines = key
                break

        return lines

    def check_start_demand_finish_stop(self):
        transfer_dict = defaultdict(list)
        start_stop_dict = defaultdict(set)

        for info in self.bus_information:
            key = info['stop_type']
            value = info['stop_name']
            if key == 'S':
                start_stop_dict[key].add(value)
            elif key == 'F':
                start_stop_dict[key].add(value)
            elif key == 'O':
                start_stop_dict[key].add(value)

        for info in self.bus_information:
            key = info['bus_id']
            value = info['stop_name']
            transfer_dict[key].append(value)

        transfer_stops = set()
        all_intersection_stops = transfer_dict.values()

        for route1, route2 in itertools.combinations(all_intersection_stops, 2):
            common = set(route1).intersection(set(route2))
            transfer_stops.update(common)

        start_stop_dict['T'] = transfer_stops

        on_demand = start_stop_dict['O'].difference(start_stop_dict['S'], start_stop_dict['F'], start_stop_dict['T'])
        start_stop_dict['O'] = on_demand

        start = sorted(start_stop_dict['S'])
        transfer = sorted(start_stop_dict['T'])
        finish = sorted(start_stop_dict['F'])
        on_demand = sorted(start_stop_dict['O'])

        print(f"Start stops: {len(start)} {start}")
        print(f"Transfer stops: {len(transfer)} {transfer}")
        print(f"Finish stops: {len(finish)} {finish}")
        print(f"On demand stops: {len(on_demand)} {on_demand}")

    def validate_arrival(self):
        arrival_dict = defaultdict(list)
        for info in self.bus_information:
            key = info['bus_id']
            value = info['a_time']
            arrival_dict[key].append(value)

        for key, value in arrival_dict.items():
            for i in range(1, len(value)):
                if value[i-1] >= value[i]:
                    self.errors['a_time'] += 1
                    break

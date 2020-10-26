# Chae DeLaRosa Oct 25th, 2020
import speedtest
import datetime
import json
import time
import os

from network_graph import NetworkGraph


class Monitor:
    '''
        Measure network data
        Save to json files
        Display graph of data collected
    '''

    def __init__(self):

        self.networkSpeed = speedtest.Speedtest()

        json_directory = f"{os.getcwd()}\{self.get_date()}"

        # get network data
        network_data_list = self.get_network_data(6)
        # write data to json
        self.networkjson(network_data_list, json_directory)
        # create graph of data
        network_graph = NetworkGraph(json_directory)

    def get_network_data(self, numOfDataPoints: int):
        '''
            Input: How many data points to be measured
            Store upload and download speeds with the time in a list
        '''
        network_data_list = []
        print("Measuring network speeds...")
        for _ in range(1, numOfDataPoints+1):
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            uploadBits = self.networkSpeed.upload()
            downloadBits = self.networkSpeed.download()

            uploadMbps = round(uploadBits / 1048576, 2)
            downloadMbps = round(downloadBits / 1048576, 2)
            network_data_list.append([current_time, uploadMbps, downloadMbps])
            time.sleep(30)
        print("Network Speeds recorded.")
        return network_data_list

    def get_date(self):

        todays_date = datetime.date.today()

        month_dict = {1: 'jan', 2: 'feb', 3: 'mar', 4: 'aprl', 5: 'may',
                      6: 'jun', 7: 'jul', 8: 'aug', 9: 'sep', 10: 'oct', 11: 'nov', 12: 'dec'}

        date = f"{month_dict[todays_date.month]}-{todays_date.day}"

        return date

    def networkjson(self, datalist: list, directory: str):
        '''
            Input: a list of date information, directory to save files
        '''
        if not os.path.isdir(directory):
            os.mkdir(directory)

        number_of_points = 1
        for dataPoint in datalist:
            networkJsonData = {
                'time': dataPoint[0], 'uploadSpeed': dataPoint[1], 'downloadSpeed': dataPoint[2]}
            with open(f'{directory}\\Network_Data_{number_of_points}.json', 'w') as jsonFile:
                json.dump(networkJsonData, jsonFile, indent=4, sort_keys=True)
            jsonFile.close()
            number_of_points += 1


if __name__ == '__main__':
    netwokmonitor = Monitor()

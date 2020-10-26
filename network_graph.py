# Chae DeLaRosa
import matplotlib.pyplot as plt
import json
import os


class NetworkGraph:

    def __init__(self, netjsondatapath: str):
        network_data_list = []

        for jsonFile in os.listdir(netjsondatapath):
            with open(f'{netjsondatapath}\{jsonFile}', 'r') as network_json:
                network_data_list.append(json.load(network_json))
            network_json.close()

        time = []
        upload_speed = []
        download_speed = []

        for jsondata in network_data_list:
            time.append(jsondata['time'])
            upload_speed.append(jsondata['uploadSpeed'])
            download_speed.append(jsondata['downloadSpeed'])

        self.display_graph(time, upload_speed, download_speed)

    def display_graph(self, time: list, uploadspeed: list, downloadspeed: list):
        '''
            Display the network data as a graph
        '''

        fig, (upload_plot, download_plot) = plt.subplots(2, 1)
        download_plot.plot(time, downloadspeed, label='download', color='r')
        upload_plot.plot(time, uploadspeed, label='upload', color='b')
        download_plot.set_ylabel('Mb/s')
        upload_plot.set_ylabel('Mb/s')
        plt.xlabel('Time')
        fig.suptitle("Internet speeds")
        download_plot.legend()
        upload_plot.legend()
        plt.show()

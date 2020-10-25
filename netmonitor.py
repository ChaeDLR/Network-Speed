import speedtest
import datetime
import json


class Monitor:
    '''
        Work network data
    '''

    def __init__(self):

        self.networkSpeed = speedtest.Speedtest()

        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        todays_date = datetime.date.today()
        day = todays_date.day
        month = todays_date.month
        year = todays_date.year

        dateList = [day, month, year]

        print("Checking network speeds...")
        uploadBits = self.networkSpeed.upload()
        downloadBits = self.networkSpeed.download()

        uploadMbps = round(uploadBits / 1048576, 2)
        downloadMbps = round(downloadBits / 1048576, 2)

        print(f"Time: {current_time}")
        print(f"The {day} day of {month}, {year}")

        print(f"Bits: {uploadBits}, {downloadBits}")

        print(f"Upload: {uploadMbps} mbps\nDownload: {downloadMbps} mbps")

        self.networkjson(dateList, uploadMbps, downloadMbps)

    def networkjson(self, datelist: list, uploadspeed: float, downloadspeed: float):
        '''
            Input: a list of date information, network upload, and network download speed
                in Mb/s
        '''
        networkJsonData = {'day': datelist[0], 'month': datelist[1],
                           'year': datelist[2], 'uploadSpeed': uploadspeed, 'downloadSpeed': downloadspeed}
        with open('Network_Data.json', 'w') as jsonFile:
            json.dump(networkJsonData, jsonFile, indent=4, sort_keys=True)
        jsonFile.close()


if __name__ == '__main__':
    netwokmonitor = Monitor()

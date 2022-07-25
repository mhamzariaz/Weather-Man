from calculations import Calculations
from filehandler import FileHandler
from weatherreadings import WeatherReadings


class CalculationsResults:

    @staticmethod
    def get_temperatures_result(*args):
        for i in args:
            h_temp = i[0]
            h_temp_day = i[1]
            h_temp_month = i[2]
            l_temp = i[3]
            l_temp_day = i[4]
            l_temp_month = i[5]
            max_humid = i[6]
            max_humid_day = i[7]
            max_humid_month = i[8]

            print(f'\nHighest Temperature: {h_temp}C on {h_temp_day} {h_temp_month}\nLowest Temperature:'
                  f' {l_temp}C on {l_temp_day} {l_temp_month}\nMaximum Humidity: {max_humid}% on {max_humid_day}'
                  f' {max_humid_month}')

    @staticmethod
    def get_averages_result(*args):
        for i in args:
            average_highest_temp = i[0]
            average_lowest_temp = i[1]
            average_mean_humid = i[2]
            print(f'\nHighest Average Temperature: {average_highest_temp}C \nLowest Average Temperature:'
                  f' {average_lowest_temp}C\nAverage Humidity: {average_mean_humid}%')

    @staticmethod
    def get_charts_result(arg):
        for x in arg:
            print(x)


"""f = FileHandler()
data = f.get_data('/Users/hamzariaz/PycharmProjects/weather_man')
d = WeatherReadings()
main_data = d.retrieve_required_data(data)
c = Calculations()
c2 = CalculationsResults()
c2.get_charts_result(c.get_chart(main_data, 2011, 6))"""


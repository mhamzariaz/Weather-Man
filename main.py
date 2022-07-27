import argparse
from calculations import Calculations
from calculationsresult import CalculationsResults
from datetime import datetime
from filehandler import FileHandler
from weatherreadings import WeatherReadings


def is_valid_year(date):
    try:
        return datetime.strptime(date, "%Y").date()
    except:
        print("Invalid Format")


def is_valid_year_month(date):
    try:
        return datetime.strptime(date, "%Y/%m").date()
    except:
        print("Invalid Date Format")


def input_handler():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help='path to project folder')
    parser.add_argument('-e', type=is_valid_year, help='year')

    allowed = ['-a', '-c']
    [parser.add_argument(arg, action='append', type=is_valid_year_month, help='year/month') for arg in allowed]
    arguments = parser.parse_args()

    my_dict = vars(arguments)

    open_files = FileHandler()
    weather_data = WeatherReadings()
    results = Calculations()
    print_results = CalculationsResults()

    for flag, values in my_dict.items():

        if flag == 'path':

            main_data = open_files.read_files(values)
            retrieved_data = weather_data.retrieve_required_data(main_data)

        elif flag == 'e' and values:

            temperature_data = results.get_temperatures(retrieved_data, values.year)
            print_results.get_temperatures_result(temperature_data)

        elif flag == 'a' and values:

            average_data = results.get_average(retrieved_data, values[0].year, values[0].month)
            print_results.get_averages_result(average_data)

        elif flag == 'c' and values:

            charts_data = results.get_chart(retrieved_data, values[0].year, values[0].month)
            print_results.get_charts_result(charts_data)


input_handler()

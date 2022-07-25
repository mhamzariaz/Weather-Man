import argparse
from calculations import Calculations
from calculationsresult import CalculationsResults
from datetime import datetime
from filehandler import FileHandler
from weatherreadings import WeatherReadings


def is_valid_year(date):
    try:
        date = datetime.strptime(date, "%Y").date()
        return date
    except:
        print("Invalid Format")


def is_valid_year_month(date):
    try:
        date = datetime.strptime(date, "%Y/%m").date()
        return date
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
            main_data = open_files.get_data(values)
            new_data = weather_data.retrieve_required_data(main_data)

        elif flag == 'e' and values is not None:
            new_list = results.get_temperatures(new_data, values.year)
            print_results.get_temperatures_result(new_list)

        elif flag == 'a' and values is not None:
            for item in values:
                new_list = results.get_average(new_data, item.year, item.month)
                print_results.get_averages_result(new_list)

        elif flag == 'c' and values is not None:

            for item in values:
                new_list = results.get_chart(new_data, item.year, item.month)
                print_results.get_charts_result(new_list)


input_handler()

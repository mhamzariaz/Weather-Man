from datetime import datetime
from filehandler import FileHandler


class WeatherReadings:

    @staticmethod
    def retrieve_required_data(data_from_files):

        main_dates = []
        for line in data_from_files:

            needed_dates = []
            for k, v in line.items():
                if k == 'PKT' or k == 'PKST':
                    dates = v

            highest_temp = line['Max TemperatureC']
            lowest_temp = line['Min TemperatureC']
            highest_humid = line['Max Humidity']
            mean_humid = line[' Mean Humidity']

            new_dates = datetime.strptime(dates, '%Y-%m-%d')

            if len(highest_temp) >= 1 and \
                    len(lowest_temp) >= 1 and \
                    len(highest_humid) >= 1:

                needed_dates.append(int(new_dates.year))
                needed_dates.append(int(new_dates.month))
                needed_dates.append(int(new_dates.day))
                needed_dates.append(int(highest_temp))
                needed_dates.append(int(lowest_temp))
                needed_dates.append(int(highest_humid))
                needed_dates.append(int(mean_humid))

            if len(needed_dates) > 0:
                results_dict = {
                    "Year": needed_dates[0],
                    "Month": needed_dates[1],
                    "Day": needed_dates[2],
                    "Highest Temperature": needed_dates[3],
                    "Lowest Temperature": needed_dates[4],
                    "Max Humid": needed_dates[5],
                    "Mean Humid": needed_dates[6]
                }

                main_dates.append(results_dict)
        return main_dates

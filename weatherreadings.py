from datetime import datetime


class WeatherReadings:

    @staticmethod
    def retrieve_required_data(reader):  # takes data from files and returns required data in the form of a list

        main_dates = []
        for line in reader:

            needed_dates = []  # list to store all the required data
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
                try:
                    needed_dates.append(int(new_dates.year))
                    needed_dates.append(int(new_dates.month))
                    needed_dates.append(int(new_dates.day))
                    needed_dates.append(int(highest_temp))
                    needed_dates.append(int(lowest_temp))
                    needed_dates.append(int(highest_humid))
                    needed_dates.append(int(mean_humid))
                except ValueError:
                    pass

            if len(needed_dates) == 7:
                main_dates.append(needed_dates)
        return main_dates

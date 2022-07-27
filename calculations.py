from datetime import datetime


def convert_to_date(year, month, day):
    date = datetime.strptime((str(year) + '-' + str(month) + '-' + str(day)), '%Y-%m-%d')
    return datetime.strftime(date, "%B")


class Calculations:

    @staticmethod
    def get_temperatures(data_from_weather_readings, year):

        this_year = []

        for item in data_from_weather_readings:
            if item['Year'] == int(year):
                this_year.append(item)

        h_temp = 0
        l_temp = 1000
        max_humid = 0
        h_temp_day = 0
        l_temp_day = 0
        max_humid_day = 0
        h_temp_month = 0
        l_temp_month = 0
        max_humid_month = 0

        # Calculating max, min temperatures and humidity

        for i in this_year:
            if i['Highest Temperature'] > h_temp:
                h_temp = i['Highest Temperature']
                h_temp_day = i['Day']
                h_temp_month = i['Month']

            if i['Lowest Temperature'] < l_temp:
                l_temp = i['Lowest Temperature']
                l_temp_day = i['Day']
                l_temp_month = i['Month']

            if i['Max Humid'] > max_humid:
                max_humid = i['Max Humid']
                max_humid_day = i['Day']
                max_humid_month = i['Month']

        high_month = convert_to_date(year, h_temp_month, h_temp_day)
        low_month = convert_to_date(year, l_temp_month, l_temp_day)
        high_humid_month = convert_to_date(year, max_humid_month, max_humid_day)

        return {
            'High Temp': h_temp,
            'High Day': h_temp_day,
            'High Month': high_month,
            'Low Temp': l_temp,
            'Low Day': l_temp_day,
            'Low Month': low_month,
            'High Humid': max_humid,
            'High Humid Day': max_humid_day,
            'High Humid Month': high_humid_month
        }

    @staticmethod
    def get_average(data_from_weather_readings, year, month):

        this_month = []
        for item in data_from_weather_readings:
            if item['Year'] == int(year) and item['Month'] == int(month):
                this_month.append(item)

        max_temp = 0
        low_temp = 0
        mean_humid = 0

        for i in this_month:
            if i['Highest Temperature'] > max_temp and \
                    i['Lowest Temperature'] > low_temp and \
                    i['Mean Humid'] > mean_humid:
                max_temp = i['Highest Temperature']
                low_temp = i['Lowest Temperature']
                mean_humid = i['Mean Humid']

        new_max_temp = []
        new_min_temp = []
        new_mean_humid = []

        for items in this_month:
            new_max_temp.append(items['Highest Temperature'])
            new_min_temp.append(items['Lowest Temperature'])
            new_mean_humid.append(items['Mean Humid'])

        # Calculating Averages
        mean_max_temp = int(sum(new_max_temp) / len(new_max_temp))
        mean_min_temp = int(sum(new_min_temp) / len(new_min_temp))
        mean_mean_humid = int(sum(new_mean_humid) / len(new_mean_humid))

        return {
            'Mean Max Temp': mean_max_temp,
            'Mean Min Temp': mean_min_temp,
            'Mean Mean humid': mean_mean_humid
        }

    @staticmethod
    def get_chart(data_from_weather_readings, year, month):

        this_month = []
        results_list = []

        for item in data_from_weather_readings:

            if item['Year'] == int(year) and item['Month'] == int(month):
                this_month.append(item)

        for sub in this_month:
            n_day = sub['Day']

        new_month = convert_to_date(year, month, n_day)

        print(f'\n{new_month}, {year}')

        # Bar Chart
        for sub_data in this_month:
            day = sub_data['Day']
            high_temp = sub_data['Highest Temperature']
            low_temp = sub_data['Lowest Temperature']
            plot_high = '+' * high_temp
            plot_low = '+' * low_temp

            # Task 3

            results_dict = {
                'Day': day,
                'Plot High': plot_high,
                'Plot Low': plot_low,
                'High Temp': high_temp,
                'Low Temp': low_temp
            }

            results_list.append(results_dict)

        return results_list

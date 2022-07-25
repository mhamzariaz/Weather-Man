from datetime import datetime


class Calculations:

    @staticmethod
    def get_temperatures(given_data, year):

        this_year = []  # to store the current years data

        for item in given_data:
            if item[0] == int(year):
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
            if i[3] > h_temp:
                h_temp = i[3]
                h_temp_day = i[2]
                h_temp_month = i[1]

            if i[4] < l_temp:
                l_temp = i[4]
                l_temp_day = i[2]
                l_temp_month = i[1]

            if i[5] > max_humid:
                max_humid = i[5]
                max_humid_day = i[2]
                max_humid_month = i[1]

        date_max_temp = datetime.strptime((str(year) + '-' + str(h_temp_month) + '-' + str(h_temp_day)), '%Y-%m-%d')
        high_month = datetime.strftime(date_max_temp, "%B")

        date_min_temp = datetime.strptime((str(year) + '-' + str(l_temp_month) + '-' + str(l_temp_day)), '%Y-%m-%d')
        low_month = datetime.strftime(date_min_temp, "%B")

        date_max_humid = datetime.strptime((str(year) + '-' + str(max_humid_month) + '-' + str(max_humid_day)),
                                           '%Y-%m-%d')
        high_humid_month = datetime.strftime(date_max_humid, "%B")

        return [h_temp, h_temp_day, high_month, l_temp, l_temp_day, low_month, max_humid, max_humid_day, high_humid_month]

    @staticmethod
    def get_average(given_data, year, month):

        this_month = []  # to store the current month data
        for item in given_data:
            if item[0] == int(year) and item[1] == int(month):
                this_month.append(item)

        max_temp = 0
        low_temp = 0
        mean_humid = 0

        for i in this_month:
            if i[3] > max_temp and i[4] > low_temp and i[5] > mean_humid:
                max_temp = i[3]
                low_temp = i[4]
                mean_humid = i[5]

        new_max_temp = []
        new_min_temp = []
        new_mean_humid = []

        for items in this_month:
            new_max_temp.append(items[3])
            new_min_temp.append(items[4])
            new_mean_humid.append(items[5])

        # Calculating Averages
        mean_max_temp = int(sum(new_max_temp) / len(new_max_temp))
        mean_min_temp = int(sum(new_min_temp) / len(new_min_temp))
        mean_mean_humid = int(sum(new_mean_humid) / len(new_mean_humid))

        return mean_max_temp, mean_min_temp, mean_mean_humid

    @staticmethod
    def get_chart(given_data, year, month):

        this_month = []  # to store the current months data
        for item in given_data:
            if item[0] == int(year) and item[1] == int(month):
                this_month.append(item)

        for sub in this_month:
            n_day = sub[2]

        new_date = datetime.strptime((str(year) + "-" + str(month) + '-' + str(n_day)), "%Y-%m-%d")
        new_month = datetime.strftime(new_date, "%B")

        print(f'\n{new_month}, {year}')

        # Bar Chart
        for sub_data in this_month:
            day = sub_data[2]
            high_temp = sub_data[3]
            low_temp = sub_data[4]
            plot_high = '+' * high_temp
            plot_low = '+' * low_temp

            # Task 3
            yield (f'\u001b[37;1m{day}\u001b[31;1m{plot_high}\u001b[35;1m{high_temp}C\n\u001b[37;1m{day}\u001b[34;1m'
                   f'{plot_low}\u001b[35;1m{low_temp}C')

            # Bonus Task
            yield (f'\u001b[37;1m{day}\u001b[34;1m{plot_low}\u001b[31;1m{plot_high}'
                   f'\u001b[37;1m{low_temp}-{high_temp}C\u001b[37;1m')

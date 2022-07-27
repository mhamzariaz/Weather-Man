class CalculationsResults:

    @staticmethod
    def get_temperatures_result(data_from_calculations):
        h_temp = data_from_calculations['High Temp']
        h_temp_day = data_from_calculations['High Day']
        h_temp_month = data_from_calculations['High Month']
        l_temp = data_from_calculations['Low Temp']
        l_temp_day = data_from_calculations['Low Day']
        l_temp_month = data_from_calculations['Low Month']
        max_humid = data_from_calculations['High Humid']
        max_humid_day = data_from_calculations['High Humid Day']
        max_humid_month = data_from_calculations['High Humid Month']

        print(f'\nHighest Temperature: {h_temp}C on {h_temp_day} {h_temp_month}\nLowest Temperature:'
              f' {l_temp}C on {l_temp_day} {l_temp_month}\nMaximum Humidity: {max_humid}% on {max_humid_day}'
              f' {max_humid_month}')

    @staticmethod
    def get_averages_result(data_from_calculations):
        average_highest_temp = data_from_calculations['Mean Max Temp']
        average_lowest_temp = data_from_calculations['Mean Min Temp']
        average_mean_humid = data_from_calculations['Mean Mean humid']

        print(f'\nHighest Average Temperature: {average_highest_temp}C \nLowest Average Temperature:'
              f' {average_lowest_temp}C\nAverage Humidity: {average_mean_humid}%')

    @staticmethod
    def get_charts_result(data_from_calculations):
        red = '\u001b[31;1m'
        white = '\u001b[37;1m'
        blue = '\u001b[34;1m'
        purple = '\u001b[35;1m'

        for i in data_from_calculations:
            day = i['Day']
            plot_high = i['Plot High']
            plot_low = i['Plot Low']
            high_temp = i['High Temp']
            low_temp = i['Low Temp']

            print(f'{white}{day}{red}{plot_high}{purple}{high_temp}C{white}\n{day}{blue}'
                  f'{plot_low}{purple}{low_temp}C')

            print(f'{white}{day}{blue}{plot_low}{red}{plot_high}'
                  f'{purple}{low_temp}-{high_temp}C{white}')

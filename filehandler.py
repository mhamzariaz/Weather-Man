import csv
import os


class FileHandler:

    @staticmethod
    def read_files(path):
        my_list = []
        var = os.path.join(path, 'weatherfiles')
        for files in os.listdir(var):
            with open(os.path.join(var, files), 'r') as file:
                reader = csv.DictReader(file, delimiter=',')
                for item in reader:
                    my_list.append(item)
        return my_list

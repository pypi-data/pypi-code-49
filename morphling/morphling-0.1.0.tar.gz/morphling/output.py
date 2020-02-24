import csv

class Writer:

    def __init__(self):
        pass

    def write(self, data, file_path):
        with open(file_path, "w") as writer:
            writer.write(data)

    def append(self, data, file_path):
        with open(file_path, "a") as writer:
            writer.write(data)

    def to_csv(self, data, file_path):
        with open(file_path, mode='w') as output_file:
            writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in data:
                writer.writerow(row)
import csv
from collections import defaultdict


def read_csv_file():
    my_dict = defaultdict(list)
    csv_file_path = 'sample_resources/Khombedza Health Centre.csv'
    with open(csv_file_path, mode='r') as infile:
        csv_reader = csv.DictReader(infile)
        for line in csv_reader:
            first_field_name = csv_reader.fieldnames[0]
            second_field_name = csv_reader.fieldnames[1]
            third_field_name = csv_reader.fieldnames[2]
            location_details = {'name': line[third_field_name], 'parent_id': line[second_field_name]}
            my_dict[line[first_field_name]].append(location_details)

    return my_dict


if __name__ == '__main__':
    print(read_csv_file())

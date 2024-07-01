from file.export_csv import dict_list_to_csv
from file.load_csv import csv_to_dict_list
from pprint import pprint


LETTER_GROUPS = {
    'Aa-Cn': 'Molly',
    'Co-Gd': 'Laynee',
    'Ge-Jz': 'Greg',
    'Ka-Mc': 'Michelle',
    'Md-Pz': 'Grace',
    'Qa-Ss': 'Tiffany',
    'St-Zz': 'Amy'
}


def get_group(last_name: str) -> tuple[str, str] | None:
    """
    Determine the employee responsible for a student based on their last name.
    :param last_name: last name of the student
    :return: Associated employee based on the last name
    """
    for group, employee in LETTER_GROUPS.items():
        start, end = group.split('-')
        if start <= last_name[:2] <= end:
            return group, employee
    return None


if __name__ == '__main__':
    yield_path = "input/MontanaStateUniversity_Yield_20240627.csv"
    yield_data = csv_to_dict_list(yield_path)

    # split the data into groups
    split_data = {}
    for line in yield_data:
        lastname = line["last_name"]
        l_group = get_group(lastname)
        if l_group not in split_data:
            split_data[l_group] = [line]
        else:
            split_data[l_group].append(line)

    # export the data to separate files
    for l_group in split_data:
        if not l_group:
            continue
        group_data = split_data[l_group]
        print(l_group, len(group_data))
        dict_list_to_csv(data=group_data,
                         filename=l_group[0],
                         folder="output")

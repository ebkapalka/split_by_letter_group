import csv


def csv_to_dict_list(path: str) -> list[dict]:
    """
    Read a CSV file into a list of dictionaries.
    :param path: Path to the CSV file.
    :return: List of dictionaries.
    """
    with open(path, 'r') as file:
        reader = csv.DictReader(file)
        # strip all keys and all values
        output_list = []
        for row in reader:
            output_list.append({k.strip(): v.strip()
                                for k, v in row.items()})
        return output_list

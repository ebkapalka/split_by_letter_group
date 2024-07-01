from datetime import datetime
import csv
import os


def dict_list_to_csv(data: list[dict], filename: str, folder: str) -> None:
    """
    Write a list of dictionaries to a CSV file.
    :param data: list of dictionaries whose keys are the column names
    :param filename: the base name of the file
    :param folder: folder to save the file
    :return: None
    """
    filename = f"yield_{timestamp()}_{filename}.csv"
    path = os.path.join(folder, filename)
    with open(path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def timestamp(dt_obj: datetime = None, fmt: str = "%Y%m%d") -> str:
    """
    Generate a timestamp in the specified format.
    :param dt_obj: datetime object
    :param fmt: format for the timestamp
    :return: timestamp string
    """
    if not dt_obj:
        dt_obj = datetime.now()
    return dt_obj.strftime(fmt)

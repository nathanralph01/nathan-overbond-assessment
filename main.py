import matplotlib.pyplot as plt
import numpy as np

MONTHS = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug',
          9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}


def get_data(input_file):
    """
    Extracts data from input_file.

    :param input_file: String representing file name
    :return: 2D list containing file content. Each element is a row in input_file, and sub-list element is a data
    entry (seperate by ';' in input_file).
    """
    raw_data = open(input_file, encoding='utf8')
    data_lst = []
    for line in raw_data:
        data_lst.append(line.split(';'))
    return data_lst


def get_fields(data_lst):
    """
    Given a list of extracted data, get the desired data fields (DIs, BPr, APl, Pl)

    :param data_lst: 2D list containing raw data content. Each element is a row in input_file, and sub-list
    element is a data entry.
    :return: List of dictionaries, where each dictionary represents each records respective DIs, BPr, APl, and Pl
    data-values. If a record does not contain a specfic data-value, the value at key data-value will be None.
    """

    output_lst = []

    temp_dict = {'DIs': None, 'BPr': None, 'APl': None, "Pl": None}
    for row in data_lst:
        cnt = 0
        for entry in row:
            if len(entry) >= 3:
                if entry[0:3] == 'DIs':
                    temp_dict['DIs'] = get_date(entry[3:])
                elif entry[0:3] == 'BPr':
                    temp_dict['BPr'] = float(entry[3:])
                elif entry[0:3] == 'APl':
                    temp_dict["APl"] = float(entry[3:])
                elif entry[0:2] == 'Pl':
                    temp_dict['Pl'] = float(entry[2:])
            cnt += 1

        if cnt >= 10 and temp_dict['DIs'] is not None:
            output_lst.append(temp_dict)
            temp_dict = {'DIs': None, 'BPr': None, 'APl': None, "Pl": None}

    return output_lst


def get_date(date_str):
    """
    Converts date to new string format.

    :param date_str: String representing a records date. Of the format "YYYYMMDD"
    :return: A string object representing date in format DD-MM-YY
    """
    year = (date_str[:4])[2:]
    month = MONTHS[int(date_str[4:6])]
    day = date_str[6:]

    return day + '-' + month + '-' + year


def fix_lst(lst1, lst2):
    """
    Sorts and removes unnecessary data from lst1 and lst2. Data is deemed unecessary if the value in lst2 is None.
    *Note: Values in lst1 at index i are directly related to values in lst2 at index i.

    :param lst1: List representing list of dates
    :param lst2: List representing a numeric list of some other attribute
    :return: Two new lists (new_lst1, new_lst2) containing no None values. Dates in new_lst1
    directly correspond to the attribute value in new_lst2
    """

    temp_lst1 = []
    temp_lst2 = []
    for i in range(0, len(lst1)):
        if lst2[i] is not None:
            temp_lst1.append(lst1[i])
            temp_lst2.append(lst2[i])

    # Combine temp_lst1, temp_lst2 into a list of tuples
    temp_sort = list(zip(temp_lst1, temp_lst2))
    temp_sort.sort()  # Sorts by numeric value in tuple

    new_lst1 = [y for y, x in temp_sort]  # Extracts non-numeric tuple values
    new_lst2 = [x for y, x in temp_sort]  # Extracts numeric tuple values

    return new_lst1, new_lst2


def plot_graph(date_lst, bid_lst, ask_lst, price_lst):
    """
    Plots a scatter-plot graph given lists of desired data.

    :param date_lst: List containg each records date
    :param bid_lst: List containing each records CleanBid
    :param ask_lst: List containg eaach records CleanAsk
    :param price_lst: List containing each records Last Price

    :return: None
    """

    # Plot CleanBids
    dates, bids = fix_lst(date_lst, bid_lst)
    plt.scatter(dates, bids, c='r')

    # Plot CleanAsks
    dates, asks = fix_lst(date_lst, ask_lst)
    plt.scatter(dates, asks, c='g')

    # Plot Last Prices
    dates, prices = fix_lst(date_lst, price_lst)
    plt.scatter(dates, prices, c='b')

    plt.xticks(np.arange(0, len(date_lst), 5), rotation=90)
    plt.legend(['CleanBid', 'CleanAsk', 'LastPrice'])
    plt.show()


def main(data_file):
    """
    Given a desired raw data filename, the function will create and display a matplotlib
    scatter plot displaying the desired information.

    :param data_file: String representing the desired filename
    :return: None
    """

    raw_data = get_data(data_file)
    data_lst = get_fields(raw_data)

    date_lst, bid_lst, ask_lst, price_lst = [], [], [], []
    for entry in data_lst:
        if not ((entry['BPr'] is None) and (entry['APl'] is None) and (entry['Pl'] is None)):
            date_lst.append(entry['DIs'])
            bid_lst.append(entry['BPr'])
            ask_lst.append(entry['APl'])
            price_lst.append(entry['Pl'])

    plot_graph(date_lst, bid_lst, ask_lst, price_lst)





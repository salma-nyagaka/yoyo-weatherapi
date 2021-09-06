
from functools import reduce
import statistics


def perform_computations(data):
    """ Function to get the maximum, minimum, average
    and median data from the temperature data
    """

    responses = data['forecast']['forecastday']

    maximum = []
    minimum = []
    avg = []

    for response in responses:
        maximum.append(response['day']['maxtemp_c'])
        minimum.append(response['day']['mintemp_c'])
        avg.append(response['day']['avgtemp_c'])

    total_average = reduce(add, avg)
    length = len(avg)
    average_data = total_average / length

    max_median = median_number(maximum)
    min_median = median_number(minimum)

    median = {
        "maximum_median": max_median,
        "minimum_median": min_median
    }

    return max(maximum), min(minimum), average_data, median


def add(x, y):
    """
    Function to add all numbers in the list
    """

    return x + y


def median_number(data):
    """
    Function to get the median
    from the maximum temperature values
    and the median from the minimum temperature
    values
    """

    med = statistics.median(data)
    return med

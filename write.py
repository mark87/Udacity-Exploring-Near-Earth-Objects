"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""
import csv
import json


def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = (
        'datetime_utc', 'distance_au', 'velocity_km_s',
        'designation', 'name', 'diameter_km', 'potentially_hazardous'
    )

    # Open new CSV file with filename provided by user
    with open(filename, 'w') as csv_file:
        # Create CSV writer
        writer = csv.writer(csv_file)
        # First row is the header row containing fieldnames collection
        writer.writerow(fieldnames)

    """Check for missing values and update values from results stream to make
    more readable"""
    for result in results:
        if result.neo.name is None:
            result.neo.name = ''
        if result.neo.diameter is None:
            result.neo.diameter == 'nan'
        if result.neo.hazardous == 'Y':
            result.neo.hazardous == 'True'
        else:
            result.neo.hazardous == 'False'
        """Organize values into list for each close approach in prepartion
        for writing to a single row entry"""
        result = [result.time, result.distance, result.velocity,
                  result._designation, result.neo.name, result.neo.diameter,
                  result.neo.hazardous]
        # Write each close approach, row by row, to csv file
        writer.writerow(result)


def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    # Create list to be filled with close approach data in dictionary format
    data = []

    """Check for missing values and update values from results stream to make
    more readable"""
    for result in results:
        if result.neo.name is None:
            result.neo.name == ''
        if result.neo.diameter is None:
            result.neo.diameter = 'NaN'
        if result.neo.hazardous == 'Y':
            result.neo.hazardous = bool(1)
        else:
            result.neo.hazardous = bool(0)

        """ Organize values into dictionary for each close approach in prepartion
        for writing to JSON format

        Also convert values to specific data types.
        """
        result_dict = {
            'datetime_utc': result.time_str,
            'distance_au': float(result.distance),
            'velocity_km_s': float(result.velocity),
            'neo': {
                'designation': str(result.neo.designation),
                'name': result.neo.name,
                'diameter_km': float(result.neo.diameter),
                'potentially_hazardous': result.neo.hazardous
                }
          }
        data.append(result_dict)  # Write each close approach dict to "data"
        # list. Open new JSON file with filename provided by user
    with open(filename, 'w') as json_file:
        # Write "data" list to JSON file in JSON format
        json.dump(data, json_file)

"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach

# Path for testing CSV file
neo_csv_path = 'data\\neos.csv'


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    list_neos = []

    with open(neo_csv_path, 'r') as infile:
        reader = csv.DictReader(infile)  # Each row is stored as a dictionary
        for row in reader:
            # pdes - the primary designation of the NEO. This is a unique
            # identifier in the database, and its "name" to computer systems.
            designation = row['pdes']
            name = None
            # Conditional value for 'name' if it is empty or and NOT 'None'
            if (row['name'] != '' and row['name'] is not None):
                # name - the International Astronomical Union (IAU) name
                # of the NEO. This is its "name" to humans.
                name = row['name']
            diameter = float('nan')
            # Conditional value for 'diameter' if it is empty or and NOT 'None'
            if (row['diameter'] != '' and row['diameter'] is not None):
                # diameter - the NEO's diameter (from an equivalent sphere)
                # in kilometers.
                diameter = float(row['diameter'])
            # pha - whether NASA has marked the NEO as a "Potentially
            # Hazardous Asteroid,"
            hazardous = row['pha']
            # Create class instance for each neo
            neo = NearEarthObject(designation, name, diameter, hazardous)
            list_neos.append(neo)  # Add each neo to list: list_neos
        return list_neos


# Path for testing JSON file
cad_json_path = 'data\\cad.json'


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close
    approaches.
    :return: A collection of `CloseApproach`es.
    """
    list_approaches = []

    with open(cad_json_path, 'r') as infile:
        contents = json.load(infile)  # Parse JSON data into a Python object
        for row in contents['data']:  # Each row is actually a list of values
            # des - primary designation of the asteroid or comet (e.g., 443,
            # 2000 SG344)
            designation = row[0]
            # cd - time of close-approach (formatted calendar date/time, in
            # UTC)
            time = row[3]
            distance = row[4]  # dist - nominal approach distance (au)
            # v_rel - velocity relative to the approach body at close approach
            # (km/s)
            velocity = row[7]
            # Create class instance for each cad
            cad = CloseApproach(designation, time, distance, velocity)
            # Add each cad to list: list_approaches
            list_approaches.append(cad)
        return list_approaches

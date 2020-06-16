import argparse
import csv
from datetime import datetime
import os


class BMIRange:

    def __init__(self, value, lower_threshold=0.0, upper_threshold=None):
        self.lower_threshold = lower_threshold
        self.upper_threshold = upper_threshold
        self.value = value


bmi_ranges = [
    BMIRange('underweight', upper_threshold=18.5),
    BMIRange('normal', 18.5, 25),
    BMIRange('overweight', 25, 30),
    BMIRange('obese', 30),
]


def get_bmi_range(bmi):
    """
    Gets the bmi range for a given value.

    Args:
        * `bmi` - `float`

    Returns:
        `BMIRange` instance
    """
    for bmi_range in bmi_ranges:
        # handles obese range
        if not bmi_range.upper_threshold and bmi >= bmi_range.lower_threshold:
            return bmi_range
        # handles all other ranges
        if bmi_range.lower_threshold <= bmi <= bmi_range.upper_threshold:
            return bmi_range


def get_bmi(height, weight):
    """
    Converts height and weight into a bmi range.

    Args:
        * `height` - `float` - height in meters
        * `weight` - `float` - weight in kilograms

    Returns:
        `float`
    """
    return weight / (height ** 2)


def imperial_to_metric(height, weight):
    """
    Converts imperial system height and weight into metric system height and
    weight.

    Args:
        * `height` - `float` - height in feet
        * `weight` - `float` - weight in stone

    Returns:
        `tuple` - (height, weight)
    """
    # convert stuff
    height = height / 3.28
    weight = weight * 6.35
    return height, weight


def write(first_name, surname, data):
    first_name = first_name.lower()
    surname = surname.lower()

    # If the measurements folder doesn't exist, make it
    project_root = os.path.dirname(os.path.realpath(__file__))
    measurements_dir = project_root + '/measurements/'
    if not os.path.exists(measurements_dir):
        os.makedirs(measurements_dir)

    # Convert the name and surname into filename
    filename = surname + '_' + first_name + '.csv'

    # Add the data as a row to the file
    fields = ['Date', 'Range', 'Value']
    with open(measurements_dir + filename, 'a+', newline='') as csv_file:
        dict_writer = csv.DictWriter(csv_file, fieldnames=fields)
        # %x Locale’s appropriate date representation
        # %X Locale’s appropriate time representation
        display_date_time = datetime.now().strftime('%x - %X')
        data = {
            'Date': display_date_time,
            'Range': data[0],
            'Value': data[1],
        }
        dict_writer.writerow(data)


def check_positive(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError("%s is an invalid positive int value" % value)
    return ivalue


parser = argparse.ArgumentParser(
    description='Calculates body mass index (BMI)'
)
parser.add_argument(
    'first name',
    type=str,
    help='The first name of the person being measured.'
)
parser.add_argument(
    'surname',
    type=str,
    help='The surname of the person being measured.'
)
parser.add_argument(
    'height',
    type=float,
    help='Height in meters'
)
parser.add_argument(
    'weight',
    type=float,
    help='Weight in kilograms'
)
parser.add_argument(
    '--imperial',
    action='store_true',
    help=(
        'Uses imperial system instead of metric system for weight and height. '
        '(height: feet, weight: stone)'
    ),
)
parser.add_argument(
    '--decimal',
    type=int,
    default=2,
    help='Rounds bmi value to given number of decimal places.',
)

parser.add_argument(
    '-w',
    '--write',
    help='Write to file (defaults to CSV file)',
    action='store_true'
)


args = parser.parse_args()
if args.imperial:
    height, weight = imperial_to_metric(args.height, args.weight)
else:
    height, weight = args.height, args.weight


bmi = get_bmi(height, weight)
bmi_range = get_bmi_range(bmi)
rounded_value = round(bmi, args.decimal)

if args.write:
    data = [bmi_range.value, rounded_value]
    write(args.first_name, args.surname, data)
    print('Data has been written to the measurements folder')
else:
    output_string = 'Your BMI is {} which means you are {}.' \
        .format(rounded_value, bmi_range.value)
    print(output_string)
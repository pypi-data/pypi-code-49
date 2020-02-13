#!/usr/bin/env python

import argparse
import pendulum
import random

def main():
    parser = argparse.ArgumentParser(
        description='Tools for helping to work with vehicles in our web services')
    parser.add_argument('-reg', '--registration-number',
                        action='store_true',
                        help='generates a random registration number for a vehicle')
    parser.add_argument('-vin', '--vehicle-identification-number',
                        action='store_true',
                        help='generates a random vehicle identification number')
    parser.add_argument('--age-from-days',
                        action='store',
                        type=int,
                        help='displays the date of the vehicle from how old it is in days from today')
    parser.add_argument('--age-from-date',
                        action='store',
                        type=str,
                        help='displays the date of the vehicle from how old it is in days from today')

    args = parser.parse_args()

    if args.registration_number:
        print(f'{randString(2)}{randString(2,"0123456789")}{randString(3)}')

    if args.vehicle_identification_number:
        print(randString(17,"ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"))

    if args.age_from_days is not None:
        today = pendulum.today()
        registration_date = today.subtract(days=args.age_from_days)
        print(registration_date)

    if args.age_from_date is not None:
        today = pendulum.today()
        registration_date = pendulum.parse(args.age_from_date)
        date_diff_in_days = today.diff(registration_date).in_days()
        print(date_diff_in_days)

def randString(length=5, character_set='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    return ''.join((random.choice(character_set) for i in range(length)))

if __name__ == "__main__":
    main()

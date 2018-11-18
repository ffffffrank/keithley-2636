#!/usr/bin/env python
# coding:utf-8
"""
  Author:  Ross Warren <peregrine dot warren at physics dot ox dot ac dot uk>
  Purpose: Run OFET measurements remotely with simple CLI interface
  Created: 17/11/18
"""

from argparse import ArgumentParser
import k2636
import time

def main(args):
    try:
        # Set up
        keithley = k2636.K2636()
        begin_measure = time.time()
        # Measurements
        keithley.IVsweep(args.file[0])
        keithley.Output(args.file[0])
        keithley.Transfer(args.file[0])
        # Finish
        keithley.closeConnection()
        finish_measure = time.time()
        print('-------------------------------------------\nAll measurements complete. Total time % .2f mins.'
              % ((finish_measure - begin_measure) / 60))

    except ConnectionError:
        print('MEASUREMENT ERROR: Measurement could not be made due to connection issues.')

if __name__ == '__main__':
    parser = ArgumentParser(description=__doc__)
    parser.add_argument('file', nargs='+', help='File name to write to')
    args = parser.parse_args()
    main(args)
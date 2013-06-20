#!/usr/bin/env python

import os
import subprocess
import argparse
import sys
import time

multiple_fruitstrap_location = os.path.dirname(os.path.realpath(__file__))

def set_up_parser():
    parser = argparse.ArgumentParser(description='Transfer .app to all connected iOS devices.')
    parser.add_argument('--app', '-a', action='store', required=True, help='location of .app (cannot be an .ipa)')
    parser.add_argument('--delay', '-d', action='store', type=int, help='Adds a delay to the end of the script for help in automating')

# now parser args
    args = parser.parse_args()

    return args

def get_device_udids():
    print 'multiple_fruitstrap_location: ' + multiple_fruitstrap_location
    multiple_device_script = multiple_fruitstrap_location + '/connected_udids.sh'
    print 'multiple_device_script: ' + multiple_device_script
    udid_scraper = subprocess.Popen(["sh", multiple_device_script], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    udids = udid_scraper[0].split()
    print udids
    return udids

def transfer_app(udid, app_location):
    fruitstrap_script = multiple_fruitstrap_location + '/fruitstrap'
    #transporter = subprocess.Popen([fruitstrap_script, '-i', udid, '-b', app_location], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    transporter = subprocess.Popen([fruitstrap_script, '-i', udid, '-b', app_location], stdout=sys.stdout, stderr=sys.stderr).communicate()
#print transporter

def post_process(args):
    print "DONE! now do postprocessing"
    if args.delay:
        time.sleep(args.delay)

def main():
    args = set_up_parser()
    udids = get_device_udids()
    for udid in udids:
        transfer_app(udid, args.app)
    post_process(args)
    print 'end of multiple_fruitstrap'

if __name__ == '__main__':
    main()
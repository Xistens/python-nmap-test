#!/usr/bin/python3
import sys
import argparse
import nmap3

def parse_args(args):
    """ Create the arguments """
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", dest="ports", help="Ports to scan")
    parser.add_argument("-f", dest="file", help="File to open")

    return parser.parse_args(args)

args = parse_args(sys.argv[1:])
# https://stackoverflow.com/questions/11109859/pipe-output-from-shell-command-to-a-python-script                                                 
if not sys.stdin.isatty():
    input_stream = sys.stdin
else:
    input_stream = open(args.file, "r").readlines()
                                           

ports = '-p-' if not args.ports else f"-p{args.ports}"
for line in input_stream:
    print(f"Starting scan on: {line.strip()} with port command: {ports}")
    nmap = nmap3.NmapScanTechniques()
    result = nmap.nmap_syn_scan(line, args=ports)

    f = list(result.keys())[0]
    print(f)
    for i in result[f]:
        print(f"{i['portid']} Status: {i['state']}")
    print()

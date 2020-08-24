#!/usr/bin/python3
import sys
import ipaddress
import argparse
import netifaces
from netaddr import IPNetwork
import nmap3
"""
Requirements:
https://pypi.org/project/python3-nmap/
netifaces
netaddr
"""

def get_ip(ifname):
    """
    Get ip addr and subnet mask from ifname
    """
    addr = netifaces.ifaddresses(ifname)[netifaces.AF_INET][0]['addr']
    subnet = netifaces.ifaddresses(ifname)[netifaces.AF_INET][0]['netmask']
    return (addr, subnet)

def netmask_to_cidr(m_netmask):
    """
    Convert netmask to cidr

    https://gist.github.com/Akendo/6cf70aa01f92ab2f03ae6c27480f713e
    """
    return(sum([ bin(int(bits)).count("1") for bits in m_netmask.split(".") ]))


def main(args):
    addr = None
    network = None


    if args.ifname:
        addr, subnet = get_ip(args.ifname)
        network = str(IPNetwork(f"{addr}/{subnet}").cidr)
    elif args.subnet:
        network = args.subnet

    # Simple test, for more info: https://pypi.org/project/python3-nmap/
    nmap = nmap3.NmapHostDiscovery()
    results = nmap.nmap_no_portscan(network)
    for i in results['hosts']:
        print(i['addr'], file=sys.stdout)


def parse_args(args):
    """ Create the arguments """
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", dest="ifname", help="Interface to scan")
    parser.add_argument("-I", dest="subnet", help="Subnet. Ex: 10.10.1.0/24")
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    return parser.parse_args(args)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args)

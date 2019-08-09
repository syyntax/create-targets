#!/usr/bin/python

"""
Title:          create-targets
Description:    Create target list
Author:         Jason G. Scott (@syynt4x)
Email:          syyntax@protonmail.com
Date:           24 Jan 2019
Version:        2019.01.24
"""

import argparse, os, re, ipaddress as addr, random as r

# VARIABLES
script_path = os.path.dirname(os.path.abspath(__file__))  # File path of this script
regIP4 = re.compile(
    "^(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)){3}(/(3[012]|[12]\d|\d))$")
regIP6 = re.compile(
    "(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|("
    "[0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}"
    ":){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]"
    "{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:)"
    "{0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:)"
    "{1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))"
)

color_dict = {"red":"\033[1;31m", "yellow":"\033[1;33m", "green":"\033[1;32m", "blue":"\033[1;34m", "cyan":"\033[1;36m",
              "white":"\033[1;37m", "black":"\033[1;30m", "bold":"\033[1m", "underline":"\033[4m", "off":"\033[0;0m"}

parser = argparse.ArgumentParser(description="Generate a target list of IPv4 or IPv6 addresses based off a provided "
                                             "subnet.")
parser.add_argument("-r", "--random", action="store_true", help="Randomize the target list.", dest="random",
                    default=False)
parser.add_argument("-n", "--net", action="store", help="Network range to generate (e.g. 192.168.1.0/24)", dest="net",
                    default=None, metavar="RANGE")
parser.add_argument("--ipv6", action="store_true", help="Use IPv6 addressing (default is IPv4).", dest="ipv6",
                    default=False)
parser.add_argument("-x", "--exclude", action="store", help="Exclude a comma-delimited list of IP addresses (e.g. "
                                                            "192.168.1.1,192.168.1.2,...). Do not use spaces.",
                    dest="exclude", default=None, metavar="LIST")
parser.add_argument("-xl", "--exclude-list", action="store", help="Exclude a file containing newline-delimited IP"
                                                                  " addresses.", dest="excludelist", default=None,
                    metavar="FILE")
parser.add_argument("-o", "--out", action="store", help="Output results to a file.", dest="outfile", default=None,
                    metavar="FILE")
args = parser.parse_args()


def col(color, text):
    return "{}{}{}".format(color_dict[color], text, color_dict["off"])


def span_ip(ip_range, random):
    '''
    if args.ipv6 is False:
        network = addr.IPv4Network(u'{}'.format(ip_range))

    else:
        network = addr.IPv6Network(u'{}'.format(ip_range))
    '''
      
    network = addr.ip_network(u'{}'.format(args.net), False)

    network_list_temp = list(network.hosts())
    network_list = [str(network_list_temp[i]) for i in range(len(network_list_temp))]

    if random is True:
        r.shuffle(network_list)

    return network_list


def create_list():

    if args.ipv6 is True:
        reg_ip = regIP6

    else:
        reg_ip = regIP4

    if args.outfile is None:
        outfile = os.path.abspath(os.path.join(".", "targets.list"))

    else:
        outfile = os.path.abspath(args.outfile)

    if args.net is None:
        return "\n{} You must provide a CIDR network range to generate a list of IPs.  Use '--help' to see more" \
               " options.\n".format(col("red", "ERROR:"))

    elif not re.match(reg_ip, args.net):
        return "\n{} The network you specified is an invalid network range: {}\n".format(col("red", "ERROR:"),
                                                                                         col("yellow", args.net))

    else:
        network_list = span_ip(args.net, args.random)

        if args.exclude:
            exclude_list = args.exclude
            exclude_list = exclude_list.split(',')
            network_list = [x for x in network_list if x not in exclude_list]

        if args.excludelist:
            file_xl = open(args.excludelist, 'r')
            xllist = file_xl.readlines()
            xllist = [i.replace('\n', '') for i in xllist]
            network_list = [x for x in network_list if x not in xllist]
            file_xl.close()

        f = open(outfile, 'w')

        for i in network_list:
            f.write("{}\n".format(i))

        f.close()

        return "\nTarget list created:  {}\n".format(col("blue", outfile))


print(create_list())

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# easywifishare : mainfile

#import cli.app # probably not necessary
import sys
import os
from optparse import OptionParser
from tabulate import tabulate
import argparse
from termcolor import colored
import subprocess

mainDir = os.path.dirname(os.path.realpath(__file__))

usage = "usage: %prog [ [ [ -a | --auth ] <Auth Method> ]  [ [ -n | --name ] <Network Name> ]  [ [ -p | --passwd ] <password> ] [ -l | --logo | --no-logo ]  ]"
parser = OptionParser(usage=usage, version="%prog 0.1")


parser.add_option("-a",  "--auth",          help="Set authentication method (wep, wep2, wpa, wpa2).", default="wpa2", action="store", dest="authMethod")
parser.add_option("-n",  "--name",          help="Set the network name",                              default=False,  action="store", dest="networkName")
parser.add_option("-p",  "--passwd",        help="Set password",                                      default=False,  action="store", dest="passwd")
parser.add_option("--logo",          help="Print the Wi-Fi Alliance(tm) logo.",                default=True,   action="store_true", dest="logo")
parser.add_option("--no-logo",              help="Dont print the Wi-Fi Alliance(tm) logo.",           default=False,  action="store_true", dest="logo")
parser.add_option("-i",  "--ignore-advice", help="Ignore auth advice.",                               default=True,   action="store_true", dest="advice")

(options, args) = parser.parse_args()

def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")


allowedAuthMethods = ["wep", "wep2", "wpa", "wpa2"]

if len(sys.argv) < 2:
    "Please see documentation of easywifishare before using it."
    sys.exit(1)

if (options.networkName == False):
    print("Please specify network name using --name option or see --help for help.")
    sys.exit(1)

if (options.authMethod not in ["wep", "wep2", "wpa", "wpa2"]) and (options.advice == False):
    answer = query_yes_no("The “" + options.authMethod + "” authentication method you chose isn’t knowen. Would you like to continue", "no")
    if answer == False:
        sys.exit(1)


formatedwifilink = "WIFI:S:" + options.networkName + ";T:" + options.authMethod+ ";"

texargs = "\\newcommand\\wifiname{" + options.networkName +"}" + " "
texargs = texargs + "\\newcommand\\wifiauthtype{" + options.authMethod +"}" + " "

if options.passwd != False:
    formatedwifilink = formatedwifilink + "P:" + options.passwd + ";;"
    texargs = texargs + "\\newcommand\\wifipassword{" + options.passwd +"}" + " "
else:
    formatedwifilink = formatedwifilink + ";"

texcommand = "xelatex -jobname=wifi-" + options.networkName + " " + " " + texargs + " "  + " " + "\\input{" +  mainDir + "/" + "main.tex" + "}"

subprocess.Popen(texcommand.split())

sys.exit(1)

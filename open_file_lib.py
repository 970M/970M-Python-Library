"""Module Lecture/Ecriture fichiers"""

import argparse


parser = argparse.ArgumentParser()

parser.add_argument("host")
parser.add_argument("-c", "--clean", action="store_true", required=False)

args = parser.parse_args()
print(args)

print("Configure host", args.host)

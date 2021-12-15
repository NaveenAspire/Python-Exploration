import argparse

parser= argparse.ArgumentParser(description="Argparser Usage")

#Positional arguments
parser.add_argument('name',type=str, help='Name of the Programmer')


#Optional arguments
parser.add_argument('--mobile', type=str, required=True, help='Name of the mobile')
args = parser.parse_args()

print(args.name+"'s mobile brand is "+args.mobile)
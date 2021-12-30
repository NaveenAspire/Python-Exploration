"""This is Practice for argarser"""
import argparse

parser = argparse.ArgumentParser(description="Argparser Usage")

# # Positional arguments
# parser.add_argument("name", type=str, help="Name of the Programmer")


# # Optional arguments
# parser.add_argument("--mobile", type=str, default="Samsung", help="Name of the mobile")
# parser.set_defaults(mobile="Apple")
# print(parser.get_default("mobile"))
# args = parser.parse_args()

# print(args.name + "'s mobile brand is " + args.mobile)


# Subparsers

subparser = parser.add_subparsers(dest="Gadget")
mobile = subparser.add_parser("mobile")
laptop = subparser.add_parser("laptop")

mobile.add_argument("--name", default="Samsung")
laptop.add_argument("--name", default="Acer")

args = parser.parse_args()

if args.Gadget == "mobile":
    print("Naveen's mobile brand is : ", args.name)

elif args.Gadget == "laptop":
    print("Naveen's laptop brand is  : ", args.name)

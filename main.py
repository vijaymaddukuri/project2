
from argparse import ArgumentParser
import json



def setup_args():
    parser = ArgumentParser(description='Arguments for talking to vCenter')

    parser.add_argument('-d', '--data',
                        required=True,
                        action='store',
                        help='UDM recom data')
    args = parser.parse_args()
    return args


def main():
    args = setup_args()
    data = json.loads(args.data)
    print(data)
    print(type(data))



# Start program
if __name__ == "__main__":
    main()
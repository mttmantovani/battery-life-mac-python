from datetime import date, timedelta
from sys import argv, stdout

import argparse

start = date(2017, 1, 10)
today = date.today()
max_cycles = 1000

def battery_life(cycles):
    final = start + timedelta(days=max_cycles/(cycles/(today - start).days))
    return final.strftime("%d %h %Y")


if __name__=='__main__':
    parser = argparse.ArgumentParser(description='Battery life utility.')
    parser.add_argument('--output', '-o', nargs='?', 
                        type=argparse.FileType('a+'), default=stdout,
                        help='Specifies output file.')
    parser.add_argument('--cycles', type=str, help='Battery cycle count.')
    parser.add_argument('--capacity', type=str, help='Full battery capacity.')
    parser.add_argument('--design-capacity', type=str, 
                        help='Design battery capacity.')
    args = parser.parse_args()

    data = {'date': today.strftime("%d %h %Y"),
            'cycles': args.cycles if args.cycles else '\t',
            'final': battery_life(int(args.cycles)) if args.cycles is not None else '\t',
            'capacity': args.capacity if args.capacity else '\t',
            'design_capacity': args.design_capacity if args.design_capacity else '\t',
            }
    
    if args.output is not stdout:
        with open(args.output.name, 'a+') as f:
            #f.write(f'{today.strftime("%d %h %Y")},{cycles},{final},{capacity},{design_capacity}\n')
            f.write(',\t\t\t'.join(data.values())+'\n')
    else:
        # TODO: write nicely to stdout
        pass






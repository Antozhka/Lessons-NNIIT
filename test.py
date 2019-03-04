import argparse
from datetime import datetime

now = datetime.now()

name_dir = ''

parser = argparse.ArgumentParser()
parser.add_argument('-y', '--year', action="store_true",  help='the Year in the name of new Dir')
parser.add_argument('-m', '--month', action="store_true",  help='the Month in the name of new Dir')
parser.add_argument('-d', '--day', action="store_true",  help='the Day in the name of new Dir')
parser.add_argument('path', type=str, help='the Path to new Dir')

args = parser.parse_args()

print(args)
if args.year:
    name_dir += str(now.year) + '-'
if args.month:
    name_dir += str(now.month) + '-'
if args.day:
    name_dir += str(now.day)
if not args.year and not args.month and not args.day:
    name_dir = 'unknown'

from os.path import exists
from os import mkdir

if exists(args.path + '\\' + name_dir):
    print('Такая папка уже существует')
elif exists(args.path):
    mkdir(args.path + '\\' + name_dir)
else:
    mkdir(args.path)
    mkdir(args.path + '\\' + name_dir)

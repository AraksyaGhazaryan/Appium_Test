import argparse
import subprocess

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('--test', choices=['Start_page','\n',
                                       'Game_page','\n',
                                       'End_page','\n' ],
                    help='Choose name for run test')
parser.add_argument('pytest', choices=['Yes', 'No'],)
args = parser.parse_args()

if(args.test == 'Start_page'):
    subprocess.call(['pytest', r'.\venv\tests\test_for_start_page.py'], shell=True)
elif(args.test == 'Game_page' ):
    subprocess.call(['pytest', r'.\venv\tests\test_for_game_page.py'], shell=True)
elif(args.test == 'End_page' ):
    subprocess.call(['pytest', r'.\venv\tests\test_for_end_page.py'], shell=True)
    subprocess.call(['pytest', 'tests/test_for_start_page.py'], shell=True)



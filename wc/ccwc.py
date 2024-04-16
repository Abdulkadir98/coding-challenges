import argparse
import os
import sys

def main():
    parser = argparse.ArgumentParser()
    # If data is not being piped through stdin
    if sys.stdin.isatty():
        parser.add_argument('filename')
    parser.add_argument('-c', action='store_true')
    parser.add_argument('-l', action='store_true')
    parser.add_argument('-w', action='store_true')
    args = parser.parse_args()
    try:
        filename = args.filename
    except AttributeError:
        filename = ""
    content = read_file(filename) if filename else sys.stdin.read()
    count_bytes = args.c
    count_lines = args.l
    count_words = args.w

    if count_bytes:
        file_stats = os.stat(filename)
        print(f'{file_stats.st_size} {filename}')
    
    elif count_lines:
        print(f'{countlines(content)} {filename}')

    elif count_words:
        print(f'{countWords(content)} {filename}')

    else:
        print(f'{file_stats.st_size} {countlines(content)} {countWords(content)} {filename}')


def countlines(content):
    return len(content.splitlines())
    
def countWords(content):
    words_count = 0
    lines = content.splitlines()
    for line in lines:
        words = line.split()
        words_count += len(words)
    
    return words_count

def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()




if __name__ == "__main__":
    main()
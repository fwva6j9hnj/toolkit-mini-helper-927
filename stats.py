import sys

def word_count(text):
    return {w: text.split().count(w) for w in set(text.split())}

if __name__ == '__main__':
    print(word_count(sys.stdin.read().lower()))

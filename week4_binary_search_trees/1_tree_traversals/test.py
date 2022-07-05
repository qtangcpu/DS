import sys, threading


def main():
    for i in range(5):
        [a, b, c] = map(int, sys.stdin.readline().split())
        print(a,b,c)
threading.Thread(target=main).start()
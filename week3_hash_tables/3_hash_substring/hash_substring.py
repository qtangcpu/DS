# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def areEqual(text_seg,pattern):

    if text_seg != pattern:
        return False
    return True

def _hash_func(s):
    ans = 0
    for c in reversed(s):
        ans = (ans * 11 + ord(c)) % 10000001
    return ans
def precomputeHashes(pattern, text):
    size_p = len(pattern)
    size_t = len(text)
    H = [-1] *(size_t - size_p+1)
    H[size_t-size_p] = _hash_func(text[size_t-size_p:])
    y = 1
    for i in range(size_p):
        y = (y*11)% 10000001           #p为500001
    for i in range(size_t-size_p-1,-1,-1):
        H[i] = (11*H[i+1] + ord(text[i]) - y*ord(text[i+size_p])) % 10000001
    return H

def get_occurrences(pattern, text):
    result = []
    H  =precomputeHashes(pattern, text)
    pH = _hash_func(pattern)
    for i in range(len(text)-len(pattern)+1):
        if H[i] != pH:
            continue
        if areEqual(text[i:i+len(pattern)],pattern):
            result.append(i)
    return result


if __name__ == '__main__':

    print_occurrences(get_occurrences(*read_input()))


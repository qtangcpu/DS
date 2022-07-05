# python3



'''
def windowMax(listi, m):
    # the part of this list at positions >= qs is a deque
    # with elements monotonically decreasing.  Each one
    # may be the max in a window at some point
    q = []
    qs = 0

    listo=[]
    for i in range(len(listi)):

        # remove items from the end of the q that are <= the new one
        while len(q) > qs and listi[q[-1]] <= listi[i]:
            del q[-1]

        # add new item
        q.append(i)

        if i >= m-1:
            listo.append(listi[q[qs]])
            # element falls off start of window
            if i-q[qs] >= m-1:
                qs+=1

        # don't waste storage in q. This doesn't change the deque
        if qs > m:
            del q[0:m]
            qs -= m
    return listo
    '''
def windowMax2(list1,m):
    max = []
    answer = []
    for i in range(m):
        if len(max)==0:
            max.append(i)
        else:
            while max and list1[max[-1]] < list1[i]:
                max.pop()
            max.append(i)
    answer.append(list1[max[0]])
    for i in range(m,len(list1)):
        if max[0] == i-m:
            max.pop(0)

        if len(max)==0:
            max.append(i)
        else:
            while max and list1[max[-1]] < list1[i]:
                max.pop()
            max.append(i)
        answer.append(list1[max[0]])
    return answer
if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*windowMax2(input_sequence, window_size))


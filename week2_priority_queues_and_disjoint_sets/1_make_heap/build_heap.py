# python3
def left_child(i,size):
    return 2*i
def right_child(i,size):
    return 2*i+1
def sift_down(l,i,size):
    swap = []
    min_index = i
    left = left_child(i,size)
    if left <= size and l[left-1] < l[min_index-1]:
        min_index = left
    right = right_child(i, size)
    if right <= size and l[right-1] < l[min_index-1]:
        min_index = right
    if i != min_index:
        swap.append([i-1,min_index-1])
        a = l[i-1]
        l[i-1] = l[min_index-1]
        l[min_index-1] = a
        swap += sift_down(l,min_index,size)

    return swap
def build_heap(data):

    swaps = []
    size = len(data)
    for i in range(int(len(data)//2), 0,-1 ):
        swaps += sift_down(data,i,size)
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i,j in swaps:
        print(i,j)


if __name__ == "__main__":
    main()

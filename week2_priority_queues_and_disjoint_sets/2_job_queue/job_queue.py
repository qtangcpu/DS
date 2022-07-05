# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])
# 先创建一个长度为n_workers的min_heap，初始值全部为0，再创建一个长度为n_worker的list，记录每一个thread的编号以及在之后变换时，记录编号排序
#每一个新任务进来是，把时间加在root上，在sift——down,再同步当前root的编号
def left_child(i,size):
    return 2*i
def right_child(i,size):
    return 2*i+1
def sift_down(l,index,i,size):
    min_index = i
    left = left_child(i,size)
    if left <= size and (l[left-1] < l[min_index-1] or(l[left-1] == l[min_index-1] and index[left-1] < index[min_index-1])):
        min_index = left
    right = right_child(i, size)
    if right <= size and (l[right-1] < l[min_index-1] or (l[right-1] == l[min_index-1] and index[right-1] < index[min_index-1])):
        min_index = right

    if i != min_index:
        a = l[i-1]
        l[i-1] = l[min_index-1]
        l[min_index-1] = a
        b = index[i - 1]
        index[i - 1] = index[min_index - 1]
        index[min_index - 1] = b
        sift_down(l,index ,min_index,size)

    return l,index

def assign_jobs(n_workers, jobs):
    result = []
    workload = [0]*n_workers
    index = [i for i in range(n_workers)]
    for job in jobs:
        result.append([index[0],workload[0]])
        workload[0] += job
        workload,index = sift_down(workload,index,1,n_workers)

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for i,j in assigned_jobs:
        print(i, j)


if __name__ == "__main__":
    main()

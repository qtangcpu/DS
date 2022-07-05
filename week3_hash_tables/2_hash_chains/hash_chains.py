# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007
    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.d = [[] for i in range(self.bucket_count)]
    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):

        if query.type == "check":
            # use reverse order, because we append strings to the end
            print(' '.join(reversed(self.d[query.ind])))
        else:
            if query.type == 'find':
                i = 0
                while i <len(self.d[self._hash_func(query.s)]):
                    if self.d[self._hash_func(query.s)][i] == query.s:
                        print('yes')
                        break
                    else:
                        i+= 1
                if i >= len(self.d[self._hash_func(query.s)]):
                    print('no')
            elif query.type == 'add':
                i = 0
                while i < len(self.d[self._hash_func(query.s)]):
                    if self.d[self._hash_func(query.s)][i] == query.s:
                        break
                    else:
                        i += 1
                if i >= len(self.d[self._hash_func(query.s)]):
                    self.d[self._hash_func(query.s)].append(query.s)
            else:
                if len(self.d[self._hash_func(query.s)]) != 0:
                    for i in self.d[self._hash_func(query.s)]:
                        if i == query.s:
                            self.d[self._hash_func(query.s)].remove(i)
                            break

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()

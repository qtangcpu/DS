# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def hash_func(phone_number):
    a = 32
    b = 9
    p = 1
    hash = phone_number//p
    return hash

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = [[] for i in range(10000000)]
    for cur_query in queries:
        if cur_query.type == 'add':
            i = 0
            while i < len(contacts[hash_func(cur_query.number)]):
                if contacts[hash_func(cur_query.number)][i][0] == cur_query.number:
                    contacts[hash_func(cur_query.number)][i][1] = cur_query.name
                    break
                else:
                    i +=1
            if i >= len(contacts[hash_func(cur_query.number)]):
                contacts[hash_func(cur_query.number)].append([cur_query.number, cur_query.name])

        elif cur_query.type == 'del':
            if len(contacts[hash_func(cur_query.number)]) != 0:
                for i in contacts[hash_func(cur_query.number)]:
                    if i[0] == cur_query.number:
                        contacts[hash_func(cur_query.number)].remove(i)
                        break
        else:
            response = 'not found'
            result.append(response)
            if len(contacts[hash_func(cur_query.number)]) != 0:
                for i in contacts[hash_func(cur_query.number)]:
                    if i[0] == cur_query.number:
                        result[-1] = i[1]
                        break
    return result

def process_queries2(queries):
    contacts = {}
    result = []
    for cur_query in queries:
        if cur_query.type == 'add':
            contacts[cur_query.number] =cur_query.name
        elif cur_query.type == 'del':
            if cur_query.number in contacts:
                contacts.pop(cur_query.number)
        else:
            response = 'not found'
            if cur_query.number in contacts:
                response = contacts[cur_query.number]
            result.append(response)
    return result
if __name__ == '__main__':
    write_responses(process_queries(read_queries()))


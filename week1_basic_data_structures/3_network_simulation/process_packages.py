# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = [0]
    def process(self, request):
        i = 0
        while i < (len(self.finish_time)):
            if self.finish_time[i] <= request[0]:
                self.finish_time.pop(i)
            else:
                break
        if len(self.finish_time) < self.size:
            if len(self.finish_time) >= 1:
                finish = self.finish_time[-1] + request[1]
                self.finish_time.append(finish)
                return Response(False,self.finish_time[-2])
            else:
                finish = request[0] + request[1]
                self.finish_time.append(finish)
                return Response(False, request[0])

        return Response(False, -1)


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()

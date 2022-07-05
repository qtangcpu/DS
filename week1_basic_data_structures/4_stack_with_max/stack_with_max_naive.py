#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.aux_stack = []
    def Push(self, a):
        self.__stack.append(a)
        if len(self.aux_stack) == 0:
            self.aux_stack.append(a)
        elif a >= self.peek_aux():
            self.aux_stack.append(a)

    def peek_aux(self):
        assert (len(self.__stack))
        return self.aux_stack[-1]

    def Pop(self):
        assert (len(self.__stack))
        if self.__stack.pop() == self.peek_aux():
            self.aux_stack.pop()

    def Max(self):
        assert (len(self.__stack))
        return self.peek_aux()


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)

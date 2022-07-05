# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))
        def add_tree(self):
            self.nodes = []
            for i in range(self.n):
                self.nodes.append([])
            for i in range(self.n):
                parent_index = self.parent[i]
                if parent_index == -1:
                    self.root = i
                else:
                    self.nodes[parent_index].append(i)
        def compute_height(self,r):
                # Replace this code with a faster implementation
                max_height = 0
                if len(self.nodes[r]) ==0:
                    return 1
                childs = self.nodes[r]
                for i in childs:
                    max_height = max(max_height,1 + self.compute_height(i))



                return max_height;

def main():
  tree = TreeHeight()
  tree.read()
  tree.add_tree()
  print(tree.compute_height(tree.root))

threading.Thread(target=main).start()

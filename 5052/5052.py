import sys


class Node(object):
    def __init__(self, key, fullStr=None):
        self.key = key
        self.fullStr = fullStr
        self.childCount = 0
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        currentNode = self.head
        # if node not exist,make node
        for char in string:
            if char not in currentNode.children:
                currentNode.children[char] = Node(char)
            currentNode = currentNode.children[char]
            currentNode.childCount += 1
        # set final node flag
        currentNode.fullStr = string

    def search(self, string):
        currentNode = self.head
        # jump to final node
        for char in string:
            if char in currentNode.children:
                currentNode = currentNode.children[char]
            else:
                return False
        # if flag is Not None
        if currentNode.fullStr:
            return True
        else:
            return False
    # return childCount
    def starts_with(self, prefix):
        currentNode = self.head
        words = []
        # jump to prefix node
        for p in prefix:
            if p in currentNode.children:
                currentNode = currentNode.children[p]
            else:
                return None
        return currentNode.childCount

testCases = int(sys.stdin.readline().rstrip())

for case in range(testCases):
    N = int(sys.stdin.readline().rstrip())
    trie = Trie()
    al = True
    stList = []
    for ix in range(N):
        st = sys.stdin.readline().rstrip()
        stList.append(st)
        trie.insert(st)
    for strr in stList:
        if trie.starts_with(strr)>1:
            al = False
    if al:
        print("YES")
    else:
        print("NO")
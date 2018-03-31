# Every TRIE Node
class Node :
    def __init__(self, char) :
        self.char = char
        self.children = {}
        self.leaf = False
        self.pos = set()


# TRIE structure
class Tree :
    def __init__(self) :
        self.root = Node(None)

    def addNode(self, morp, pos) :
        curNode = self.root
        for i, char in enumerate(morp) :
            # character of input morp works as a key to the entries of current Node.
            if char in curNode.children :
                curNode = curNode.children[char]
            else :
                newNode = Node(char)
                curNode.children[char] = newNode
                curNode = curNode.children[char]

            if ( i == len(morp)-1 ) :
                curNode.leaf = True
                curNode.pos.add(pos)

    # If morp exists in the TRIE, return its POS
    def searchMorp(self, morp) :
        curNode = self.root
        for i, char in enumerate(morp) :
            if char not in curNode.children :
                return False
            else :
                curNode = curNode.children[char]

            if ( i == len(morp)-1 and curNode.leaf == True ) :
                return curNode.pos
            elif (i == len(morp)-1 and curNode.leaf == False ) : # DOES exist, but not a leaf
                return False


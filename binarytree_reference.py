class BinaryTree(object):

    def __init__(self, rootObj):

        # Inititalise root, left nad right to None
        # Set key to root object
        self.key = rootObj
        self.leftChild = None
        self.RightChild = None

    def insertLeft(self, newNode):

        # Check if left node is empty
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:  # If, there's already a tree, we insert a new node and push the existing node one level down

            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):

        # Check if left node is empty
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)

        else:  # If, there's already a tree, we insert a new node and push the existing node one level down

            t = BinaryTree(newNode)
            t.RightChild = self.RightChild
            self.RightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

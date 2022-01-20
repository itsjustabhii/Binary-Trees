def preorder(tree):
    if tree != None:
        print(tree.getRootVal())
        preorder(tree.getLeftChild)
        preorder(tree.getRightChild)

def binarytree(r):
    return [r, [], []]


def insertLeft(root, newBranch):
    # Inserting Left with Index 1
    t = root.pop(1)

    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root


def insertRight(root, NewBranch):
    # Inserting Right with Index 2
    t = root.pop(2)

    if len(t) > 1:
        root.insert(2, [NewBranch, [], t])
    else:
        root.insert(2, [NewBranch, [], []])
    return root


# To get the root value
def getRootVal(root):
    return root[0]


# To set a new root value
def setRootVal(root, newVal):
    root[0] = newVal


# To get the value of Left Child
def getLeftChild(root):
    return root[1]


# To get the value of Right Child
def getRightChild(root):
    return root[2]

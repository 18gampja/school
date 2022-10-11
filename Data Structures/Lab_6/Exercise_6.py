
#############################
#       Assignment 6        #
#############################

class treeNode:
    def __init__(self, val = None):                     # Initializes a node/leaf
        self.right = None                               # Sets an initial value, as well as setting left and right values
        self.left = None                                # to none. Also sets val to none if no value is passed.
        self.val = val

    def insert(self, val):                              # Insertion method

        if self.val == None:                            # If the node is empty, inserts the value here
            self.val = val

        elif self.val > val:                            # Checks where to put it. Both then initialize the child being
            if self.left == None:                       # given a value, then inserting the value.
                self.left = treeNode()
                self.left.insert(val)
            
            else:
                self.left.insert(val)

        elif self.val < val or self.val == val:

            if self.right == None:
                self.right = treeNode()
                self.right.insert(val)

            else:
                self.right.insert(val)

    def findMax(self):                                  # Finds the maximum value in the tree starting at a certain point.

        if self.right == None:
            return self.val
        
        return self.right.findMax()

    def findMin(self):                                  # Same as findMax, just for the minimum value.

        if self.left == None:
            return self.val

        return self.left.findMin()

    def inOrder(self):                                  # Prints out the contents of the tree in order. In Order Traversal.

        vals = []
        
        if self.left != None and self.left.val != None:
            vals += (self.left.inOrder())

        print(self.val)
        vals.append(self.val)

        if self.right != None and self.right.val != None:
            vals += (self.right.inOrder())
        
        return vals

    def preOrder(self):                                 # Prints out the contents of the tree in pre order. Pre-Order Traversal.

        print(self.val)

        if self.left != None and self.left.val != None:
            self.left.preOrder()

        if self.right != None and self.right.val != None:
            self.right.preOrder()

    def postOrder(self):                                # Prints out the contents of the tree in post order. Post-Order Traversal.

        if self.left != None and self.left.val != None:
            self.left.postOrder()

        if self.right != None and self.right.val != None:
            self.right.postOrder()

        print(self.val)

    def searchTree(self, val):                          # Searches for a specific value

        if self.val == val:                             # The base case, returns the found value
            print (str(val) + " is in the tree.")
            print()
            return self
    
        elif(val > self.val and self.right != None):    # Checks to see if hte value is greater or less than the current node, adjusts search accordingly
            return self.right.searchTree(val)

        elif(val < self.val and self.left != None):
            return self.left.searchTree(val)

        else:                                           # Returns false if the value isn't found
            print(str(val) + " is not in the tree.")
            print()
            return False       

    def removeNode(self, val):                          # Removes a node
    
        if(self.searchTree(val) == False):              # Checks to see if the node exists, if not returns the same tree
            return tree

        else:

            pos = self.searchTree(val)                  # Uses the search function to find the value

            if pos.left == None:                        # These two handle the case of one or no children.
                if pos.right != None:                   # Set a temporary value to the child, even if that value is "None"
                    temp = pos.right.val                # Then move the temp value to the original node, removing the child value
                    pos.val = temp                      # or effectively removing/changing the original value
                    pos.right.val = None
                    return

                elif pos.right == None:
                    temp = pos.right
                    pos.val = temp
                    pos.right = None
                    return

            elif pos.right == None:
                if pos.left != None:
                    temp = pos.left.val
                    pos.val = temp
                    pos.left.val = None
                    return

                elif pos.left == None:
                    temp = pos.left
                    pos.val = temp
                    pos.left = None
                    return

            temp = pos.left.findMax()                   # This handles the case of two children. Basically does the same process,
                                                        # but over a couple of iterations until complete. It replaces the parent node
            pos.val = temp                              # with the largest node in the left sub tree, then removes that node.

            pos.left.removeNode(temp)

def mergeTrees(tree1, tree2):

    elems1 = tree1.inOrder()
    elems2 = tree2.inOrder()
    allElems = []

    sortElems(elems1, elems2, allElems)

    newBST = treeNode()
    for item in allElems:
        newBST.insert(item)

    return newBST

    
def sortElems(arr1, arr2, result):

    i = j = 0

    while (i < len(arr1) and j < len(arr2)):

        if(arr1[i] > arr2[j]):

            result.insert(len(result), arr2[j])
            j += 1

        else:

            result.insert(len(result), arr1[i])
            i += 1

    while(i < len(arr1)):

        result.insert(len(result), arr1[i])
        i += 1

    while(j < len(arr2)):

        result.insert(len(result), arr2[j])
        j += 1


tree = treeNode()
tree2 = treeNode()

tree.insert(5)
tree.insert(3)
tree.insert(2)
tree.insert(4)
tree.insert(7)
tree.insert(8)
tree.insert(6)
tree.insert(1)
tree.insert(9302)
tree.insert(9)
tree2.insert(1)
tree2.insert(2)
tree2.insert(3)
tree2.insert(4)
tree2.insert(5)
tree2.insert(6)
tree2.insert(7)
tree2.insert(8)
tree2.insert(9)
tree2.insert(10)
print()
tree.searchTree(2)
print()
tree.searchTree(10)
print()
tree.removeNode(5)
print("In Order:")
print()
tree.inOrder()
print()
print("Pre-Order:")
print()
tree.preOrder()
print()
print("Post-Order:")
print()
tree.postOrder()
print()
print("Merged Trees:")
print()
mergedTree = mergeTrees(tree, tree2)
mergedTree.inOrder()
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BinaryTree:
    def __init__(self):
        self.root = None
    
    def draw(self, root, level = 0):
        if root:
            print("\t" * level + str(root.val))
            self.draw(root.left, level + 1)
            self.draw(root.right, level + 1)

    # Insert in tree
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)
    
    def _insert(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    # Inorder Traversal
    def inorder_trverse(self):
        visited = []
        self._inorder_travers(self.root, visited)
        return visited
    
    def _inorder_travers(self, node, visited):
        if not node :
            return 
        
        self._inorder_travers(node.left, visited)
        visited.append(node.val)
        self._inorder_travers(node.right, visited)

    # preorder Trabersal
    def preorder_trverse(self):
        visited = []
        self._preorder_travers(self.root, visited)
        return visited
    
    def _preorder_travers(self, node, visited):
        if not node :
            return 
        
        visited.append(node.val)
        self._preorder_travers(node.left, visited)
        self._preorder_travers(node.right, visited)

    # Postorder Traversal
    def postorder_trverse(self):
        visited = []
        self._postorder_travers(self.root, visited)
        return visited
    
    def _postorder_travers(self, node, visited):
        if not node :
            return 
        
        self._postorder_travers(node.left, visited)
        self._postorder_travers(node.right, visited)
        visited.append(node.val)


# reconstruct using (inorder and preorder)
def inorder_preorder_reconstruct(inorder, preorder):
    if not inorder and not preorder:
        return None
    
    root_data = preorder[0]
    root = Node(root_data)
    idx = inorder.index(root_data)
    # print(idx)

    # [3, 5, 7, 10, 12, 15, 18]
    # [10, 5, 3, 7, 15, 12, 18]
    # l = [3, 5, 7], r = [15, 12, 18]
    # pl = [5, 3, 7], pr = [15, 12, 18]
    root.left = inorder_preorder_reconstruct(inorder[:idx], preorder[1:idx+1])
    root.right = inorder_preorder_reconstruct(inorder[idx+1:], preorder[idx+1:])
    return root

# reconstruct using (inorder and postorder)
def inorder_postorder_reconstruct(inorder, postorder):
    if not inorder and not postorder:
        return None

    root_data = postorder[-1]
    root = Node(root_data)
    idx = inorder.index(root_data)
    # print(idx)

    # [3, 5, 7, 10, 12, 15, 18]
    # [3, 7, 5, 12, 18, 15, 10]
    # l = [3, 5, 7], r = [15, 12, 18]
    # pl = [3, 7, 5], pr = [12, 18, 15]
    root.left = inorder_postorder_reconstruct(inorder[:idx], postorder[:idx])
    root.right = inorder_postorder_reconstruct(inorder[idx+1:], postorder[idx:-1])
    return root
    

if __name__ == "__main__":
    bt = BinaryTree()
    bt.insert(10)
    bt.insert(5)
    bt.insert(15)
    bt.insert(3)
    bt.insert(7)
    bt.insert(12)
    bt.insert(18)

    inorder_list = bt.inorder_trverse()
    preorder_list = bt.preorder_trverse()
    postorder_list = bt.postorder_trverse()

    print(inorder_list)
    print(preorder_list)
    print(postorder_list)

    print("\nreconstructed trees:")
    in_pre = inorder_preorder_reconstruct(inorder_list, preorder_list)
    bt_in_pre = BinaryTree()
    bt_in_pre.root = in_pre
    print("inorder + preorder = ", bt_in_pre.inorder_trverse())
    # bt_in_pre.draw(bt_in_pre.root)

    in_post = inorder_postorder_reconstruct(inorder_list, postorder_list)
    bt_in_post = BinaryTree()
    bt_in_post.root = in_post
    print("inorder + postorder = ", bt_in_post.inorder_trverse())
    # bt_in_post.draw(bt_in_post.root)

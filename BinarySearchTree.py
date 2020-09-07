'''
name : ByeongJun Ahn
nation : KOREA
contact : 010-2736-5474 or ahnbj0@naver.com
source : https://geonlee.tistory.com/72 [빠리의 택시 운전사]
comment : 이진탐색트리에서 삽입, 검색, 삭제, 전위순회, 중위순회, 후위순회 기능을 구현하였다.
위 출처에 있는 코드를 필사하면서 암기하였는데, 중간중간 세심하고 효율적인 코드에 대해 배울 점이 있었다.
'''

class Node(object):
    def __init__(self, data):
        self.data= data
        self.left = None
        self.right = None

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node

    def find(self, key):
        return self._find_value(self.root, key)

    def _find_value(self, root, key):
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            return self._find_value(root.left, key)
        else:
            return self._find_value(root.right, key)

    def delete(self, key):
        self.root, deleted = self._delete_value(self.root, key)
        return deleted

    def _delete_value(self, node, key):
        if node is None:
            return node, False

        deleted = False
        if node.data == key:
            deleted = True
            if node.left and node.right:
                parent, child = node, node.right
                while child.left:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        else:
            if key < node.data:
                node.left, deleted = self._delete_value(node.left, key)
            else:
                node.right, deleted = self._delete_value(node.right, key)
        return node, deleted

    def preorder_traversal(self):
        def _preorder_(root):
            if root is None:
                pass
            else:
                print(root.data, end = " ")
                _preorder_(root.left)
                _preorder_(root.right)
        _preorder_(self.root)
        print()

    def inorder_traversal(self):
        def _inorder_(root):
            if root is None:
                pass
            else:
                _inorder_(root.left)
                print(root.data, end = " ")
                _inorder_(root.right)
        _inorder_(self.root)
        print()

    def postorder_traversal(self):
        def _postorder_(root):
            if root is None:
                pass
            else:
                _postorder_(root.left)
                _postorder_(root.right)
                print(root.data, end = " ")
        _postorder_(self.root)
        print()

# Example
array = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]
bst = BinarySearchTree()
for x in array:
    bst.insert(x)

# Find
print(bst.find(15)) # True
print(bst.find(17)) # False

# Delete
print(bst.delete(55)) # True
print(bst.delete(14)) # True
print(bst.delete(11)) # False

# traversal
bst.preorder_traversal()
bst.inorder_traversal()
bst.postorder_traversal()

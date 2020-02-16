from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)

    def to_array(self):
        result = []
        queue = deque([self])

        while True:
            size = len(queue)
            hasValue = False

            for i in range(size):
                cur = queue.popleft()
                if (cur is None):
                    result += [None]
                else:
                    result += [cur.val]
                    if not hasValue and (cur.left is not None or cur.right is not None):
                        hasValue = True
                    queue.append(cur.left)
                    queue.append(cur.right)
            if hasValue == False:
                return result

    @staticmethod
    def insertLevelOrder(arr):
        return TreeNode._insertLevelOrder(arr, None, 0, len(arr))

    @staticmethod
    def _insertLevelOrder(arr, root, index, n):
        if index < n and arr[index] is not None:
            temp = TreeNode(arr[index])
            root = temp
            root.left = TreeNode._insertLevelOrder(arr, root.left, 2 * index + 1, n)
            root.right = TreeNode._insertLevelOrder(arr, root.right, 2 * index + 2, n)
        return root

    @staticmethod
    def maxDepth(root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0;

        lookup, depth = deque([root]), 0

        while len(lookup) > 0:
            size = len(lookup)
            depth += 1
            for i in range(size):
                node = lookup.popleft()
                if node.left is not None:
                    lookup.append(node.left)
                if node.right is not None:
                    lookup.append(node.right)

        return depth

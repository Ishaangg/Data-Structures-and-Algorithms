
class Solution:
    
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.sums = 0
        self.traverse(root, 'c')
        return self.sums

    def traverse(self, root, dir):
        if not root:
            return

        if root.left == None and root.right == None and dir == 'l':
            self.sums += root.val  

        self.traverse(root.left, 'l')

#         self.right = right
#         self.left = left
[

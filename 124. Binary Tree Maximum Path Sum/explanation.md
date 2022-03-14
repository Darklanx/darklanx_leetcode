[124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum)
===
If the optimal path includes a node N, then this path can be
1. N is the root of this optimal path (nodes above this node is not included in the path) => max(node.left, 0) + node.val + max(node.right, 0), where node.left is the maximum sum of the left node can find. 
2. node.val + max(node.left, 0)
3. node.val + max(node.right, 0)


### Time complexity: $\mathcal{O}(N)$
where N is number of nodes, since we visit each node not more than 2 times.

### Space complexity: $\mathcal{O}(H)$
where $H$ is a tree height, to keep the recursion stack. In the average case of balanced tree, the tree height $H = \log N$, in the worst case of skewed tree, $H=N$
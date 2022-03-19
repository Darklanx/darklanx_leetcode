[19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list)
===
1. Maintain `head, prev, cur, next`
2. Let `next` forward `n`, then we forward `next` and `cur` at the same time. Whenever `next is None`, `cur` will be the node that we want to remove.

Note that if `prev is None` we are removing the head so we have to return `head.next`.
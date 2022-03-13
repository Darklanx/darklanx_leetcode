# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def append_node(end_of_node, new_node):
            end_of_node.next = new_node
            end_of_node = end_of_node.next
            end_of_node.next = None
            return end_of_node
            
        return_list_head = ListNode()
        return_list_ptr = return_list_head
        max_seen = -1e10
        holding_node = None
        # we only append the return_list when the larger number or the last node is seen (and there's no dup)
        while head is not None:      
            if head.val == max_seen: # dup!
                holding_node = None
            elif head.val > max_seen:
                if holding_node is not None:
                    return_list_ptr = append_node(return_list_ptr, holding_node)

                
                holding_node = head
                max_seen = head.val

            head = head.next
            if head is None:
                if holding_node is not None:
                    return_list_ptr = append_node(return_list_ptr, holding_node)

    
        return return_list_head.next
    

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

int getSize(ListNode* head){
    int size = 0;
    while (head != nullptr){
        size++;
        head = head->next;
    }
    return size;
}

ListNode* reverse(ListNode* head, int k){
    /*
        return new head
    */
    ListNode* operating_node = head;
    ListNode* prev_node = head;
    ListNode* tmp_next = operating_node->next;
    while(k--){
        tmp_next = operating_node->next;  
        operating_node->next = prev_node; // reverse current_node  
        prev_node = operating_node; 
        operating_node = tmp_next; 
    }
    // handle head here
    head->next = tmp_next;
    return prev_node;
    
}

ListNode* forwardNode(ListNode* current_node, int steps){
    for(int i=0; i<steps; i++){
        if (current_node->next == nullptr){
            return nullptr;
        }
        current_node = current_node->next;
    }
    return current_node;
}

class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        int size = getSize(head);
        if (size < k || head == nullptr)
            return head;
        ListNode* new_head = reverse(head, k);
        ListNode* next_head = forwardNode(new_head, k); 
        forwardNode(new_head, k-1)->next = reverseKGroup(next_head, k);
        return new_head;
    }
};
/*
 * @lc app=leetcode id=23 lang=cpp
 *
 * [23] Merge k Sorted Lists
 */

// @lc code=start
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

struct cmp{
    bool operator()(ListNode* lhs, ListNode *rhs){
        return lhs->val > rhs->val;

    }
};
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        priority_queue<ListNode*, vector<ListNode*>, cmp> pq;
        for (ListNode* &list : lists) {
            ListNode* current = list;
            while(current != nullptr){
                pq.push(current);
                current = current->next;
            }
        }
        
        ListNode* head = new ListNode(-100);
        ListNode* current = head;
        cout << pq.size() << endl;
        while(!pq.empty()){
            current->next = pq.top();
            pq.pop();
            cout << current->next->val <<endl;
            cout << "h: " << head->next->val << endl;
            current = current->next;
        }
        current->next = nullptr;
        // cout << "h next: " << head->next->val << endl;
        // // while(head!=nullptr){
        // //     cout << head->val;
        // //     head = head->next;
        // // }
        return head->next;
    }
};

// class Solution {
// public:
//     ListNode* mergeKLists(vector<ListNode*>& lists) {
//         ListNode *current, *head;

//         current = new ListNode();
//         head = current;
        
//         while(true){
//             int min = INT_MAX;
//             int min_idx = -1;
//             // search for min val
//             for(int i=0; i<lists.size(); i++){
//                 if (lists[i] == nullptr)
//                     continue;
//                 if(lists[i]->val < min){
//                     min = lists[i]->val;
//                     min_idx = i;   
//                 }
//             }
//             if(min_idx == -1)
//                 break;
//             // min_idx has the min value 
//             current->next = lists[min_idx];
//             current = current->next;
//             lists[min_idx] = lists[min_idx]->next;
            
//         }
        
//         return head->next;
//     }
// };
// @lc code=end


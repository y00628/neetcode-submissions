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

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int length = 0;
        ListNode* prev = nullptr;
        ListNode* curr = head;

        while (curr) {
            length++;
            curr = curr->next;
        }

        curr = head;

        for (int i = 0; i < length-n; i++) {
            prev = curr;
            curr = curr->next;
        }

        if (prev && curr) {
            prev->next = curr->next;
        } else if (curr) {
            head = curr->next;
        }

        curr->next = nullptr;
        curr = nullptr;

        return head;
    }
};

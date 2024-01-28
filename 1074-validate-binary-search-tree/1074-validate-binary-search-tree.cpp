/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool isValidBST(TreeNode *root) {
	if (root==NULL) return true;
	if (root->left == NULL && root->right==NULL) return true;
	if (root->left!=NULL) {if (root->left->val >= root->val) return false;}
	if (root->right!=NULL) {if (root->right->val <= root->val) return false;}
	return (isValidBST(root->left) && isValidBST(root->right));     
}

};
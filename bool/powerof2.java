class Solution {
    public boolean isPowerOfTwo(int n) {
        return n>0&&(n&(n-1))==0;
    }
}
// Logical Evaluation of the Return Statement
// The expression:
// n > 0 && (n & (n - 1)) == 0
// is evaluated as:
// Check if n > 0 → returns boolean
// Compute (n & (n - 1))
// Compare result with 0 → returns boolean
// Apply logical AND (&&) between both boolean results
// So final structure becomes:
// boolean && boolean

class Solution {
    public long countCommas(long n) {
        long result = 0;
        long base = 1000;          // First threshold: 1,000

        while (base <= n) {
            result += n - base + 1; // How many numbers are in [base, n]?
            base *= 1000;           // Move to next threshold: 1,000,000 → 1,000,000,000 → ...
        }
    return result;
    }
}

[![Leetcode Stats](https://leetcard.jacoblin.cool/RajaYokenSSR?theme=dark&font=Sarpanch&ext=heatmap)](https://leetcode.com/hareeshprogrammer)

# LeetCode Journey & DSA Learnings 🚀

Welcome to my LeetCode repository! This repository serves as a personal log of my problem-solving journey, where I practice Data Structures and Algorithms (DSA), optimize solutions, and document key learnings.

---

## 💡 Key Algorithmic Patterns Learnt

Here are some of the most critical algorithmic patterns and data structures I've explored and mastered in this repository:

<details>
<summary>📂 <b>1. Monotonic Stack & Queue</b></summary>

* **Core Concept**: A stack that maintains elements in a specific order (either strictly increasing or decreasing). It is highly optimized for finding the *next greater element* or *previous smaller element* in a single pass ($O(N)$ time).
* **Key Solutions**:
  * [Largest Rectangle in Histogram](./List/hard/Largest%20Rectangle%20in%20Histogram.py) — Used a monotonic increasing stack to efficiently track boundary limits of bars.
  * [Daily Temperatures](./List/medium/739.%20Daily%20Temperatures.py) — Found the number of days until a warmer temperature using index tracking.
  * [Final Prices With a Special Discount](./List/easy/1475.%20Final%20Prices%20With%20a%20Special%20Discount%20in%20a%20Shop.py) — Computed discounted prices based on the next smaller element.
</details>

<details>
<summary>📂 <b>2. Disjoint Set Union (DSU / Union-Find)</b></summary>

* **Core Concept**: A tree-like data structure that tracks partition groupings. Uses *Path Compression* and *Union by Rank/Size* to perform element groupings and connectivity checks in near-constant time ($O(\alpha(N))$).
* **Key Solutions**:
  * [Check if There is a Valid Path in a Grid](./List/medium/1391.%20Check%20if%20There%20is%20a%20Valid%20Path%20in%20a%20Grid.py) — Grouped adjacent cells if they have matching corridor layouts to check start-to-end connectivity.
</details>

<details>
<summary>📂 <b>3. Priority Queue / Heaps</b></summary>

* **Core Concept**: A tree structure that allows rapid lookup and extraction of the minimum or maximum element ($O(1)$ lookup, $O(\log N)$ extraction/insertion).
* **Key Solutions**:
  * [Construct Target Array With Multiple Sums](./List/hard/Construct%20Target%20Array%20With%20Multiple%20Sums.py) — Used a Max-Heap combined with modulo division optimization to reverse-engineer target array construction.
  * [Find K Pairs with Smallest Sums](./List/medium/Find%20K%20Pairs%20With%20Smallest%20Sums.py) — Extracted combinations efficiently without evaluating all pairs.
  * [Last Stone Weight](./List/easy/Last%20Stone%20Weight.py) — Simulated stone smashing using a Max-Heap.
</details>

<details>
<summary>📂 <b>4. Two Pointers & Sliding Window</b></summary>

* **Core Concept**: Using multiple indices to traverse arrays/strings from different directions or at different speeds, reducing $O(N^2)$ brute-force solutions to $O(N)$.
* **Key Solutions**:
  * [3Sum](./List/medium/15.%203Sum.py) — Sorted the array and applied two pointers to avoid nested loops and duplicates.
  * [Valid Palindrome](./String/easy/125.%20Valid%20Palindrome.py) — Compared characters from outer boundaries inward.
  * [Move Zeroes](./List/easy/283.%20Move%20Zeroes.py) & [Remove Duplicates](./List/easy/26.%20Remove%20Duplicates%20from%20Sorted%20Array.py) — Tracked write vs. read positions to modify arrays in-place.
</details>

<details>
<summary>📂 <b>5. Mathematical Proofs & Greedy Tricks</b></summary>

* **Core Concept**: Leveraging mathematical rules or locally optimal choices to achieve a globally optimal result with minimal memory or steps.
* **Key Solutions**:
  * [Find Unique Binary String](./String/medium/1980.%20Find%20Unique%20Binary%20String.py) — Applied **Cantor's Diagonal Argument** to construct a unique binary string in $O(N)$ time and $O(1)$ extra space.
  * [Partitioning Into Minimum Number Of Deci-Binary Numbers](./String/medium/1689.%20Partitioning%20Into%20Minimum%20Number%20Of%20Deci-Binary%20Numbers.py) — Realized the minimum partitions equals the maximum digit in the input string.
  * [Minimum Swaps to Arrange a Binary Grid](./List/medium/1536.%20Minimum%20Swaps%20to%20Arrange%20a%20Binary%20Grid.py) — Computed required trailing zeroes and greedily swapped rows.
</details>

---

## 📊 Solved Problems Index

Here is the index of all solutions currently stored in this repository:

### 🏆 Hard Problems
| # | Problem Name | Code Solution | Key Concept / Pattern |
|---|---|---|---|
| 84 | [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) | [Python](./List/hard/Largest%20Rectangle%20in%20Histogram.py) | Monotonic Stack |
| 1354 | [Construct Target Array With Multiple Sums](https://leetcode.com/problems/construct-target-array-with-multiple-sums/) | [Python](./List/hard/Construct%20Target%20Array%20With%20Multiple%20Sums.py) | Max-Heap, Modulo Optimization |

### ⚡ Medium Problems
| # | Problem Name | Code Solution | Key Concept / Pattern |
|---|---|---|---|
| 6 | [ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion/) | [Python](./String/medium/zig%20zag%20conversion%20lc-6.py) | String Simulation |
| 15 | [3Sum](https://leetcode.com/problems/3sum/) | [Python](./List/medium/15.%203Sum.py) | Two Pointers, Sorting |
| 53 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | [Python](./List/medium/53.%20Maximum%20Subarray.py) | Kadane's Algorithm, Dynamic Programming |
| 373 | [Find K Pairs with Smallest Sums](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/) | [Python](./List/medium/Find%20K%20Pairs%20With%20Smallest%20Sums.py) | Min-Heap / Priority Queue |
| 459 | [Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/) | [Python](./String/medium/Repeated%20Substring%20Pattern.py) | String Manipulation |
| 686 | [Repeated String Matching](https://leetcode.com/problems/repeated-string-matching/) | [Python](./String/medium/Repeated%20String%20Matching.py) | String Search, Rabin-Karp |
| 739 | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | [Python](./List/medium/739.%20Daily%20Temperatures.py) | Monotonic Stack |
| 843 | [Masking Personal Information](https://leetcode.com/problems/masking-personal-information/) | [Python](./String/medium/Masking%20Personal%20Information.py) | String Formatting |
| 1391 | [Check if There is a Valid Path in a Grid](https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/) | [Python](./List/medium/1391.%20Check%20if%20There%20is%20a%20Valid%20Path%20in%20a%20Grid.py) | Disjoint Set Union (DSU) |
| 1536 | [Minimum Swaps to Arrange a Binary Grid](https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/) | [Python](./List/medium/1536.%20Minimum%20Swaps%20to%20Arrange%20a%20Binary%20Grid.py) | Greedy row swap logic |
| 1689 | [Partitioning Into Minimum Deci-Binary Numbers](https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/) | [Python](./String/medium/1689.%20Partitioning%20Into%20Minimum%20Number%20Of%20Deci-Binary%20Numbers.py) | Max Digit Extraction |
| 1861 | [Rotating the Box](https://leetcode.com/problems/rotating-the-box/) | [Python](./List/medium/1861.%20Rotating%20the%20Box.py) | Two Pointers, Grid Transformation |
| 1980 | [Find Unique Binary String](https://leetcode.com/problems/find-unique-binary-string/) | [Python](./String/medium/1980.%20Find%20Unique%20Binary%20String.py) | Cantor's Diagonal Argument |

### 🌱 Easy Problems
| # | Problem Name | Code Solution | Key Concept / Pattern |
|---|---|---|---|
| 26 | [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | [Python](./List/easy/26.%20Remove%20Duplicates%20from%20Sorted%20Array.py) | Two Pointers |
| 121 | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | [Python](./List/easy/121.%20Best%20Time%20to%20Buy%20and%20Sell%20Stock.py) | Sliding Window, Prefix Min |
| 125 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | [Python](./String/easy/125.%20Valid%20Palindrome.py) | Two Pointers |
| 203 | [Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/) | [Python](./List/easy/203.%20Remove%20Linked%20List%20Elements.py) | Linked List Traversal |
| 217 | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | [Python](./List/easy/217-%20Contains%20Duplicate.py) | HashSet lookup |
| 242 | [Valid Anagram](https://leetcode.com/problems/valid-anagram/) | [Python](./String/easy/242.%20Valid%20Anagram.py) | Frequency Counter / Hash Map |
| 283 | [Move Zeroes](https://leetcode.com/problems/move-zeroes/) | [Python](./List/easy/283.%20Move%20Zeroes.py) | Two Pointers |
| 344 | [Reverse String](https://leetcode.com/problems/reverse-string/) | [Python](./String/easy/344.%20Reverse%20String.py) | Two Pointers |
| 482 | [License Key Formatting](https://leetcode.com/problems/license-key-formatting/) | [Python](./String/easy/License%20Key%20Formatting.py) | String Processing |
| 520 | [Detect Capital](https://leetcode.com/problems/detect-capital/) | [Python](./String/easy/Detect%20Capitals.py) | String Matching |
| 796 | [Rotate String](https://leetcode.com/problems/rotate-string/) | [Python](./String/easy/Rotate%20String.py) | Substring search `(s + s)` |
| 1022 | [Sum of Root To Leaf Binary Numbers](https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/) | [Python](./List/easy/1022.%20Sum%20of%20Root%20To%20Leaf%20Binary%20Numbers.py) | Binary Tree, DFS Traversal |
| 1046 | [Last Stone Weight](https://leetcode.com/problems/last-stone-weight/) | [Python](./List/easy/Last%20Stone%20Weight.py) | Max-Heap simulation |
| 1475 | [Final Prices Special Discount](https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/) | [Python](./List/easy/1475.%20Final%20Prices%20With%20a%20Special%20Discount%20in%20a%20Shop.py) | Monotonic Stack / Array |
| 1700 | [Number of Students Unable to Eat Lunch](https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/) | [Python](./List/easy/Number%20of%20Students%20Unable%20to%20Eat%20Lunch.py) | Queue & Stack simulation |
| 1848 | [Minimum Distance to Target](https://leetcode.com/problems/minimum-distance-to-the-target-element/) | [Python](./List/easy/1848.%20Minimum%20Distance%20to%20the%20Target%20Element.py) | Array iteration |
| 2073 | [Time Needed to Buy Tickets](https://leetcode.com/problems/time-needed-to-buy-tickets/) | [Python](./List/easy/Time%20Needed%20to%20Buy%20Tickets.py) | Simulation / Math |

---

## 🛠️ Tech Stack & Utilities

- **Language**: Python 3.x
- **Topics**: Dynamic Programming, Graphs, Data Structure Design (Stacks/Queues/Heaps), Greedy algorithms.
- **Aesthetic Stats Card**: [Jacob Lin's Leetcard API](https://github.com/luckyjoseph/leetcard)

Happy Coding! 💻

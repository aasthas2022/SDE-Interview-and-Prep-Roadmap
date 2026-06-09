# Sliding Window

A technique for problems involving **contiguous subarrays or substrings**, where we maintain a "window" `[l, r]` over the data and slide it instead of recomputing from scratch. It turns many naive `O(n²)`/`O(n·k)` brute forces into `O(n)`.

## When to reach for it

Look for these signals in a problem statement:

- "contiguous subarray" / "substring"
- "longest / shortest / max / min" subarray satisfying some condition
- A constraint that grows or shrinks **monotonically** as the window changes (e.g. sum, count of distinct chars, frequency)
- Fixed window length `k`, or a target you grow/shrink toward

If the validity of a window is **monotonic** (extending an invalid window keeps it invalid, or a valid window stays valid when shrunk), sliding window applies. If not, you usually need prefix sums + hashing, or another approach.

---

## Two core patterns

### 1. Fixed-size window

Window length is fixed at `k`. Slide one step at a time: add the entering element, remove the leaving element.

```cpp
// Max sum of any subarray of length k
long long maxSumK(const vector<int>& a, int k) {
    long long sum = 0, best = LLONG_MIN;
    for (int r = 0; r < (int)a.size(); r++) {
        sum += a[r];
        if (r >= k - 1) {
            best = max(best, sum);
            sum -= a[r - k + 1];   // element leaving the window
        }
    }
    return best;
}
```

**Template shape**

```
for r in [0, n):
    add a[r] to window state
    if window size == k:
        record / use answer
        remove a[r - k + 1] from window state
```

### 2. Variable-size window (expand / shrink)

The window grows by advancing `r`, and shrinks by advancing `l` whenever the window becomes invalid (or to optimize). Each index enters and leaves at most once → `O(n)` total even with the nested `while`.

```cpp
// Longest substring without repeating characters (LeetCode 3)
int lengthOfLongestSubstring(const string& s) {
    vector<int> last(256, -1);   // last index of each char
    int l = 0, best = 0;
    for (int r = 0; r < (int)s.size(); r++) {
        if (last[s[r]] >= l)     // char repeats inside window
            l = last[s[r]] + 1;  // jump l past the duplicate
        last[s[r]] = r;
        best = max(best, r - l + 1);
    }
    return best;
}
```

**Template shape**

```
l = 0
for r in [0, n):
    add a[r] to window state
    while window is invalid:
        remove a[l] from window state
        l++
    update answer with [l, r]
```

The only design decisions are: *what state describes the window*, and *what "invalid" means*.

---

## Choosing between "longest" and "shortest"

The shrink condition flips depending on the goal:

| Goal | Loop invariant | When to shrink |
|------|----------------|----------------|
| **Longest** valid window | keep window valid | shrink **while invalid**, then record |
| **Shortest** valid window | window may be valid | shrink **while valid**, recording each step |

```cpp
// Shortest subarray with sum >= target (positive numbers) — LeetCode 209
int minSubArrayLen(int target, const vector<int>& a) {
    int l = 0, best = INT_MAX;
    long long sum = 0;
    for (int r = 0; r < (int)a.size(); r++) {
        sum += a[r];
        while (sum >= target) {            // shrink while STILL valid
            best = min(best, r - l + 1);
            sum -= a[l++];
        }
    }
    return best == INT_MAX ? 0 : best;
}
```

---

## Common window states

The "state" is whatever lets you check validity in `O(1)` amortized:

- **Running sum** → sum/average constraints
- **Frequency map** (`array[26/128/256]` or `unordered_map`) → distinct counts, anagrams, char limits
- **Count of "bad" elements** → "at most k zeros / replacements" problems
- **Monotonic deque** → window max/min in `O(1)`
- **`distinct` counter** alongside the freq map → number of unique elements in window

```cpp
// Longest substring with at most k distinct characters
int atMostKDistinct(const string& s, int k) {
    unordered_map<char,int> cnt;
    int l = 0, best = 0;
    for (int r = 0; r < (int)s.size(); r++) {
        cnt[s[r]]++;
        while ((int)cnt.size() > k) {
            if (--cnt[s[l]] == 0) cnt.erase(s[l]);
            l++;
        }
        best = max(best, r - l + 1);
    }
    return best;
}
```

---

## The "exactly k" trick

Counting subarrays with a property **exactly k** is awkward directly, but easy via:

```
exactly(k) = atMost(k) - atMost(k - 1)
```

This reduces "exactly" problems (e.g. *Subarrays with K Different Integers*, LeetCode 992) to two standard at-most sliding windows.

```cpp
int subarraysWithKDistinct(vector<int>& a, int k) {
    return atMost(a, k) - atMost(a, k - 1);
}
// atMost counts subarrays with <= k distinct; for each r add (r - l + 1)
```

> Counting subarrays: when the window `[l, r]` is valid, **every** subarray ending at `r` with start in `[l, r]` is valid, so add `r - l + 1` to the count.

---

## Monotonic deque: window maximum

For sliding window max/min, a deque holds **indices** in decreasing value order. Front is always the window max.

```cpp
// Sliding window maximum (LeetCode 239)
vector<int> maxSlidingWindow(const vector<int>& a, int k) {
    deque<int> dq;            // stores indices, values decreasing
    vector<int> res;
    for (int r = 0; r < (int)a.size(); r++) {
        while (!dq.empty() && a[dq.back()] <= a[r]) dq.pop_back();
        dq.push_back(r);
        if (dq.front() <= r - k) dq.pop_front();   // drop out-of-window
        if (r >= k - 1) res.push_back(a[dq.front()]);
    }
    return res;
}
```

---

## Pitfalls

- **Negative numbers break the sum window.** `minSubArrayLen` assumes positives so that `sum` is monotonic. With negatives, use prefix sums + monotonic deque (LeetCode 862) instead.
- **Off-by-one on window size:** size is `r - l + 1`, not `r - l`.
- **Forgetting to erase zero-count keys** when using `unordered_map` for distinct counts — `map.size()` will be wrong otherwise.
- **Recording the answer at the wrong moment** — for "longest", record after shrinking back to valid; for "shortest", record inside the shrink loop while still valid.
- **Resetting `l` backwards.** `l` only ever moves forward; that monotonic movement is what guarantees `O(n)`.

---

## Practice set

| # | Problem | Pattern |
|---|---------|---------|
| LC 3 | Longest Substring Without Repeating Characters | variable, freq |
| LC 76 | Minimum Window Substring | variable, freq + need-counter |
| LC 209 | Minimum Size Subarray Sum | variable, shortest |
| LC 239 | Sliding Window Maximum | monotonic deque |
| LC 424 | Longest Repeating Character Replacement | variable, max-freq |
| LC 567 | Permutation in String | fixed, freq compare |
| LC 862 | Shortest Subarray with Sum ≥ K | prefix + deque |
| LC 992 | Subarrays with K Different Integers | atMost(k) − atMost(k−1) |
| LC 1004 | Max Consecutive Ones III | variable, bad-counter |
| LC 1456 | Max Vowels in Substring of Length K | fixed |

---

## Complexity

- Time: **O(n)** — each index is added once and removed at most once.
- Space: **O(1)** for sum windows, **O(k)** or **O(alphabet)** for frequency/deque windows.
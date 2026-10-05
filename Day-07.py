The important condition is that the array is sorted.

Example:

nums = [1, 2, 3, 4, 5]

We put:

left → 1
right → 5

Suppose our target is 6.

We check:

1 + 5 = 6 ✅

Done immediately.

But suppose target is 7:

1 + 5 = 6

The sum is too small, so we know we need a larger number.

Therefore, we move left forward:

    left → 2
             right → 5

2 + 5 = 7 ✅

That's the intelligence behind Two Pointers: the sorted order tells us which pointer to move.
1️⃣ What is Two Pointers?

The simplest idea:

We use two variables (pointers) to keep track of two positions in an array/string and move them intelligently.

For example:

nums = [1, 2, 3, 4, 5]

        ↑           ↑
       left        right

Here:

left  = 0
right = 4

So left points to 1 and right points to 5.

Instead of checking every possible pair like we did in brute-force Two Sum, we use these two positions and decide which pointer should move.

That's the basic idea.

Don't worry about when/how to move them yet. We'll understand that next.



next?

Now let's understand the three possible situations when we calculate:

nums[left] + nums[right]
1. Sum = target ✅

We found the answer:

1 + 5 = 6

Return the two indices.

2. Sum < target

The sum is too small, so we need a bigger value.

1 + 5 = 6
target = 7

→ move left forward
3. Sum > target

The sum is too large, so we need a smaller value.

2 + 5 = 7
target = 6

→ move right backward

So remember:

sum < target → left++
sum > target → right--
sum = target → answer

That's the core rule of Two Pointers. 🔥


Now let's learn when you should recognize Two Pointers in an interview.

Usually, look for these clues:

🔎 Clue 1 — Array/String is sorted
[1, 2, 3, 4, 5]

Sorted order lets us decide which pointer to move.

🔎 Clue 2 — Problem asks about a pair

For example:

"Find two numbers whose sum equals target."

🔎 Clue 3 — You are comparing from both ends

Something like:

left →          ← right
Simple interview rule 🧠

Sorted array + pair/search/comparison → immediately consider Two Pointers.

Next we'll start LeetCode 167 — Two Sum II, where you'll apply exactly what you just learned.

ok 
LeetCode 167 — Two Sum II

The problem gives us a sorted array and a target. We need to find two numbers whose sum equals the target and return their 1-based indices.

Example:

numbers = [2, 7, 11, 15]
target = 9

We need:

2 + 7 = 9

So the answer is:

[1, 2]

⚠️ Notice: LeetCode 167 uses 1-based indices, unlike Two Sum (LeetCode 1), which uses 0-based indices.

Before we code, you tell me how you would place the two pointers on this sorted array.

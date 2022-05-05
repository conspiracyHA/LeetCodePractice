"""
You are given a string s consisting only of characters 'a' and 'b'​​​​.

You can delete any number of characters in s to make s balanced.
s is balanced if there is no pair of indices (i,j)
such that i < j and s[i] = 'b' and s[j]= 'a'.

Return the minimum number of deletions needed to make s balanced.



Example 1:

Input: s = "aababbab"
Output: 2
Explanation: You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").

Example 2:

Input: s = "bbaaaaabb"
Output: 2
Explanation: The only solution is to delete the first two characters.



Constraints:

    1 <= s.length <= 105
    s[i] is 'a' or 'b'​​.


"""


class Solution:
    def minimumDeletions(self, s: str) -> int:
        if 'b' not in s or 'a' not in s:
            return 0
        total_count = 0
        a_count_list = list()
        for c in s:
            if c == 'a':
                total_count += 1
            a_count_list.append(total_count)

        answer = total_count
        previous_a_count = a_count_list[0]
        for idx, a_count in enumerate(a_count_list[1:], start=1):
            if answer > total_count - a_count + idx - previous_a_count:
                answer = total_count - a_count + idx - previous_a_count
            previous_a_count = a_count
        return answer


class Solution:
    def minimumDeletions(self, s: str) -> int:
        b_count = 0
        result = 0
        for c in s:
            if c == 'b':
                b_count += 1
            else:
                result = min(result + 1, b_count)
        return result





if __name__ == '__main__':
    test = [
        'aababbab',
        'bbaaaaabb',
        "bbbbbbbaabbbbbaaabbbabbbbaabbbbbbaabbaaabaabbbaaaabaaababbbabbabbaaaabbbabbbbbaabbababbbaaaaaababaaababaabbabbbaaaabbbbbabbabaaaabbbaba"
    ]
    answer = [
        2,
        2,
        60
    ]
    for t, a in zip(test, answer):
        if Solution().minimumDeletions(t) == a:
            print('pass')
        else:
            print('wrong answer')




'''
340. 至多包含K个不同字符的最长子串
给一个字符串 s 和整数 k ， 要求返回最多由k个不同字符组成的最长子串

示例 1:

输入: s = "eceba", k = 2
输出: 3
解释: 子字符串 "ece" 长度为 3.
示例 2:

输入: s = "aa", k = 1
输出: 2
解释: 子字符串 "aa" 长度为 2.
'''
class Solution:
	def lengthOfLongestSubstringKDistinct(s, k):
        pass


if __name__ =='__main__':
    #参考leetcode 159
    s1 = Solution()
    s = "eceba"
    k = 2
    print('1',s1.lengthOfLongestSubstringKDistinct(s,k))
    s = "aa"
    k = 1
    print('1',s1.lengthOfLongestSubstringKDistinct(s,k))
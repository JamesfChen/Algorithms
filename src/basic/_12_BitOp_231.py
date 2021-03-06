'''
231. 2的幂
给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

示例 1:
输入: 1
输出: true
解释: 2^0 = 1
示例 2:
输入: 16
输出: true
解释: 2^4 = 16
示例 3:
输入: 218
输出: false
'''
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #由于2的幂次数的二进制数，只会有一个1
        return n>0 and not (n & n-1)
if __name__=='__main__':
    s = Solution()
    n=1
    print('1', s.isPowerOfTwo(n))
    n=16
    print('1', s.isPowerOfTwo(n))
    n=218
    print('1', s.isPowerOfTwo(n))

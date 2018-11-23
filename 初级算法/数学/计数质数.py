class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        prime_list = [True] * n
        prime_list[0], prime_list[1] = False, False
        num = 2
        while num ** 2 < n:
            if prime_list[num] == True:
                # 小于num ** 2的不用排除了
                # 因为已经被小于num的倍数排除掉了
                time = num ** 2
                while time < n:
                    prime_list[time] = False
                    time += num
            # 筛选结束
            num += 1
        return sum(prime_list)

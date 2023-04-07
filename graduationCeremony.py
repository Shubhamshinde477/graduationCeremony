
from itertools import permutations


class GraduationCeremony:

    def __init__(self, n):
        if n < 4:
            raise Exception(f"Input days {n} are less than 4")
        self.n = n

    def brute_force(self):

        ways_to_attend = 0
        ways_to_miss = 0

        for i in range(0, self.n+1):
            A = "A"*i + 'P'*(self.n-i)
            B = set(map(lambda b: ''.join(b), set(permutations(A))))
            days_to_ignore = 4*'A'

            for k in B:
                if k.find(days_to_ignore) == -1:
                    ways_to_attend += 1
                    if k.endswith('A'):
                        ways_to_miss += 1
        return f'{ways_to_miss}/{ways_to_attend}'

    def optimised_solution(self):
        """
        This
        :return:
        """
        dp = [[0] * 4 for _ in range(self.n + 1)]

        dp[0][0] = 1
        for i in range(1, self.n + 1):
            # attended on day i
            dp[i][0] = sum(dp[i - 1][:4])
            for j in range(1, 4):
                dp[i][j] = dp[i - 1][j - 1]

        return f"{sum(dp[self.n][1:])}/{sum(dp[self.n])}"

if __name__=="__main__":
    gc = GraduationCeremony(5)
    print(gc.brute_force())
    print(gc.optimised_solution())

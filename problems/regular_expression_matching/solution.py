class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        p_len = len(p)
        s_len = len(s)

        res = [ [False]*(p_len+3) for i in range(s_len+3) ]

        res[s_len][p_len] = True

        for i in range(s_len, -1, -1):
            for j in range(p_len - 1, -1, -1):

                if (j+1) < p_len and p[j+1] == '*':
                    res[i][j] = res[i][j+2]

                    if i < s_len and (p[j] == '.' or s[i] == p[j]):
                        res[i][j] = res[i][j] or res[i+1][j]
                elif i < s_len and (p[j] == '.' or s[i] == p[j]):
                    res[i][j] = res[i+1][j+1]

        return res[0][0]

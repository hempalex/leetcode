class Solution:
    def compress(self, chars: List[str]) -> int:
            
        cur = 0
        cnt = 1
        prev = chars[0]

        def putChCnt():
            nonlocal cur, prev, cnt
            chars[cur] = prev
            cur += 1
            if cnt > 1:
                for ch in str(cnt):
                    chars[cur] = ch
                    cur += 1


        for i in range(1, len(chars)):
            if chars[i] != prev:
                putChCnt()
                cnt = 1
                prev = chars[i]
            else:
                cnt += 1
        
        if cnt > 0:
            putChCnt()

        return cur
            

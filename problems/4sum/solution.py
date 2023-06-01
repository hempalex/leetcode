class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        count = {}
        uniq = []

        for i, n in enumerate(nums):
            count[n] = count.get(n, 0) + 1
            if count[n] <= 4:
                uniq.append((i, n))

        pairs = {}

        for xidx, x in uniq:
            for yidx, y in uniq:
                if yidx > xidx:
                    s = x + y
                    if s not in pairs:
                        pairs[s] = {}

                    pair = (xidx, yidx)

                    if pair in pairs[s]:
                        continue
                    
                    pairs[s][pair] = True

        qindices = {} # хэш (индексы) => (значения)
        qvalues = {}  # хэш (значения) => bool

        # цикл по всем парам
        for n in pairs:
            m = target - n

            # ранний выход если пар-кандидатов пары для данного n нет
            if m not in pairs:
                continue

            # перебираем все пары
            for p1 in pairs[n].keys():
                for p2 in pairs[m].keys():

                    qidx = tuple(set(list(p1) + list(p2)))

                    if len(qidx) != 4:
                        continue

                    if qidx in qindices:
                        continue

                    val = tuple(sorted([nums[idx] for idx in qidx]))

                    if val in qvalues:
                        continue

                    qindices[qidx] = True
                    qvalues[val] = True

        # превращаем tuple в list
        res = [list(k) for k in qvalues.keys()]

        return res


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0]) # сортируем интервалы по 0 индексу

        res = []
        prev = intervals[0] # предыдущий интервал

        # проходим по всем интервалам кроме первого
        for x in intervals[1:]:

            if prev[1] >= x[0]: # если конец предыдущего интервала попадает перекрывает следующий
                prev[1] = max(prev[1], x[1]) # объединяем интервалы - конец - максимум из двух концов
            else:
                # не перекрывает - добавляем предыдущий к результату
                res.append(prev)
                # предыдущий - текущий интервал
                prev = x

        # добавляем последний объединенный интервал
        res.append(prev)

        return res

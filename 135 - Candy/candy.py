class Solution:
    # @param {integer[]} ratings
    # @return {integer}
    def candy(self, ratings):
        n = len(ratings)
        total = 1
        count_descending = 0
        prev = 1
        for idx in range(1, n):
            if ratings[idx] >= ratings[idx - 1]:
                if count_descending > 0:
                    total += count_descending * (count_descending + 1) / 2
                    if count_descending >= prev:
                        total += count_descending + 1 - prev
                    prev = 1
                    count_descending = 0
                prev = prev + 1 if ratings[idx] > ratings[idx - 1] else 1
                total += prev
            else:
                count_descending += 1
                
        if count_descending > 0:
            total += count_descending * (count_descending + 1) / 2
            if count_descending >= prev:
                total += count_descending + 1 - prev
                
        return total
        

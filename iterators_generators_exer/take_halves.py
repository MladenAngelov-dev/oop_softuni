def solution():

    def intigers():
        num = 1
        while True:
            yield num
            num += 1

    def halves():
        for i in intigers():
            yield i / 2

    def take(n, seq):
        return [next(seq) for _ in range(n)]
        # result = []
        # for _ in range(n):
        #    result.append(next(seq))
        # return result

    return (take, halves, intigers)


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))

take = solution()[0]
halves = solution()[1]
print(take(0, halves()))
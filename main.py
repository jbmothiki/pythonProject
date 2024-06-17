def divisible_impairs(n, k, ary):
    score = 0
    for ai in range(n-1):
        for bi in range(1, (n-ai)):
            if (ary[ai] + ary[ai+bi]) % k == 0:
                score += 1
    print(score)


if __name__ == '__main__':
    divisible_impairs(6, 3, [1, 3, 2, 6, 1, 2])

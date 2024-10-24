def find_sum(n):
    if n == 1:
        return 1
    return n + find_sum(n - 1)


if __name__ == "__main__":
    print(find_sum(3))  # 6
    print(find_sum(5))  # 15
    print(find_sum(10))  # 55
    print(find_sum(100))  # 5050
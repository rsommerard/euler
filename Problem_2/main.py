def fibonacci(n):
    if n == 1 or n == 2:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    sum = 0
    prev = 0
    next = 1
    while True:
        if next > 4000000:
            break

        tmp = prev
        prev = next
        next = tmp + next

        if next % 2 == 0:
            sum += next

    print(sum)

if __name__ == '__main__':
    main()

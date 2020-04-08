def permutation(arr, length):
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    def generate(chosen, used):
        if len(chosen) == length:
            print(chosen)
            return

        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()

    generate([], used)


def combination(arr, length):
    arr = sorted(arr)

    def generate(chosen):
        if len(chosen) == length:
            print(chosen)
            return

        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for i in range(start, len(arr)):
            chosen.append(arr[i])
            generate(chosen)
            chosen.pop()

    generate([])






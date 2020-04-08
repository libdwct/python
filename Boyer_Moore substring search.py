def Boyer_Moore(target, data, idx):
    n = len(target)
    if data[idx] in target:
        cases = [i for i, x in enumerate(target) if x == data[idx] and idx+(n-1-i) < len(data)]

        for i in cases:
            cnt = 0
            for j in range(n):
                if data[idx+(n-1-i)-j] == target[n-1-j]:
                    cnt += 1
                else : break
            if cnt == n: return True

        if len(data)-(idx+1) >= n: return Boyer_Moore(target, data, idx+n)
        else: return False

    else:
        if len(data)-(idx+1) >= n: return Boyer_Moore(target, data, idx+n)
        else: return False
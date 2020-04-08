def find_palindrome(text, N, M):    # N*N text, M: length of palindrome
    for i in range(N-M+1):  # find vertical case
        for j in range(N):
            cnt = 0
            for k in range(M//2):   # the number of comparing
                if text[i+k][j] == text[i+M-k-1][j]:
                    cnt+=1
                else: break
            if cnt == M//2:
                result = ''
                for L in range(M):
                    result += text[i+L][j]
                return result
    for i in range(N):  # find horizontal case
        for j in range(N-M+1):
            cnt = 0
            for k in range(M // 2):
                if text[i][j+k] == text[i][j+M-k-1]:
                    cnt += 1
                else: break
            if cnt == M // 2:
                return text[i][j:j+M]

text = ['WPMACSIBIK', 'STWASDCOBQ', 'AMOUENCSOG', 'XTIIGBLRCZ', 'WXVSWXYYVU', 'CJVAHRZZEM',
        'NDIEBIIMTX', 'UOOGPQCBIW', 'OWWATKUEUY', 'FTMERSSANL']
N = 10
M = 10
print(find_palindrome(text, N, M))
def main():
    m, n = map(int, input().split())
    
    h = list(map(int, input().split()))
    d = list(map(int, input().split()))
    
    # Calculamos el HN máximo
    total = 0
    for x in d:
        total += x
    
    # El problema se modela como un DP mochila
    dp = [total] * (n)
    dp[0] = 0
    
    # Tratamos de quedarnos con el menor valor posible
    # tal que el peso actual de la mochila sea >= n
    mn_value = total
    
    for i in range(m):
        for j in reversed(range(n)):
            # Si el peso excede a n, minimizamos nuestro valor de mn_value
            if j + h[i] >= n:
                mn_value = min(mn_value, dp[j] + d[i])
            # En otro caso, calculamos dp[j+h[i]]
            else:
                dp[j+h[i]] = min(dp[j+h[i]], dp[j] + d[i])
    
    
    print(total - mn_value)

if __name__ == '__main__':
    main()

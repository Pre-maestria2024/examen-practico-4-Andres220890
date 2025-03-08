def main():

	m, n = map(int, input().split())
	H = list(map(int, input().split()))
	D = list(map(int, input().split()))

# Calculamos el HN máximo
total = 0
for x in D:
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
        if j + H[i] >= n:
            mn_value = min(mn_value, dp[j] + D[i])
        # En otro caso, calculamos dp[j+H[i]]
        else:
            dp[j+H[i]] = min(dp[j+H[i]], dp[j] + D[i])
	
if __name__ == '__main__':
	main()



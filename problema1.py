def main():
    m, n = map(int, input().split())
    H = list(map(int, input().split()))
    D = list(map(int, input().split()))

    # Calculamos el HN máximo
    total = sum(D)

    # El problema se modela como un DP de mochila
    dp = [total] * (n + 1)  # Asegurar tamaño correcto
    dp[0] = 0  # Caso base

    mn_value = total  # Inicializamos el valor mínimo posible

    for i in range(m):
        for j in reversed(range(n + 1)):  # Bucle en reversa para evitar sobreescribir estados previos
            if dp[j] < total:  # Asegurar que dp[j] es válido
                if j + H[i] >= n:
                    mn_value = min(mn_value, dp[j] + D[i])
                elif j + H[i] < len(dp):  # Validación de rango
                    dp[j + H[i]] = min(dp[j + H[i]], dp[j] + D[i])

    print(mn_value)  # Imprimir la solución final

if __name__ == '__main__':
    main()

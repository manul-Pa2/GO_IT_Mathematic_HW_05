# Задача 2. Аналіз доставки замовлень
# X ~ Binomial(n=50, p=0.88)

from math import sqrt
from scipy.stats import binom

def main():
    n = 50
    p = 0.88

    # 2.1) Математичне сподівання та стандартне відхилення
    EX = n * p
    sigma = sqrt(n * p * (1 - p))

    # 2.2) Ймовірність, що всі 50 доставлять вчасно: P(X = 50)
    p_x_50 = binom.pmf(50, n, p)

    # 2.3) Ймовірність, що рівно 45 доставлять вчасно: P(X = 45)
    p_x_45 = binom.pmf(45, n, p)

    # 2.4) Ймовірність, що вчасно доставлять від 42 до 46: P(42 <= X <= 46) = F(46) - F(41)
    p_42_46 = binom.cdf(46, n, p) - binom.cdf(41, n, p)

    # 2.5) Ймовірність, що більше 5 замовлень запізняться:
    #    (50 - X) > 5  <=>  X < 45  <=>  X <= 44  => P(X <= 44) = F(44)
    p_more_than_5_late = binom.cdf(44, n, p)

    print(f"Параметри: n={n}, p={p}")
    print("-" * 50)
    print(f"1) E[X] = {EX:.4f}")
    print(f"   σ    = {sigma:.4f}")
    print(f"2) P(X = 50) = {p_x_50:.10f}")
    print(f"3) P(X = 45) = {p_x_45:.10f}")
    print(f"4) P(42 ≤ X ≤ 46) = {p_42_46:.10f}")
    print(f"5) P(запізниться > 5) = P(X ≤ 44) = {p_more_than_5_late:.10f}")

if __name__ == "__main__":
    main()

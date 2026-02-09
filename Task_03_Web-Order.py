
from scipy.stats import expon
import math

# Параметри  #Показниковий розподіл: T ~ Exp(λ), де λ = 6 замовл/год = 0.1 замовл/хв
lam_per_min = 0.1              # λ (хв)
scale = 1 / lam_per_min       # scale = 1/λ => 10 хв

# Розподіл у SciPy: expon(loc=0, scale=scale)
dist = expon(scale=scale)

# 3.1) E[T] та стандартне відхилення σ
E_T = dist.mean()
sigma = dist.std()

# 3.2) P(T < 5)
p_less_5 = dist.cdf(5)

# 3.3) P(T > 15)
p_more_15 = dist.sf(15)     # sf = 1 - cdf

# 3.4) Проміжок від 5 до 15 хвилин  =>  P(5 <= T <= 15) або (5;15)
p_between_5_15 = dist.cdf(15) - dist.cdf(5)

# 3.5) Медіана (50-й перцентиль)
median = dist.ppf(0.5)

# Вивід результатів
print(f"λ = {lam_per_min} замовл/хв, scale = {scale} хв")
print("1) E[T] =", E_T, "хв")
print(" σ =", sigma, "хв")
print("2) P(T < 5) =", p_less_5)
print("3) P(T > 15) =", p_more_15)
print("4) P(5..15) =", p_between_5_15)
print("5) Median =", median, "хв")

# (Додатково) Перевірка формулами без SciPy:
# E[T] = 1/λ, σ = 1/λ, median = ln(2)/λ
print("\nПеревірка формулами:")
print("E[T] =", 1/lam_per_min)
print("σ =", 1/lam_per_min)
print("Median =", math.log(2)/lam_per_min)

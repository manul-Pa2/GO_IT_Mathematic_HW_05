

import math
from scipy.stats import t

# Вхідні дані
x_bar = 76.8
s = 14.2
n = 35
mu0 = 72
alpha = 0.05

# 4.1) Гіпотези:
# H0: μ = 72
# H1: μ ≠ 72
print("1) Гіпотези:")
print("   H0: μ = 72")
print("   H1: μ ≠ 72")

# 4.2) Стандартна похибка
SE = s / math.sqrt(n)

# 4.3) t-статистика
t_stat = (x_bar - mu0) / SE

# Ступені вільності
df = n - 1

# 4.4) p-value для двостороннього тесту через cdf:
# p = 2 * P (T <= -|t|)
p_value = 2 * t.cdf(-abs(t_stat), df=df)

print("\n2) SE =", SE)
print("3) t =", t_stat)
print("4) p-value =", p_value)

# 4.5) 95% довірчий інтервал: x̄ ± t_crit * SE
t_crit = t.ppf(1 - alpha/2, df=df)
ci_low = x_bar - t_crit * SE
ci_high = x_bar + t_crit * SE

print("\n5) 95% ДІ для μ:")
print(f" t_crit = {t_crit}")
print(f" CI = [{ci_low}, {ci_high}]")

# 4.6) Висновок при α = 0.05
print("\n6) Висновок (α = 0.05):")
if p_value < alpha:
    print(" Відхиляємо H0: є статистично значущі докази, що середній бал змінився (методика вплинула).")
else:
    print(" Не відхиляємо H0: статистично значущих доказів зміни середнього бала немає.")

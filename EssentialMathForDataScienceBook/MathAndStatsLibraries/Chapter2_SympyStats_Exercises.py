from scipy.stats import beta, binom

# Ex. 4

n = 137
p = 0.40

probability = 0
for k in range(50, n+1):
    probability += binom.pmf(k, n, p)
print(probability)


# Ex. 5

heads = 15
tails = 4

p = beta.cdf(0.50, heads, tails)
print(p)

p = beta.cdf(0.50, tails, heads)
print(p)

#
# Monte Carlo valuation of European call option
# in Black-Scholes-Merton model
# 

## Paramter values
S0 = 100    # initial  index level

K = 105     # Strick price

T = 1.0     # time-to-maturity

r = 0.05    # riskless short rate

sigma = 0.2  # volatility

## Import valuation algo
import numpy as np
import random as rd
import math

I = 100000  ## Number of simulations

z = np.random.standard_normal(I)  # pseudo random numbers

ST = S0 * np.exp(( r -0.5 *sigma **2) * T + sigma *np.sqrt(T) * z )
# Index values at maturity
hT = np.maximum(ST - K, 0)  # inner vlaues at maturity

C0  = np.exp(-r  * T) * sum(hT)/I   ## Monte Carlo estimator

## result and output
print("Value of the European Call Option %5.3f" % C0)



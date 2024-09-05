## forward modelling untuk membuat data sintetik regresi linier
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# prediksi temperatur terhadap ke dalaman di bawah permukaan
# T = a + bz (T=temperatur, z=kedalaman, variabel bebas, a dan b=parameter model)

# paramater model (m)
a = 1
b = 0.5
m = np.array([a, b])

xi = np.arange(1,11)

d = np.zeros(len(xi))
G = np.column_stack([xi**0, xi])
d = G.dot(m)

noise = np.random.normal(0,0.2,len(xi))
dnoise = d+noise

df = {"xi":xi, "y":d, "y_noise":dnoise}
df = pd.DataFrame(df)
#df.to_csv("output_fm.csv", index=False)

print(df)
plt.plot(xi,d, '-', label="d sintetik")
plt.plot(xi,dnoise,'o', label=f"d dengan noise")
plt.legend()
plt.ylabel("y")
plt.xlabel("x")
plt.show()




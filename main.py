import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
def myfunc(x):
  return slope * x + intercept


df = pd.read_csv("Stores.csv")
df.drop(df.columns[[0]], axis = 1, inplace = True)  # remove o id
sns.set()
sns.pairplot(df,diag_kind='kde',kind ='reg', height = 3)
plt.show(block = True)
corrmat = df.corr()
plt.subplots(figsize = (5,5))
sns.heatmap(corrmat, vmax=.8, linewidths=0.01, square=True, annot=True, linecolor="white",annot_kws = {'size':12})
plt.show(block = True)
x = df["Store_Area"]
y = df["Items_Available"]
slope, intercept, r, p, std_err = stats.linregress(x, y)
mymodel = list(map(myfunc, x))
plt.scatter(x, y)
plt.plot(x, mymodel, color="r")
plt.show(block = True)

print("B0 =", slope)
print("B1 =", intercept)
print("Erro =", std_err)
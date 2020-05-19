from numpy import random
from numpy import array
from numpy import mean
import json
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(color_codes=True)

with open("PET_paramaribo.json") as petfile:
    ET = array(json.load(petfile)[:365])

days = array(range(365))


# # quick show me
# sns.distplot(normal_transform)
# plt.show()

normal_transform = random.normal(3.3, 0.5, 365) 
pan_et = normal_transform * ET
# sns.lineplot(days, pan_et)
# sns.lineplot(days, ET)
# plt.show()
lim = 10
train_ET = ET[:lim]
train_pan = pan_et[:lim]
model = sm.OLS(train_ET, train_pan).fit()
res = model.predict(pan_et)
print(model.summary())

## very dumb regression, stops working better than OLS when the equation is ax + b
coefficient = mean(train_pan / train_ET)
res1 = pan_et / coefficient
print("Dumb implementation", coefficient)

sns.lineplot(days, pan_et, label="measured(pan)")
sns.lineplot(days, ET, label="FAO")
sns.lineplot(days, res, label="predicted ET(Ordinary Least Squares)")
sns.lineplot(days, res1, label="predicted ET(own 'regrassion')")
plt.ylim([0,20])
plt.show()
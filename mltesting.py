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



# simulate the values you'd be measuring. Say we have a pan with pan factor of 3.3
# the higher the std is , the worse the predictions become and the more datapoints we need to predict accurately
normal_transform = random.normal(3.3, 0.5, 365)  # 0.5 is the standard deviation. 
pan_et = normal_transform * ET # values you'd be measuring.


# # quick show me the distribution of the normal transform
# sns.distplot(normal_transform)
# plt.show()


lim = 10 # days measured, ammount of data points
train_ET = ET[:lim]
train_pan = pan_et[:lim]
model = sm.OLS(train_ET, train_pan).fit()
res = model.predict(pan_et)
print(model.summary())

## very naive "regression", stops working better than OLS when the equation is ax + b
coefficient = mean(train_pan / train_ET)
res1 = pan_et / coefficient
print("Dumb implementation", coefficient)

sns.lineplot(days, pan_et, label="measured(pan)")
sns.lineplot(days, ET, label="FAO")
sns.lineplot(days, res, label="predicted ET(Ordinary Least Squares)")
# sns.lineplot(days, res1, label="predicted ET(own 'regrassion')") # removed for clarity's sake
plt.ylim([0,20])
plt.show()
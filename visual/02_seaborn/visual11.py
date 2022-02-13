import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

penguins = sns.load_dataset('penguins')

"""
species : 종
island : 서식지
bill_length_mm : 부리의 길이
bill_depth_mm : 부리의 깊이
flipper_length_mm : 날개의 길이
body_mass_g : 체질량
sex : 성별
"""

# sns.pairplot(penguins, hue='sex')
sns.pairplot(penguins, kind='reg')   # kind 속성에 들어갈 수 있는 것들 찾아보기

plt.show()
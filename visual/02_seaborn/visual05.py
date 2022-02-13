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

sns.boxplot(data=penguins, x='species', y='bill_length_mm')   # 종 별 부리의 길이

plt.show()
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

# sns.scatterplot(data=penguins, x='body_mass_g', y='flipper_length_mm')   # --> 두 값은 관계가 있어보임. 축에 더 가까울수록 더욱 관계가 있음
# sns.scatterplot(data=penguins, x='body_mass_g', y='flipper_length_mm', hue="species", size='sex')
sns.scatterplot(data=penguins, x='body_mass_g', y='flipper_length_mm', hue="species", style='sex')

plt.show()
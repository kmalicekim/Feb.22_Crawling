# pip install seaborn
# seaborn website > Utility functions > load_dataset

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.max_columns = None    # 중간에 ... 으로 값들 줄여서 표시되게 하지 않기위해 (모든 데이터를 다 보기 위해 설정)
pd.options.display.max_rows = None

# print(sns.get_dataset_names())   # https://github.com/mwaskom/seaborn-data
car_crashes = sns.load_dataset('car_crashes')
# print(car_crashes)   # dataframe 형태

"""
total : 전체 사고 건수
speeding : 과속 비율
alcohol : 음주 비율
not_distracted : Percentage Of Drivers Involved In Fatal Collisions Who Were Not Distracted
no_previous : 이전에 사고가 없었던 운전자 비율
ins_premium : 자동차 보험료
ins_losses : 운전자 1인당 충돌사고로 보험사가 입은 손해
abbres : 미국 주 약자
"""

plt.figure(figsize=(15,10))

sns.barplot(data=car_crashes, x='abbrev', y='total')
plt.show()






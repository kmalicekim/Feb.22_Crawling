import matplotlib.pyplot as plt
# pip install matplotlib ---> 터미널에 작성 후

fig = plt.figure()   # figure : 도화지 전체라고 생각

ax = fig.subplots()  # 도화지를 몇 개로 나눌 것인가

ax.plot([1,2,3,4,5])

plt.show()

from sklearn.manifold import TSNE
import pandas as pd
import matplotlib.pyplot as plt


def t_sne(data_zs, model):
    tsne = TSNE(learning_rate=100)
    # 对数据进行降维
    tsne.fit_transform(data_zs)
    data = pd.DataFrame(tsne.embedding_, index=data_zs.index)

    # 不同类别用不同颜色和样式绘图
    d = data[model.labels_ == 0]
    plt.plot(d[0], d[1], 'r.')
    d = data[model.labels_ == 1]
    plt.plot(d[0], d[1], 'g')
    d = data[model.labels_ == 2]
    plt.plot(d[0], d[1], 'b')
    d = data[model.labels_ == 3]
    plt.plot(d[0], d[1], 'c')
    d = data[model.labels_ == 4]
    plt.plot(d[0], d[1], 'k')
    d = data[model.labels_ == 5]
    plt.plot(d[0], d[1], 'y')
    plt.show()


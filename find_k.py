from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import pandas as pd


def find_the_best_k(features):
    SSE = []  # sum of the squared errors，误差平方和,越小越好
    Score = []  # 轮廓系数，越大越好
    Calinski_harabaz_score = []  # 分数值s越大则聚类效果越好。

    for k in range(2, 11):
        km_cluster = KMeans(n_clusters=k)
        km_cluster.fit(features)
        result = km_cluster.fit_predict(features)
        SSE.append(km_cluster.inertia_)
        Score.append(silhouette_score(features, km_cluster.labels_, metric='euclidean'))
        Calinski_harabaz_score.append(metrics.calinski_harabaz_score(features, result))  # 分数值s越大则聚类效果越好。
        print("n_clusters=" + str(k) + ", Predicting result: ")
        print(result)

    k = range(2, 11)
    plt.subplot(131)  # 绘制1行3列的子图，131为第一个子图
    plt.xlabel('k')
    plt.ylabel('SSE')
    plt.plot(k, SSE, 'o-')

    plt.subplot(132)
    plt.xlabel('k')
    plt.ylabel('Score')
    plt.plot(k, Score, 'o-')

    plt.subplot(133)
    plt.xlabel('k')
    plt.ylabel('Calinski_harabaz_score')
    plt.plot(k, Calinski_harabaz_score, 'o-')
    plt.show()
    plt.savefig("forward.png")

    best_k = input("best k =")
    model = KMeans(n_clusters=int(best_k))
    best_result = model.fit_predict(features)

    tsne = TSNE(learning_rate=100)
    # 对数据进行降维
    tsne.fit_transform(features)
    data = pd.DataFrame(tsne.embedding_, index=features.index)

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
    return best_result


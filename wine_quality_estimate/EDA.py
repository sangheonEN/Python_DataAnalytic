import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt


#%% check outlier

def check_outlier(dataframe):
    """
    find outlier each column
    pandas.dataframe.isna() -> output table type: Bool (True or False) [[true, false, ...]]

    :param dataframe
    :return dataframe outlier
    """
    counted_missing_col = 0
    for i, col in enumerate(dataframe):
        missing_values = sum(dataframe[col].isna())
        is_missing = True if missing_values >= 1 else False

        if is_missing:
            counted_missing_col += 1
            print(f"outlier column: {col}")
            print(f"{col} total outlier num: {missing_values}")

        if i == len(dataframe.columns) - 1 and counted_missing_col == 0:
            print("there is not outlier")


#%% check class distribution
def class_distribution(dataframe):
    counted_value = dataframe["quality"].value_counts()
    plt.style.use("ggplot")
    plt.figure(figsize=(12, 10))
    plt.title("class counting", fontsize = 30)
    value_bar_ax = sns.barplot(x=counted_value.keys(), y=counted_value)
    value_bar_ax.tick_params(labelsize=20)


def feature_mean_graph(dataframe):
    """
    quality column별로 dataframe을 새로 만들고
    id, quality col을 삭제하고 각 col별로 describe()로 통계량을 계산해줌
    describe()로 통계량을 계산해준 dataframe에서 각 col별 mean의 dataframe을 가져와서 col별로 concat한다. 열기준으로 붙임. axis = 1 나중에 transpose
    subplot 만들어서 각 col line chart 그림.
    :param dataframe: dataframe
    :return: N/A
    """

    qualities = {}

    for i in range(4, 9):
        quality_description = dataframe[dataframe["quality"]== i].drop(["id", "quality"], axis= 1).describe()
        if i == 4:
            means = pd.DataFrame({i:quality_description.loc["mean"]})
        else:
            mean = pd.DataFrame({i:quality_description.loc["mean"]})
            means = pd.concat([means, mean], axis = 1)

    means = means.T
    fig, axes = plt.subplots(4, 3, figsize=(25, 15))

    # mean value
    fig.suptitle('mean values per quality', fontsize=40)
    for ax, col in zip(axes.flat, means.columns):
        ax.plot([4, 5, 6, 7, 8], means[col])
        ax.scatter([4, 5, 6, 7, 8], means[col])
        ax.set_title(col, fontsize=20)
    plt.setp(axes, xticks=[4, 5, 6, 7, 8])
    plt.tight_layout()
    plt.show()

    # distributions
    fig, axes = plt.subplots(4, 3, figsize=(25, 15))

    fig.suptitle('feature distributions per quality', fontsize=40)
    for ax, col in zip(axes.flat, train.columns[1:]):
        sns.violinplot(x='quality', y=col, ax=ax, data=train)
        ax.set_title(col, fontsize=20)
    plt.tight_layout()
    plt.show()


def relationship_heatmap(dataframe):
    """
    dataframe에서 필요없는 col은 없애고 dataframe.drop.corr()로 col별 상관행렬을 얻음
    seaborn에서 제공하는 seaborn.heatmap 기능 사용

    """

    plt.figure(figsize=(20, 10))

    heat_table = dataframe.drop(['id'], axis=1).corr()
    heatmap_ax = sns.heatmap(heat_table, annot=True, cmap='coolwarm')
    heatmap_ax.set_xticklabels(heatmap_ax.get_xticklabels(), fontsize=15, rotation=45)
    heatmap_ax.set_yticklabels(heatmap_ax.get_yticklabels(), fontsize=15)
    plt.title('correlation between Wine features', fontsize=40)
    plt.show()


def hist_plot(dataframe):
    # positive feature
    fig, axes = plt.subplots(2, 2, figsize=(30, 10))

    for i in range(4):
        if i == 0:
            sns.histplot(x='free sulfur dioxide', y='total sulfur dioxide', ax=axes[0,0], hue='quality', data=dataframe)
            axes[0,0].set_title("free and total sulfur dioxide", fontsize=20)
        elif i == 1:
            sns.histplot(x='free sulfur dioxide', y='total sulfur dioxide', ax=axes[0,1], hue='type', data=dataframe)
            axes[0,1].set_title("free and total sulfur dioxide", fontsize=20)
        elif i == 2:
            sns.histplot(x='density', y='alcohol', ax=axes[1,0], hue='quality', data=dataframe.drop(dataframe[dataframe["density"] == max(dataframe['density'])].index))
            axes[1,0].set_title("density and alcohol", fontsize=20)
        else:
            sns.histplot(x='density', y='alcohol', ax=axes[1,1], hue='type', data=dataframe.drop(dataframe[dataframe["density"] == max(dataframe['density'])].index))
            axes[1,1].set_title("density and alcohol", fontsize=20)

    fig.suptitle('positive and negative hist plot', fontsize=40)
    plt.show()

    # negative feature

if __name__ == "__main__":
    """
     pd.read_csv("csv path")

     parameter: csv path
     return: dataframe -> [id, value]
    """

    # data load
    train = pd.read_csv("./dataset/train.csv")
    train.head()

    # outlier check
    check_outlier(train)

    # check class distribution
    class_distribution(train)

    # data imbalance solution SMOTE

    # class by feature
    feature_mean_graph(train)

    # heatmap relationship by feature
    relationship_heatmap(train)

    # positive, negative feature hist plot
    hist_plot(train)



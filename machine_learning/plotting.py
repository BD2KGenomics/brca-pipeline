import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import textwrap

def bar_plot(df):
    print df.mean()
    n_groups = len(df.columns)

    columns = df.mean().sort(inplace=False).index.tolist()
    means = [i for i in df.mean().sort(inplace=False)]
    #means = [i for i in df.mean()]
    std = [i for i in df.describe().loc["std"]]
    index = np.arange(n_groups)
    bar_width = 0.9

    opacity = 0.4
    error_config = {'ecolor': '0.3'}

    rect = plt.bar(index, means, bar_width,
                     alpha=opacity,
                     color='b',
                     yerr=std,
                     error_kw=error_config,
                     #label='haha'
                           )

    plt.ylabel('Weight')
    #plt.xlabel()
    plt.title('weights in logistic regression')

    labels=[text.split("=")[-1] for text in columns]
    plt.xticks(index + bar_width/2, labels)
    for x, y in zip(index, means):
        plt.text(x, y + 0.002, str(y)[0:5])

    mpl.rcParams['xtick.labelsize'] = 15
    plt.tight_layout()
    plt.show()


def two_series_bar_plot(result1, result2):
    n_groups = len(result2)
    columns = sorted(result2.keys())
    means = [[], []]
    stds = []
    for index, result in enumerate([result1.mean().to_dict(), result2]):
        for column in columns:
            means[index].append(result[column])
    for column in columns:
        stds.append(result1.describe().loc["std"].to_dict()[column])


    index = np.arange(n_groups)
    bar_width = 0.4
    opacity = 0.4
    rect1 = plt.bar(index, means[0], bar_width,
                    alpha=opacity,
                    yerr=stds,
                    color='b')
    rect2 = plt.bar(index+bar_width, means[1], bar_width,
                 alpha=opacity,
                 color='r')
    plt.ylim([0.88, 1])
    plt.ylabel('Accuracy Score')
    plt.xlabel("")
    plt.title('Comparing validation and test accuracy')

    labels = [text for text in columns]
    plt.xticks(index + bar_width, labels)
    plt.legend(["cross validation accuracy", "test accuracy"])
    plt.tight_layout()
    plt.show()

def lr_plot(result1, result2):

    n_groups = len(result2.columns)
    print n_groups
    columns = result2.columns
    means = [[], []]
    stds = [[], []]

    for column in columns:
        means[0].append(result1.mean()[column])
        stds[0].append(result1.describe().loc["std"].to_dict()[column])
        means[1].append(result2.mean()[column])
        stds[1].append(result2.describe().loc["std"].to_dict()[column])

    print len(means[0])

    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.4
    error_config = {'ecolor': '0.3'}

    rect1 = plt.bar(index, means[0], bar_width,
                    alpha=opacity,
                    yerr=stds[0],
                    color='b',
                    error_kw=error_config)
    rect2 = plt.bar(index+bar_width, means[1], bar_width,
                    alpha=opacity,
                    yerr=stds[1],
                    color='r',
                    error_kw=error_config)
    plt.ylim([0.88, 0.96])
    plt.ylabel('Accuracy Score')
    plt.xlabel("")
    plt.title('Logistic Regression')

    labels = [text for text in columns]
    plt.xticks(index + bar_width, labels)
    plt.legend(["L1 regularization", "L2 regularization"])
    plt.tight_layout()
    plt.show()



if __name__ == "__main__":
    bar_plot(df=pd.DataFrame())
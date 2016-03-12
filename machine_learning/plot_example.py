import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import textwrap

def bar_plot(df):
    n_groups = len(df.columns)
    means = [i for i in df.mean()]
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

    plt.ylim([0.88, 1])
    plt.ylabel('Accuracy Score')
    plt.xlabel("")
    # plt.title('')

    labels=[text.split("=")[-1] for text in df.columns]
    plt.xticks(index + bar_width/2, labels)
    for x, y in zip(index, means):
        plt.text(x, y + 0.002, str(y)[0:5])

    mpl.rcParams['xtick.labelsize'] = 15
    plt.tight_layout()
    plt.show()



if __name__ == "__main__":
    bar_plot(df=pd.DataFrame())
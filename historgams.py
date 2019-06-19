import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

def histogram(x):
    plt.hist(x, bins=20, range=[0, max(x)])
    #plt.xlabel("avg_pairwise_dist")
    plt.xlabel("diameter")
    plt.ylabel("frequency")
    plt.show()


def main():
    sns.set()
    csv_fn = "avg_pairwise_dist_geodesic.csv"

    df = pd.read_csv(csv_fn)
    avg_pw_values = df.avg_pw_dist.values
    diameter_values = df.diameter.values
    x = np.array(diameter_values)
    #print(avg_values)
    #x = np.array(avg_pw_values)
    #print("Minimum avg pairwise dist is  ", min(x))
    #print("Maximum avg pairwise dist is  ", max(x))
    print("Minimum diameter is  ", min(x))
    print("Maximum diameter is  ", max(x))

    histogram(x)

    #comm_min = df.loc[df['avg_pw_dist'] == min(x)]
    comm_min = df.loc[df['diameter'] == min(x)]
    print(comm_min)

    #comm_max = df.loc[df['avg_pw_dist'] == max(x)]
    comm_max = df.loc[df['diameter'] == max(x)]
    print(comm_max)


if __name__ == '__main__':
    main()
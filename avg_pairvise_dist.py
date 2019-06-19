import csv
import pandas as pd
from scipy.spatial import distance
import numpy as np
import math
import geopy
from geopy.distance import geodesic

def test_geodesic():
    newport_ri = (41.49008, -71.312796)
    cleveland_oh = (41.499498, -81.695391)
    print(geodesic(newport_ri, cleveland_oh).miles)


def test():
    # EPSG:4326 coord in degrees
    a = (45.47619, 9.05812)
    b = (45.47618, 9.06112)
    c = (45.47830, 9.06113)
    print(geodesic(a, c).meters)


    # EPSG:3857 coord in meters
    ap = (1008345.10171, 5696801.37462)
    bp = (1008679.80177, 5696801.12548)
    cp = (1008680.05636, 5697136.94088)
    dst = distance.euclidean(ap, cp)
    #my_dist = math.sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2))
    #print(my_dist)
    #print(dst)

def pw_dist(a, b, da):
    #dst = distance.euclidean(a, b) #not Euclidian! You need geodesic distance...
    dst = geodesic(a, b).meters
    da.append(dst)
    return da

def cells_pw():
    file = open("cells_comm_coord_Nov08.csv", 'r')
    wfile = open("avg_pairwise_dist_geodesic.csv", 'w')
    wfile.write("communityId, avg_pw_dist, diameter" + '\n')
    df = pd.read_csv(file)
    uncommid = df.commid.unique()
    for comm in uncommid:
        dst_array = []
        df_subs = df.loc[df['commid'] == comm]
        for i in df_subs['cellid']:
            df_subs_i = df_subs.loc[df['cellid'] == i]
            xi = df_subs_i.iloc[0]['xcoord']
            yi = df_subs_i.iloc[0]['ycoord']
            a = (xi, yi)
            for j in df_subs['cellid']:
                df_subs_j = df_subs.loc[df['cellid'] == j]
                xj = df_subs_j.iloc[0]['xcoord']
                yj = df_subs_j.iloc[0]['ycoord']
                b = (xj, yj)

                if i != j:
                    dist_array = pw_dist(a, b, dst_array)

        avg = np.mean(dist_array)
        diameter = np.max(dist_array)
        print(comm, avg, diameter)
        wfile.write(str(comm) + ',' + str(avg) + ',' + str(diameter) + '\n')

    file.close()
    wfile.close()



def main():
    cells_pw()
    #test()
    #test_geodesic()

if __name__ == "__main__":
    main()


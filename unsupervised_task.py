import numpy as np
from sklearn.cluster import KMeans
def main():
    #Data: Marks and attendance
    data = np.array([
        [85,90],
        [78,92],
        [80,88],
        [70,85],
        [60,80],
        [55,75],
        [50,70],
        [45,65]
    ])
    #create Model
    model = KMeans(n_clusters=3)
    #train model
    model.fit(data)

    print("Clusters labels")
    for i,point in enumerate(data):
        print(f"student {i+1} ->clusters{model.labels_[i]}")
if __name__ == "__main__":
    main()


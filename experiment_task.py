import numpy as np
from sklearn.linear_model import LinearRegression
def main():
    #Try different dataset

    x = np.array([[1], [2], [3], [4], [5]])
    y = np.array([40, 50, 60, 70, 80])

    model  = LinearRegression()
    model.fit(x , y)

    test_values = [2.5 , 3.5 , 7]
    print("Experiment Results:")
    for val in test_values:
        pred = model.predict([[val]])
        print(f"{val} hours → {pred[0]:.2f} marks")
    print("\nModel Insights")
    print("Slope (weight)", model.coef_[0])
    print("Intercpet:" , model.intercept_)
if __name__ == "__main__":
    main()
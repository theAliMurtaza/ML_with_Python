import numpy as np
from sklearn.linear_model import LinearRegression

def main():
    # Study hours (features)
    x = np.array([[1], [2], [3], [4], [5]])

    # Student marks (target)
    y = np.array([40, 50, 60, 70, 80])

    # Create model
    model = LinearRegression()

    # Train model
    model.fit(x, y)

    # Predictions
    print("Predictions:")

    for hours in range(1, 8):
        pred = model.predict([[hours]])
        print(f"{hours} hours → {pred[0]:.2f} marks")

if __name__ == "__main__":
    main()
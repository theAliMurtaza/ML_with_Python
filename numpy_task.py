import numpy as np

def main():
    arr = np.array([10, 20, 30, 40, 50])
    print("Original Array:", arr)

    print("\nAdd 5:", arr + 5)
    print("Multiply by 2:", arr * 2)

    print("\nMean:", arr.mean())
    print("Sum:", arr.sum())
    print("Max:", arr.max())
    print("Min:", arr.min())

    print("\nFirst 3 elements:", arr[:3])

    # ✅ Fixed matrix
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    print("\nMatrix:\n", matrix)

    # Extra (recommended)
    print("\nMatrix shape:", matrix.shape)
    print("Matrix * 2:\n", matrix * 2)

if __name__ == "__main__":
    main()
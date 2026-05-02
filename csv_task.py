import pandas as pd

def main():
    df = pd.read_csv("students.csv")
    print("DataFrame:\n", df)

    # Basic Information
    print("\nBasic Info:")
    df.info()

    # Statistical summary
    print("\nStatistical Summary:\n", df.describe())

    # Grade function
    def grades(marks):
        if marks >= 90:
            return "A"
        elif marks >= 80:
            return "B"
        elif marks >= 70:
            return "C"
        elif marks >= 60:
            return "D"
        elif marks >= 50:
            return "E"
        else:
            return "F"

    # Apply grading
    df["Grades"] = df["Marks"].apply(grades)

    print("\nUpdated DataFrame:\n", df)

if __name__ == "__main__":
    main()
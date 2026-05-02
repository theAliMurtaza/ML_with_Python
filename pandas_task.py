import pandas as pd
def main():
    data = {
        "Name": ["Ali" , "Ahmed" , "Sara" , "Zainab"],
        "Marks": [85 , 90 , 78 , 92]
    } 
    df =pd.DataFrame(data)
    print("DataFrame:\n" , df)

    df["Passed"] = df["Marks"] >= 70
    def assign_grade(marks):
        if marks >= 90:
            return "A"
        elif marks >= 80:
            return "B"
        elif marks >= 70:
            return "C"
        else:
            return "F"
    df["Grade"] = df["Marks"].apply(assign_grade)
    print("\n Updated DataFrrame:\n" , df)
    highest_marks = df[df["Marks"] > 80]
    print("\nStudents with marks greater than 80:\n" , highest_marks)
    sorted_df = df.sort_values(by="Marks" , ascending=False)
    print("\nDataFrame sorted by Marks (descending):\n" , sorted_df )
if __name__ == "__main__":
    main()
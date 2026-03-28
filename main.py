import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

print("\n--- Expense Analysis & Predictor ---")

while True:
    # Always reload latest CSV data
    try:
        data = pd.read_csv("expenses.csv")
    except:
        print("Error: expenses.csv not found!")
        break

    print("\n1. Show Analysis")
    print("2. Predict Expense")
    print("3. Exit")

    choice = input("Enter choice: ")

    # ✅ Show analysis
    if choice == '1':
        if len(data) == 0:
            print("No data!")
        else:
            print("Total:", data['expense'].sum())
            print("Average:", round(data['expense'].mean(), 2))

            plt.plot(data['day'], data['expense'], marker='o')
            plt.xlabel("Day")
            plt.ylabel("Expense")
            plt.title("Expense Graph")
            plt.show()

    # ✅ Prediction
    elif choice == '2':
        if len(data) < 3:
            print("Need more data!")
        else:
            X = data[['day']]
            y = data['expense']

            model = LinearRegression()
            model.fit(X, y)

            future_days = np.arange(1, 31).reshape(-1, 1)
            pred = model.predict(future_days)

            print("Predicted Monthly Expense:", round(pred.sum(), 2))

    # Exit
    elif choice == '3':
        print("Exiting...")
        break

    else:
        print("Invalid choice")
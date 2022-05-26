# circle diagram of expenses
import matplotlib.pyplot as plt

def main():

    expenses = [400, 100, 300, 200, 150, 350]
    slice_labels = ['rent', 'gas', 'food', 'clothe', 'car payment', 'other']

    plt.pie(expenses, labels = slice_labels)
    plt.title('My expenses')
    plt.show()

main()

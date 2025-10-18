import csv

file_path = "expenses_astana.csv"

expenses = [
    {"date": "2025-08-11", "amount": 2000, "item": "hot chocolate", "category": "drinks"},
    {"date": "2025-08-11", "amount": 4000, "item": "dinner, breakfast, home", "category": "bazaar"},
    {"date": "2025-08-11", "amount": 1400, "item": "notebook and scissors", "category": "stationary"},
    {"date": "2025-08-11", "amount": 1750, "item": "dinner", "category": "dinner"},
    
    {"date": "2025-08-12", "amount": 900, "item": "breakfast", "category": "breakfast"},
    {"date": "2025-08-12", "amount": 270, "item": "rice", "category": "lunch"},
    {"date": "2025-08-12", "amount": 500, "item": "soup", "category": "lunch"},
    {"date": "2025-08-12", "amount": 5000, "item": "paracetamol, groprinosil, furacelin", "category": "medicine"},
    {"date": "2025-08-12", "amount": 9500, "item": "sim card", "category": "mobile operator"},
    {"date": "2025-08-12", "amount": 500, "item": "insti", "category": "medicine"},
    {"date": "2025-08-12", "amount": 800, "item": "onigiri", "category": "dinner"},
    
    {"date": "2025-08-13", "amount": 1100, "item": "pancakes with meat", "category": "breakfast"},
    {"date": "2025-08-13", "amount": 1500, "item": "sandwich", "category": "lunch"},
    {"date": "2025-08-13", "amount": 300, "item": "banana and Tuc", "category": "snacks"},

    {"date": "2025-08-14", "amount": 1750, "item": "breakfast", "category": "breakfast"},
    {"date": "2025-08-14", "amount": 1500, "item": "lunch", "category": "lunch"},
    {"date": "2025-08-14", "amount": 450, "item": "trifle dessert", "category": "snacks"},
    
    {"date": "2025-08-15", "amount": 1950, "item": "breakfast (mine and Yasminas)", "category": "breakfast"},
    {"date": "2025-08-15", "amount": 2000, "item": "fruits", "category": "fruits"},

    {"date": "2025-08-16", "amount": 750, "item": "breakfast (mine and Yasminas)", "category": "breakfast"},
    {"date": "2025-08-16", "amount": 1000, "item": "Moroccan tea", "category": "drinks"},
    {"date": "2025-08-16", "amount": 2470, "item": "lunch in cafeteria", "category": "lunch"},
    
    {"date": "2025-08-17", "amount": 800, "item": "breakfast", "category": "breakfast"},
    {"date": "2025-08-17", "amount": 5000, "item": "beshbarmak", "category": "lunch"},
    {"date": "2025-08-17", "amount": 1000, "item": "tea", "category": "drinks"},
    {"date": "2025-08-17", "amount": 1000, "item": "taxi", "category": "transport"},
    {"date": "2025-08-17", "amount": 1000, "item": "onigiri", "category": "dinner"},
    
    {"date": "2025-08-18", "amount": 800, "item": "sausage, egg, bread", "category": "breakfast"},
    {"date": "2025-08-18", "amount": 550, "item": "notebook", "category": "stationary"},
    {"date": "2025-08-18", "amount": 800, "item": "onigiri", "category": "lunch"},
    {"date": "2025-08-18", "amount": 1320, "item": "dinner", "category": "dinner"},
    {"date": "2025-08-18", "amount": 1500, "item": "yogurt, Barni, apples", "category": "snacks"},
    
    {"date": "2025-08-19", "amount": 650, "item": "breakfast", "category": "breakfast"},
    {"date": "2025-08-19", "amount": 1840, "item": "lunch", "category": "lunch"},
    {"date": "2025-08-19", "amount": 800, "item": "dinner", "category": "dinner"},
    
    {"date": "2025-08-20", "amount": 1050, "item": "breakfast", "category": "breakfast"},
    {"date": "2025-08-20", "amount": 100, "item": "lunch", "category": "lunch"},
    {"date": "2025-08-20", "amount": 300, "item": "ice cream", "category": "snacks"},
    {"date": "2025-08-20", "amount": 1410, "item": "dinner", "category": "dinner"},

    {"date": "2025-08-21", "amount": 650, "item": "breakfast", "category": "breakfast"},
    {"date": "2025-08-21", "amount": 890, "item": "onigiri", "category": "lunch"},
    {"date": "2025-08-21", "amount": 1500, "item": "self-made pasta", "category": "dinner"},
    
    {"date": "2025-08-22", "amount": 700, "item": "breakfast", "category": "breakfast"},
    {"date": "2025-08-22", "amount": 55, "item": "water refill", "category": "water"},
    {"date": "2025-08-22", "amount": 1100, "item": "sandwich", "category": "lunch"},
    {"date": "2025-08-22", "amount": 350, "item": "taxi", "category": "transport"},
    {"date": "2025-08-22", "amount": 600, "item": "taxi", "category": "transport"},
    {"date": "2025-08-22", "amount": 110, "item": "bus", "category": "transport"},
    {"date": "2025-08-22", "amount": 6750, "item": "medical insurance", "category": "medicine"},
    {"date": "2025-08-22", "amount": 110, "item": "bus", "category": "transport"},
    {"date": "2025-08-22", "amount": 300, "item": "ice cream", "category": "snacks"},
    
    {"date": "2025-08-23", "amount": 770, "item": "breakfast", "category": "breakfast"},
    {"date": "2025-08-23", "amount": 890, "item": "onigiri", "category": "lunch"},
    {"date": "2025-08-23", "amount": 890, "item": "Moroccan tea", "category": "drinks"},
    {"date": "2025-08-23", "amount": 650, "item": "fruits", "category": "fruits"},
    
    {"date": "2025-08-24", "amount": 609, "item": "banana and yogurt", "category": "breakfast"},
    {"date": "2025-08-24", "amount": 1455, "item": "two meatballs and mashed potatoes", "category": "lunch"},
    {"date": "2025-08-24", "amount": 300, "item": "ice cream", "category": "snacks"},
    {"date": "2025-08-24", "amount": 1300, "item": "chicken roll", "category": "dinner"},
    
    {"date": "2025-08-25", "amount": 1590, "item": "set: croissant, sausage, two eggs, tomatoes, bryndza cheese", "category": "breakfast"},
    {"date": "2025-08-25", "amount": 1950, "item": "cocoa", "category": "drinks"},
    {"date": "2025-08-25", "amount": 1130, "item": "lunch", "category": "lunch"},

    {"date": "2025-08-26", "amount": 200, "item": "cabbage pie", "category": "breakfast"},
    {"date": "2025-08-26", "amount": 1250, "item": "lunch", "category": "lunch"},
    {"date": "2025-08-26", "amount": 1047, "item": "Oreo, Khrutka", "category": "snacks"},
    {"date": "2025-08-26", "amount": 300, "item": "ice cream", "category": "snacks"},
    
    {"date": "2025-08-27", "amount": 900, "item": "breakfast", "category": "breakfast"},
    {"date": "2025-08-27", "amount": 1650, "item": "cocoa", "category": "drinks"},
    {"date": "2025-08-27", "amount": 1034, "item": "Temu", "category": "shopping"},
    {"date": "2025-08-27", "amount": 1000, "item": "pasta", "category": "dinner"},
    
    {"date": "2025-08-28", "amount": 650, "item": "omelet", "category": "breakfast"},
    {"date": "2025-08-28", "amount": 666, "item": "laundry powder", "category": "laundry"},
    {"date": "2025-08-28", "amount": 660, "item": "laundry", "category": "laundry"},
    {"date": "2025-08-28", "amount": 540, "item": "yogurt", "category": "snacks"},
    {"date": "2025-08-28", "amount": 203, "item": "apples", "category": "fruits"},
    {"date": "2025-08-28", "amount": 1090, "item": "sandwich", "category": "lunch"},
    {"date": "2025-08-28", "amount": 450, "item": "water", "category": "water"},
    {"date": "2025-08-28", "amount": 450, "item": "nuts", "category": "snacks"},
    {"date": "2025-08-28", "amount": 300, "item": "ice cream", "category": "snacks"},
    
    {"date": "2025-08-29", "amount": 720, "item": "breakfast", "category": "breakfast"},
    {"date": "2025-08-29", "amount": 1190, "item": "chicken roll", "category": "lunch"},
    {"date": "2025-08-29", "amount": 606, "item": "cookies", "category": "snacks"},
    {"date": "2025-08-29", "amount": 200, "item": "apples", "category": "fruits"},
    
    {"date": "2025-08-30", "amount": 361, "item": "breakfast", "category": "breakfast"},
    {"date": "2025-08-30", "amount": 400, "item": "samsa", "category": "lunch"},
    {"date": "2025-08-30", "amount": 814, "item": "chips and drink", "category": "snacks"},
    {"date": "2025-08-30", "amount": 678, "item": "Oreo, milk", "category": "snacks"},
    {"date": "2025-08-30", "amount": 100, "item": "apples", "category": "fruits"},

    {"date": "2025-08-31", "amount": 655, "item": "breakfast", "category": "breakfast"},
    {"date": "2025-08-31", "amount": 1250, "item": "lunch", "category": "lunch"},
    {"date": "2025-08-31", "amount": 790, "item": "donut", "category": "snacks"},
    {"date": "2025-08-31", "amount": 3794, "item": "Temu t-shirt", "category": "shopping"},
    
    {"date": "2025-09-01", "amount": 650, "item": "breakfast", "category": "breakfast"},
    {"date": "2025-09-01", "amount": 900, "item": "lunch", "category": "lunch"},
    {"date": "2025-09-01", "amount": 172, "item": "apples", "category": "fruits"},
    {"date": "2025-09-01", "amount": 2850, "item": "cocoa and cottage cheese", "category": "dinner"},
    
    {"date": "2025-09-02", "amount": 1500, "item": "breakfast", "category": "breakfast"},
    {"date": "2025-09-02", "amount": 1700, "item": "lunch", "category": "lunch"},
    {"date": "2025-09-02", "amount": 920, "item": "milk and bun", "category": "dinner"},
    {"date": "2025-09-02", "amount": 366, "item": "apples and bananas", "category": "fruits"},
    
    {"date": "2025-09-03", "amount": 720, "item": "breakfast", "category": "breakfast"},
    {"date": "2025-09-03", "amount": 236, "item": "lemon", "category": "fruits"},
    {"date": "2025-09-03", "amount": 1180, "item": "lunch", "category": "lunch"},
    
    {"date": "2025-09-04", "amount": 1250, "item": "sandwich and mochi", "category": "breakfast"},
    {"date": "2025-09-04", "amount": 5130, "item": "blouse", "category": "shopping"},
    {"date": "2025-09-04", "amount": 667, "item": "taxi", "category": "transport"},
    {"date": "2025-09-04", "amount": 667, "item": "ECP flash drive", "category": "foreigners"},
    {"date": "2025-09-04", "amount": 900, "item": "taxi", "category": "transport"},
    {"date": "2025-09-04", "amount": 300, "item": "banana, apple", "category": "fruits"},
    {"date": "2025-09-04", "amount": 658, "item": "banana, apple", "category": "dinner"},
    {"date": "2025-09-04", "amount": 75, "item": "water", "category": "water"},

    {"date": "2025-09-05", "amount": 450, "item": "breakfast", "category": "breakfast"},
    {"date": "2025-09-05", "amount": 660, "item": "taxi", "category": "transport"},
    {"date": "2025-09-05", "amount": 966, "item": "taxi", "category": "transport"},
    {"date": "2025-09-05", "amount": 950, "item": "lentil soup and flatbread", "category": "lunch"},
    {"date": "2025-09-05", "amount": 1238, "item": "cutlet, rice, yogurt, pear", "category": "dinner"},
    
    {"date": "2025-09-06", "amount": 280, "item": "rice porridge", "category": "breakfast"},
    {"date": "2025-09-06", "amount": 891, "item": "tea", "category": "drinks"},
    {"date": "2025-09-06", "amount": 6895, "item": "Zolotoye Yabloko", "category": "shopping"},
    {"date": "2025-09-06", "amount": 1700, "item": "pilaf and salad", "category": "lunch"},
    {"date": "2025-09-06", "amount": 166, "item": "mandarins", "category": "fruits"},
    {"date": "2025-09-06", "amount": 895, "item": "onigiri", "category": "dinner"},
    {"date": "2025-09-06", "amount": 1656, "item": "Oreo", "category": "snacks"},
    
    {"date": "2025-09-07", "amount": 450, "item": "casserole", "category": "breakfast"},
    {"date": "2025-09-07", "amount": 304, "item": "bananas", "category": "fruits"},
    {"date": "2025-09-07", "amount": 1190, "item": "chicken roll", "category": "lunch"},
    {"date": "2025-09-07", "amount": 1008, "item": "Khrutka", "category": "dinner"},
    
    {"date": "2025-09-08", "amount": 450, "item": "breakfast", "category": "breakfast"},
    {"date": "2025-09-08", "amount": 891, "item": "cocoa", "category": "drinks"},
    {"date": "2025-09-08", "amount": 920, "item": "cutlet and mashed potatoes", "category": "lunch"},
    {"date": "2025-09-08", "amount": 450, "item": "yogurt", "category": "snacks"},
    {"date": "2025-09-08", "amount": 454, "item": "swimming cap", "category": "shopping"},
    
    {"date": "2025-09-09", "amount": 800, "item": "egg and omelet", "category": "breakfast"},
    {"date": "2025-09-09", "amount": 2410, "item": "peanuts, dried apricots, apples", "category": "snacks"},
    {"date": "2025-09-09", "amount": 1025, "item": "Khrutka, milk, Milky Way", "category": "lunch"},
    {"date": "2025-09-09", "amount": 490, "item": "apples", "category": "fruits"},

    {"date": "2025-09-10", "amount": 450, "item": "red bread with hole", "category": "breakfast"},
    {"date": "2025-09-10", "amount": 8386, "item": "Temu", "category": "shopping"},
    {"date": "2025-09-10", "amount": 1030, "item": "two stuffed peppers and two breads", "category": "lunch"},
    {"date": "2025-09-10", "amount": 1450, "item": "notebook and two pens", "category": "stationary"},
    {"date": "2025-09-10", "amount": 350, "item": "cabbage pie and banana", "category": "dinner"},
    
    {"date": "2025-09-11", "amount": 950, "item": "pancake with meat and two eggs", "category": "breakfast"},
    {"date": "2025-09-11", "amount": 455, "item": "yogurt", "category": "snacks"},
    {"date": "2025-09-11", "amount": 1075, "item": "three manty and vinaigrette", "category": "lunch"},
    {"date": "2025-09-11", "amount": 1333, "item": "Beeline", "category": "mobile operator"},
    {"date": "2025-09-11", "amount": 330, "item": "laundry", "category": "laundry"},
    {"date": "2025-09-11", "amount": 700, "item": "cottage cheese", "category": "dinner"},
    {"date": "2025-09-11", "amount": 376, "item": "two bananas", "category": "fruits"},
    
    {"date": "2025-09-12", "amount": 300, "item": "sandwich", "category": "breakfast"},
    {"date": "2025-09-12", "amount": 175, "item": "Barni", "category": "snacks"},
    {"date": "2025-09-12", "amount": 588, "item": "toilet paper", "category": "bazaar"},
    {"date": "2025-09-12", "amount": 288, "item": "apples", "category": "fruits"},
    {"date": "2025-09-12", "amount": 1650, "item": "rice with meat", "category": "lunch"},
    {"date": "2025-09-12", "amount": 700, "item": "Emil", "category": "dinner"},
    
    {"date": "2025-09-13", "amount": 805, "item": "semolina porridge and cheese flatbread", "category": "breakfast"},
    {"date": "2025-09-13", "amount": 700, "item": "peanuts", "category": "snacks"},
    {"date": "2025-09-13", "amount": 500, "item": "qurt", "category": "snacks"},
    {"date": "2025-09-13", "amount": 520, "item": "cheesecake", "category": "snacks"},
    {"date": "2025-09-13", "amount": 420, "item": "Greek yogurt", "category": "dinner"},
    
    {"date": "2025-09-14", "amount": 650, "item": "omelet", "category": "breakfast"},
    {"date": "2025-09-14", "amount": 1250, "item": "cutlet with mashed potatoes", "category": "lunch"},
    {"date": "2025-09-14", "amount": 300, "item": "ice cream", "category": "snacks"},
    {"date": "2025-09-14", "amount": 150, "item": "water", "category": "water"},
    {"date": "2025-09-14", "amount": 579, "item": "chocolate bar", "category": "snacks"},

    {"date": "2025-09-15", "amount": 650, "item": "omelet", "category": "breakfast"},
    {"date": "2025-09-15", "amount": 1420, "item": "cutlet, mashed potatoes and salad", "category": "lunch"},
    {"date": "2025-09-15", "amount": 490, "item": "yogurt", "category": "snacks"},
    {"date": "2025-09-15", "amount": 895, "item": "onigiri", "category": "dinner"},
    
    {"date": "2025-09-16", "amount": 560, "item": "porridge and bread with cheese", "category": "breakfast"},
    {"date": "2025-09-16", "amount": 487, "item": "apples and banana", "category": "fruits"},
    {"date": "2025-09-16", "amount": 800, "item": "two empty samsas", "category": "lunch"},
    {"date": "2025-09-16", "amount": 1195, "item": "cottage cheese and Emil", "category": "dinner"},
    
    {"date": "2025-09-17", "amount": 500, "item": "egg and bread with topping", "category": "breakfast"},
    {"date": "2025-09-17", "amount": 1090, "item": "sandwich", "category": "lunch"},
    {"date": "2025-09-17", "amount": 891, "item": "tea", "category": "drinks"},
    {"date": "2025-09-17", "amount": 300, "item": "ice cream", "category": "snacks"},
    {"date": "2025-09-17", "amount": 500, "item": "pizza", "category": "dinner"},
    {"date": "2025-09-17", "amount": 513, "item": "chips", "category": "snacks"},
    
    {"date": "2025-09-18", "amount": 650, "item": "egg and sandwich", "category": "breakfast"},
    {"date": "2025-09-18", "amount": 1700, "item": "cocoa", "category": "drinks"},
    {"date": "2025-09-18", "amount": 2900, "item": "meat with vegetables and tea with lemon", "category": "lunch"},
    {"date": "2025-09-18", "amount": 1990, "item": "Oreo bubble tea", "category": "drinks"},
    
    {"date": "2025-09-19", "amount": 780, "item": "millet porridge and casserole", "category": "breakfast"},
    {"date": "2025-09-19", "amount": 334, "item": "apples", "category": "fruits"},
    {"date": "2025-09-19", "amount": 1700, "item": "pilaf and salad", "category": "lunch"},

    {"date": "2025-09-20", "amount": 510, "item": "rice porridge and toast", "category": "breakfast"},
    {"date": "2025-09-20", "amount": 888, "item": "cutlet with rice", "category": "lunch"},
    {"date": "2025-09-20", "amount": 110, "item": "bus", "category": "transport"},
    {"date": "2025-09-20", "amount": 780, "item": "onigiri", "category": "dinner"},
    {"date": "2025-09-20", "amount": 814, "item": "cookies and chips", "category": "snacks"},
    
    {"date": "2025-09-21", "amount": 290, "item": "croissant", "category": "breakfast"},
    {"date": "2025-09-21", "amount": 146, "item": "banana", "category": "fruits"},
    {"date": "2025-09-21", "amount": 217, "item": "Big Bon", "category": "lunch"},

    {"date": "2025-09-22", "amount": 650, "item": "sandwich and egg", "category": "breakfast"},
    {"date": "2025-09-22", "amount": 300, "item": "ice cream", "category": "snacks"},
    {"date": "2025-09-22", "amount": 565, "item": "yoghurt", "category": "snacks"},
    {"date": "2025-09-22", "amount": 230, "item": "apples", "category": "fruits"},
    {"date": "2025-09-22", "amount": 450, "item": "chicken samsa", "category": "dinner"},
    {"date": "2025-09-22", "amount": 715, "item": "milk", "category": "snacks"},
    {"date": "2025-09-22", "amount": 930, "item": "khrutka", "category": "snacks"},
    {"date": "2025-09-22", "amount": 580, "item": "soap", "category": "home"},

    {"date": "2025-09-23", "amount": 650, "item": "omelet", "category": "breakfast"},
    {"date": "2025-09-23", "amount": 890, "item": "Maroccan tea", "category": "drinks"},
    {"date": "2025-09-23", "amount": 645, "item": "soup and bread", "category": "lunch"},

    {"date": "2025-09-24", "amount": 1000, "item": "2 pieces of pizza", "category": "breakfast"},
    {"date": "2025-09-24", "amount": 480, "item": "2 pies", "category": "dinner"},

    {"date": "2025-09-25", "amount": 580, "item": "porridge and bread", "category": "breakfast"},
    {"date": "2025-09-25", "amount": 1300, "item": "cheesecake", "category": "snacks"},
    {"date": "2025-09-25", "amount": 1500, "item": "teambuilding pizza", "category": "dinner"},
    {"date": "2025-09-25", "amount": 310, "item": "pizza pie", "category": "lunch"},
    {"date": "2025-09-25", "amount": 890, "item": "onigiri", "category": "dinner"},
    {"date": "2025-09-25", "amount": 780, "item": "onigiri", "category": "dinner"}
]

try:
    with open(file_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["date", "amount", "item", "category"])
        writer.writeheader() 
        writer.writerows(expenses)  

    print(f"Data saved to {file_path}")
except FileExistsError:
    print("no such file")

import pandas as pd
import matplotlib
matplotlib.use("Agg") 
import matplotlib.pyplot as plt

df = pd.read_csv("expenses_astana.csv")
print(df.head())

print("Total spent:", df["amount"].sum())
print("Daily totals:\n", df.groupby("date")["amount"].sum())
print("Average per day:", df.groupby("date")["amount"].sum().mean())
print("Most expensive day:", df.groupby("date")["amount"].sum().idxmax())
print("By category:\n", df.groupby("category")["amount"].sum().sort_values(ascending=False))

df.groupby("category")["amount"].sum().plot(kind="bar")
plt.title("Total Spending by Category")
plt.tight_layout()
plt.savefig("spending_by_category.png")

plt.clf()

df.groupby("date")["amount"].sum().plot(kind="line")
plt.title("Daily Spending Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("spending_by_date.png")



import random
from datetime import datetime, timedelta

import data.writer as wt
from com.transactions.generator.ProductLevel import ProductLevel
from com.transactions.generator.accountnumber.account_generator import generate_account_number3
from com.transactions.properties import NUMBER_OF_GENERATED_TRANSACTIONS


# Generowanie 100 obiektów
def generate_random_transactions():
    transactions = [enhanced_generate_random_transaction() for _ in range(NUMBER_OF_GENERATED_TRANSACTIONS)]
    wt.write_to_json("generated_transactions", transactions)


def generate_random_transaction():
    return {
        'transactionDate': generate_random_date(),
        'transactionHour': generate_random_time(),
        'currency': generate_random_currency(),
        'amount': generate_random_amount(),
        'transactionType': generate_random_transaction_type(),
        'title': generate_random_title()
    }


def enhanced_generate_random_transaction():
    title = enhanced_generate_random_title()
    date = generate_random_date()
    time = enhanced_generate_random_time(title)
    account_number = generate_account_number3(title)
    currency = enhanced_generate_random_currency(title)
    amount = enhanced_generate_random_amount(title)
    transaction_type = enhanced_generate_random_transaction_type(title)

    return {
        'account_number': account_number,
        'transactionDate': date,
        'transactionHour': time,
        'currency': currency,
        'amount': amount,
        'transactionType': transaction_type,
        'title': title
    }


def generate_random_date():
    start_date = datetime(2010, 1, 1)
    end_date = datetime(2023, 12, 31)
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    return random_date.strftime('%Y-%m-%d')


def enhanced_generate_random_time(title):
    if 'Standard' in title:
        return f"{random.randint(0, 10):02d}:{random.randint(0, 59):02d}"
    elif 'Pro' in title:
        return f"{random.randint(10, 20):02d}:{random.randint(0, 59):02d}"
    else:
        return f"{random.randint(20, 23):02d}:{random.randint(0, 59):02d}"


def generate_random_time():
    return f"{random.randint(0, 23):02d}:{random.randint(0, 59):02d}"


def generate_random_currency():
    currencies = ['PLN', 'USD', 'GBP', 'EUR']
    return random.choice(currencies)


def enhanced_generate_random_currency(title):
    standard_currencies = ['RUB', 'HUF', 'PLN', 'USD', 'GBP', 'EUR']
    pro_currencies = ['PLN', 'USD', 'GBP', 'EUR']
    ultra_currencies = ['USD', 'GBP', 'EUR']

    if 'Standard' in title:
        return random.choice(standard_currencies)
    elif 'Pro' in title:
        return random.choice(pro_currencies)
    else:
        return random.choice(ultra_currencies)


def generate_random_amount():
    return round(random.uniform(0.00, 100000.00), 2)


def enhanced_generate_random_amount(title):
    if 'Standard' in title:
        return round(random.uniform(10.00, 1_000.00), 2)
    elif 'Pro' in title:
        return round(random.uniform(500, 10_000.00), 2)
    else:
        return round(random.uniform(5000.00, 50_000.00), 2)


def generate_random_transaction_type():
    return random.randint(0, 999)


def enhanced_generate_random_transaction_type(title):
    accessories_dict_keys = accessories_dict.keys()
    accessories_names = list(accessories_dict_keys)
    for name in accessories_names:
        if name in title:
            return accessories_dict[name]

    raise Exception(f"For title {title} no accessory has been found among available: {accessories_dict_keys}!")


def generate_random_title():
    return f"{random.choice(accessories)} {random.choice(ProductLevel.levels())}"


def enhanced_generate_random_title():
    accessory_name = random.choice(list(accessories_dict.keys()))
    title = f"{accessory_name} {random.choice(ProductLevel.levels())}"
    return title


accessories = [
    "Keyboard", "Mouse", "Monitor", "Headphones", "Speakers", "Webcam", "USB Hub", "Laptop Stand", "Desk Organizer",
    "Wireless Charger", "External Hard Drive", "Graphics Tablet", "Ergonomic Chair", "Desk Lamp",
    "Cable Management Box",
    "Multi-port Adapter", "Gaming Mouse Pad", "Laptop Cooling Pad", "Blue Light Blocking Glasses", "Printer"
]

accessories_dict = {
    "Keyboard": 1,
    "Mouse": 2,
    "Monitor": 3,
    "Headphones": 4,
    "Speakers": 5,
    "Webcam": 6,
    "USB Hub": 7,
    "Laptop Stand": 8,
    "Desk Organizer": 9,
    "Wireless Charger": 10,
    "External Hard Drive": 11,
    "Graphics Tablet": 12,
    "Ergonomic Chair": 13,
    "Desk Lamp": 14,
    "Cable Management Box": 15,
    "Multi-port Adapter": 16,
    "Gaming Mouse Pad": 17,
    "Laptop Cooling Pad": 18,
    "Blue Light Blocking Glasses": 19,
    "Printer": 20,
    "Scanner": 21,
    "Microphone": 22,
    "External SSD": 23,
    "Docking Station": 24,
    "Laptop Sleeve": 25,
    "Laptop Backpack": 26,
    "Desk Mat": 27,
    "Surge Protector": 28,
    "Adjustable Desk": 29,
    "Computer Glasses": 30,
    "Noise-Canceling Headset": 31,
    "Computer Stand": 32,
    "Gaming Controller": 33,
    "Smart Speaker": 34,
    "Wi-Fi Range Extender": 35,
    "Monitor Stand": 36,
    "Mechanical Keyboard": 37,
    "Mousepad with Wireless Charger": 38,
    "Portable Laptop Charger": 39,
    "Webcam Cover": 40
}

# import pandas as pd
# from sklearn.cluster import KMeans
# from sklearn.preprocessing import StandardScaler
# import matplotlib.pyplot as plt
#
# # Przygotowanie danych (w tym przypadku, przyjmujemy, że dane znajdują się w pliku CSV)
# df = pd.read_csv('dane_transakcyjne.csv')
#
# # Czyszczenie danych i ekstrakcja cech
# # Tutaj trzeba dostosować do konkretnych cech w Twoich danych
# features = df[['Amount', 'Frequency', 'AvgTransactionAmount']]
#
# # Standaryzacja danych
# scaler = StandardScaler()
# features_scaled = scaler.fit_transform(features)
#
# # Wybór liczby klastrów (grup)
# num_clusters = 3
#
# # Utworzenie i trenowanie modelu k-means
# kmeans_model = KMeans(n_clusters=num_clusters, random_state=42)
# df['Cluster'] = kmeans_model.fit_predict(features_scaled)
#
# # Eksploracja wyników
# # Wizualizacja klastrów
# plt.scatter(df['Frequency'], df['Amount'], c=df['Cluster'], cmap='viridis')
# plt.xlabel('Frequency')
# plt.ylabel('Amount')
# plt.title('K-means Clustering of Customers')
# plt.show()
#
# # Analiza klastrów
# cluster_means = df.groupby('Cluster').mean()
# print(cluster_means)
#
# # Implementacja modelu w systemie i rekomendacje produktów
# # Tutaj zaimplementuj kod, który będzie używał klastrów do personalizowanych rekomendacji produktów
# # Na przykład, oferuj produkty najczęściej kupowane przez klientów w danym klastrze
#
# # Zapisanie modelu do późniejszego użycia
# # W prawdziwym środowisku warto byłoby zastosować bardziej zaawansowane podejścia
# import joblib
# joblib.dump(kmeans_model, 'model_kmeans.pkl')

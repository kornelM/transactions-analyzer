# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

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

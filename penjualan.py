import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data_praktikum_analisis_data - data_praktikum_analisis_data.csv')
df.head()

df.info()
df.isnull().sum()

df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df = df.dropna(subset=['Total_Sales'])  # Hapus baris dengan Total_Sales kosong
df = df[df['Price_Per_Unit'] > 0]       # Pastikan harga positif
df['Month'] = df['Order_Date'].dt.to_period('M').astype(str)
monthly_sales = df.groupby('Month')['Total_Sales'].sum()

plt.figure(figsize=(10,5))
plt.plot(monthly_sales.index, monthly_sales.values, marker='o')
plt.title('Tren Penjualan Bulanan')
plt.xticks(rotation=45)
plt.show()
corr = df[['Ad_Budget', 'Quantity', 'Price_Per_Unit', 'Total_Sales']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Korelasi Antar Variabel')
plt.show()
plt.scatter(df['Quantity'], df['Total_Sales'])
plt.xlabel('Jumlah Terjual (Quantity)')
plt.ylabel('Total Penjualan')
plt.title('Scatter Plot: Quantity vs Total Sales')
plt.show()
snapshot_date = df['Order_Date'].max() + pd.Timedelta(days=1)
rfm = df.groupby('CustomerID').agg({
    'Order_Date': lambda x: (snapshot_date - x.max()).days,
    'Order_ID': 'count',
    'Total_Sales': 'sum'
})
rfm.columns = ['Recency', 'Frequency', 'Monetary']

# Skor 1-5
rfm['R_Score'] = pd.qcut(rfm['Recency'], 5, labels=[5,4,3,2,1])
rfm['F_Score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 5, labels=[1,2,3,4,5])
rfm['M_Score'] = pd.qcut(rfm['Monetary'], 5, labels=[1,2,3,4,5])

rfm['RFM_Segment'] = rfm['R_Score'].astype(str) + rfm['F_Score'].astype(str) + rfm['M_Score'].astype(str)
rfm.head()
profit_margin = df.groupby('Product_Category')['Total_Sales'].mean().sort_values()
profit_margin.plot(kind='barh', color='salmon')
plt.title('Rata-rata Total Penjualan per Kategori (Proxy Profit)')
plt.show()
avg_price = df.groupby('Product_Category')['Price_Per_Unit'].transform('mean')
df['Discount_Flag'] = (df['Price_Per_Unit'] < 0.8 * avg_price).astype(int)

discount_effect = df.groupby('Discount_Flag')['Quantity'].mean()
print(discount_effect)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data_praktikum_analisis_data - data_praktikum_analisis_data.csv')
df.head()

df.info()
df.isnull().sum()

df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df = df.dropna(subset=['Total_Sales'])  # Hapus baris dengan Total_Sales kosong
df = df[df['Price_Per_Unit'] > 0]       # Pastikan harga positif
df['Month'] = df['Order_Date'].dt.to_period('M').astype(str)
monthly_sales = df.groupby('Month')['Total_Sales'].sum()

plt.figure(figsize=(10,5))
plt.plot(monthly_sales.index, monthly_sales.values, marker='o')
plt.title('Tren Penjualan Bulanan')
plt.xticks(rotation=45)
plt.show()
corr = df[['Ad_Budget', 'Quantity', 'Price_Per_Unit', 'Total_Sales']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Korelasi Antar Variabel')
plt.show()
plt.scatter(df['Quantity'], df['Total_Sales'])
plt.xlabel('Jumlah Terjual (Quantity)')
plt.ylabel('Total Penjualan')
plt.title('Scatter Plot: Quantity vs Total Sales')
plt.show()
snapshot_date = df['Order_Date'].max() + pd.Timedelta(days=1)
rfm = df.groupby('CustomerID').agg({
    'Order_Date': lambda x: (snapshot_date - x.max()).days,
    'Order_ID': 'count',
    'Total_Sales': 'sum'
})
rfm.columns = ['Recency', 'Frequency', 'Monetary']

# Skor 1-5
rfm['R_Score'] = pd.qcut(rfm['Recency'], 5, labels=[5,4,3,2,1])
rfm['F_Score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 5, labels=[1,2,3,4,5])
rfm['M_Score'] = pd.qcut(rfm['Monetary'], 5, labels=[1,2,3,4,5])

rfm['RFM_Segment'] = rfm['R_Score'].astype(str) + rfm['F_Score'].astype(str) + rfm['M_Score'].astype(str)
rfm.head()
profit_margin = df.groupby('Product_Category')['Total_Sales'].mean().sort_values()
profit_margin.plot(kind='barh', color='salmon')
plt.title('Rata-rata Total Penjualan per Kategori (Proxy Profit)')
plt.show()
avg_price = df.groupby('Product_Category')['Price_Per_Unit'].transform('mean')
df['Discount_Flag'] = (df['Price_Per_Unit'] < 0.8 * avg_price).astype(int)

discount_effect = df.groupby('Discount_Flag')['Quantity'].mean()
print(discount_effect)
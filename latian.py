import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#dataset
data = pd.read_csv('nilai_siswa.csv')
# Display first few rows of the dataset
print(data.info())
print(data.head())
print(data.describe())

#print("Rata-rata:", data['Nilai].mean)
#print("Median:", data['Nilai].median)
#print("Modus:", data['Nilai].mode()[0])

matematika = data[data['Matpel'] == 'Matematika']
print(matematika)
Inggris = data[data['Matpel'] == 'Inggris']
print(Inggris)
Indonesia = data[data['Matpel'] == 'Indonesia']
print(Indonesia)
Produktif = data[data['Matpel'] == 'Produktif']
print(Produktif)

data.groupby('Matpel')['Nilai'].agg(['max,min'])

rata = data.groupby('Matpel')['Nilai'].mean()
rata.plot(kind='bar')
plt.title('Rata-rata Nilai Siswa per Mata Pelajaran')
plt.xlabel('Mata Pelajaran')
plt.ylabel('Rata-rata Nilai')
plt.show()

sns.boxplot(x='Matpel', y='Nilai', data=data)
plt.title('Distribusi Nilai Siswa per Mata Pelajaran')
plt.show()



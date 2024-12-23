import pandas as pd
df = pd.read_csv("Clickjacking.csv")
print(df.head())

print('The shape of the dataset is \n',df.shape)
print(df.isna().sum())
print(df.columns)


# Calculate correlation between column ‘A’ and ‘B’
correlation_ts = df['Clickjacking'].corr(df['Time Spent'])
correlation_ps = df['Clickjacking'].corr(df['Password Security'])
correlation_es = df['Clickjacking'].corr(df['Enable Security'])
correlation_sl = df['Clickjacking'].corr(df['Sharing Location'])
correlation_au = df['Clickjacking'].corr(df['Accept Unknown'])
correlation_nof = df['Clickjacking'].corr(df['Number of Friends'])
correlation_nog = df['Clickjacking'].corr(df['Number of Groups'])
correlation_coul = df['Clickjacking'].corr(df['Click on Unknown Link'])

print("\nThe correlation between Clickjacking and Time Spent is",correlation_ts)
print("\nThe correlation between Clickjacking and Password Security is",correlation_ps)
print("\nThe correlation between Clickjacking and Enable Security is",correlation_es)
print("\nThe correlation between Clickjacking and Sharing Location is",correlation_sl)
print("\nThe correlation between Clickjacking and Accept Unknown is",correlation_au)
print("\nThe correlation between Clickjacking and Number of Friends is",correlation_nof)
print("\nThe correlation between Clickjacking and Number of Groups is",correlation_nog)
print("\nThe correlation between Clickjacking and Click on Unknown Link is",correlation_coul)




import matplotlib.pyplot as plt
import numpy as np
y= df['Clickjacking']
t_s= df['Time Spent']
p_s = df['Password Security']
e_s=df['Enable Security']
s_l= df['Sharing Location']
a_u=df['Accept Unknown']
n_f=df['Number of Friends']
n_g=df['Number of Groups']
c_l=df['Click on Unknown Link']




# plotting the data
plt.suptitle('Correlation between Cyber Threat Clickjacking and independent variables')
# adds the title
plt.title('Correlation')
plt.subplot(3,2,1)

# plot the data
plt.scatter(t_s, y)
# fits the best fitting line to the data
plt.plot(np.unique(t_s),
		np.poly1d(np.polyfit(t_s, y, 1))
		(np.unique(t_s)), color='red')
# Labelling axes
plt.xlabel('Time Spent')
plt.ylabel('Clickjacking')



plt.subplot(3,2,2)
# plot the data
plt.scatter(p_s, y)
# fits the best fitting line to the data
plt.plot(np.unique(p_s),
		np.poly1d(np.polyfit(p_s, y, 1))
		(np.unique(p_s)), color='red')
# Labelling axes
plt.xlabel('Password Security')
plt.ylabel('Clickjacking')



plt.subplot(3,2,3)
# plot the data
plt.scatter(e_s, y)
# fits the best fitting line to the data
plt.plot(np.unique(e_s),
		np.poly1d(np.polyfit(e_s, y, 1))
		(np.unique(e_s)), color='red')
# Labelling axes
plt.xlabel('Enable Security')
plt.ylabel('Clickjacking')



plt.subplot(3,2,4)
# plot the data
plt.scatter(s_l, y)
# fits the best fitting line to the data
plt.plot(np.unique(s_l),
		np.poly1d(np.polyfit(s_l, y, 1))
		(np.unique(s_l)), color='red')
# Labelling axes
plt.xlabel('Sharing Location')
plt.ylabel('Clickjacking')


plt.subplot(3,2,5)
# plot the data
plt.scatter(a_u, y)
# fits the best fitting line to the data
plt.plot(np.unique(a_u),
		np.poly1d(np.polyfit(a_u, y, 1))
		(np.unique(a_u)), color='red')
# Labelling axes
plt.xlabel('Accept Unknown')
plt.ylabel('Clickjacking')




plt.subplot(3,2,6)
# plot the data
plt.scatter(c_l, y)
# fits the best fitting line to the data
plt.plot(np.unique(c_l),
		np.poly1d(np.polyfit(c_l, y, 1))
		(np.unique(c_l)), color='red')
# Labelling axes
plt.xlabel('Click on Unknown Link')
plt.ylabel('Clickjacking')




plt.show()










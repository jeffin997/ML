import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_excel('Price History.xlsx',index_col=None,na_values=['NA'],usecols="C,E")
df=pd.DataFrame(data)
#print(df)
#x=np.array(df['OPEN']).reshape(-1,1)
y=np.array(df['HIGH']).reshape(-1,1)
z=np.array(df['CLOSE']).reshape(-1,1)
df.dropna(inplace=True)
#print(y)
plt.plot(y,z)
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

leitos_df = pd.read_csv('leitos.csv')
senhas_df = pd.read_csv('senhas.csv')

leitos_df['data'] = pd.to_datetime(leitos_df['data'])
senhas_df['data'] = pd.to_datetime(senhas_df['data'])

leitos_mensal = leitos_df.resample('M', on='data').mean().round().astype(int)
senhas_mensal = senhas_df.resample('M', on='data').mean().round().astype(int)

leitos_mensal = leitos_mensal.loc['2024-01-01':'2024-06-30']
senhas_mensal = senhas_mensal.loc['2024-01-01':'2024-06-30']

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(10, 10))
fig.subplots_adjust(
    left=0.075,
    bottom=0.058,
    right=0.985,
    top=0.962,
    wspace=0.2,
    hspace=0.255
)

ax1.plot(leitos_mensal.index, leitos_mensal['ocupacao_leitos'], marker='o', linestyle='-', color='tab:blue')
ax1.set_xlabel('Mês')
ax1.set_ylabel('Média de Leitos')
ax1.set_title('Média Mensal de Leitos (Jan-Jun 2024)')
ax1.grid(True)

ax2.plot(senhas_mensal.index, senhas_mensal['quantidade_senhas'], marker='o', linestyle='-', color='tab:red')
ax2.set_xlabel('Mês')
ax2.set_ylabel('Média de Senhas')
ax2.set_title('Média Mensal de Senhas (Jan-Jun 2024)')
ax2.grid(True)

plt.tight_layout()
plt.show()

# Total market capitalisation
df['MC_sum'] = df[MARKET_CAP].sum()
# Percentage of total market capitalisation of each company
df['MC_percentage'] = (df['Market Capitalisation'] / df['MC_sum']) * 100
# Sort companies by market capitalisation
df = df.sort_values(by=['Market Capitalisation'], ascending=False)
# Cumulate the percentages for the MSCI indices
df['MC_percentage_cum'] = df['MC_percentage'].cumsum()

# Fixed size index (30 components)
figure_data_fix_number = df.head(30)
# Large cap index
figure_data_large_cap = df[df['MC_percentage_cum'] <= 0.75]
# Standard index§
figure_data_standard = df[df['MC_percentage_cum'] <= 0.90]
# Investable market index (IMI)
figure_data_imi = df[df['MC_percentage_cum'] <= 0.99]

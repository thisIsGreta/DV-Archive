import matplotlib.pyplot as plt

# -------------------------Two different axes on one line chart--------------------------- #
plt.figure(figsize=(14, 8), dpi=120)
plt.title('Tesla Web Search vs Price', fontsize=18)
plt.xticks(fontsize=14, rotation=45)

ax1 = plt.gca() # get current axis
ax2 = ax1.twinx()


ax1.grid(color='gray', linestyle='-')


ax1.set_ylabel('TSLA Stock Price', color='#E6232E', fontsize=14)  # can use a HEX code
ax2.set_ylabel('Search Trend', color='skyblue', fontsize=14)      # or a named colour

 
ax1.plot(df_tesla['MONTH'], df_tesla['TSLA_USD_CLOSE'], color='#E6232E', linewidth=3, linestyle='dashed')
ax2.plot(df_tesla['MONTH'], df_tesla['TSLA_WEB_SEARCH'], color='skyblue', linewidth=3)


ax1.set_ylim([0, 600])
ax1.set_xlim([df_tesla.MONTH.min(), df_tesla.MONTH.max()])


# --------------------------How to add tick formatting for dates on the x-axis. ---------------------------- #
ax1.xaxis.set_major_locator(years)
ax1.xaxis.set_major_formatter(years_fmt)
ax1.xaxis.set_minor_locator(months)

plt.show()

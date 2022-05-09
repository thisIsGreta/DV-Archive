import matplotlib.pyplot as plt
import seaborn as sns


# --------------------- Bubble Charts -------------------------- #
plt.figure(figsize=(8,4), dpi=200)
 
ax = sns.scatterplot(data=data_clean,
                     x='USD_Production_Budget', 
                     y='USD_Worldwide_Gross',
                     hue='USD_Worldwide_Gross',     # colour
                     size='USD_Worldwide_Gross',)   # dot size
 
ax.set(ylim=(0, 3000000000),
       xlim=(0, 450000000),
       ylabel='Revenue in $ billions',
       xlabel='Budget in $100 millions')
 
plt.show()



# ------------------------------ regplot: scatter plot and linear regression line  散点回归图---------------------------------- #
plt.figure(figsize=(8,4), dpi=200)

with sns.axes_style("whitegrid"):
  sns.regplot(data=old_films, 
            x='USD_Production_Budget', 
            y='USD_Worldwide_Gross',
            lowess = True,                # Set the lowess parameter to True to show a moving average of the linear fit.
            scatter_kws = {'alpha': 0.4},
            line_kws = {'color': 'black'})
  
  ax.set(ylim=(0, new_films['USD_Worldwide_Gross'].max()),
         xlim=(0, new_films['USD_Production_Budget'].max()),
         ylabel='USD_Worldwide_Gross',
         xlabel='USD_Production_Budget')
  
  
  
# ----------------------------- kdeplot 千里江山图 ------------------------------- #
plt.figure(dpi=200)

sns.kdeplot(before_washing.pct_deaths, 
            shade=True, 
            clip=(0,1)) #类似set limit

sns.kdeplot(after_washing.pct_deaths, 
            shade=True, 
            clip=(0,1))

plt.title('Est. Distribution of Monthly Death Rate Before and After Handwashing')
plt.xlim(0, 0.40)

plt.show()


  
# --------------------- box plot 箱型图 -------------------------- #
plt.figure(figsize=(8,4), dpi=200)

with sns.axes_style("whitegrid"):
    sns.boxplot(data=df_data,
                x='category',
                y='winning_age')
 
plt.show()




# ---------------------------------- lmplot 回归图 ---------------------------------------------- #
with sns.axes_style('whitegrid'):
    sns.lmplot(data=df_data,
               x='year', 
               y='winning_age',
               hue='category',     # put all categories on the same chart using the hue parameter
               lowess=True, 
               aspect=2,
               scatter_kws = {'alpha': 0.6},
               )
 
plt.show()


# ---------------------------------- displot 直方趋势图 ---------------------------------------------- #
sns.displot(data['PRICE'], 
            bins=50, 
            aspect=2,
            hist=True,   #是否有直方图
            kde=True,    #是否有趋势图
            color='#2196f3')

plt.title(f'1970s Home Values in Boston. Average: ${(1000*data.PRICE.mean()):.6}')
plt.xlabel('Price in 000s')
plt.ylabel('Nr. of Homes')

plt.show()

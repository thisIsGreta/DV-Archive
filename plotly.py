import plotly.express as px

# ----------------------------- Histogram 直方图 📊----------------------------#
hist = px.histogram(df_monthly, 
                   x='pct_deaths', 
                   color='washing_hands',
                   nbins=30,
                   opacity=0.6,
                   barmode='overlay',
                   histnorm='percent',
                   marginal='box',  # 在图上方又做一个box chart
                   )
 
hist.update_layout(xaxis_title='Proportion of Monthly Deaths',
                   yaxis_title='Count',)
 
hist.show()



# ----------------------------- Box Chart 箱型图-----------------------------#
box = px.box(df_monthly, 
             x='washing_hands', 
             y='pct_deaths',
             color='washing_hands', #像labels
             title='How Have the Stats Changed with Handwashing?')
 
box.update_layout(xaxis_title='Washing Hands?',
                  yaxis_title='Percentage of Monthly Deaths',)
 
box.show()



# ----------------------------- Bar Chart 柱状图-----------------------------#
bar = px.bar(x = category_installs.Installs,
               y = category_installs.index,
               orientation='h',
               color = prizes_per_category.values,
               color_continuous_scale='Aggrnyl',
               title='Category Popularity')

bar.update_layout(xaxis_title='Number of Downloads', 
                    coloraxis_showscale=False,
                    yaxis_title='Category')

bar.show()



# -----------------------------Pie Chart 饼图-------------------------------#
fig = px.pie(labels=ratings.index,
             values=ratings.values,
             title="Content Rating",
             names=ratings.index,
             )

fig.update_traces(textposition='outside', textinfo='percent+label')
 
fig.show()



# -----------------------------Donut Chart 甜甜圈图-------------------------#
fig = px.pie(labels=ratings.index,
             values=ratings.values,
             title="Content Rating",
             names=ratings.index,
             hole = 0.6
             )
fig.update_traces(textposition='inside', textinfo='percent')
 
fig.show()


import matplotlib.pyplot as pt
# Data to plot
programming_languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popuratity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
# explode 1st slice
explode = (0.1, 0, 0, 0,0,0)
# Plot
wedgep={'linewidth':1,'edgecolor':'black'}
pt.pie(popuratity, explode=explode, labels=programming_languages, colors=colors,
autopct='%1.1f%%', shadow=True, wedgeprops= wedgep,startangle=140)

pt.show()
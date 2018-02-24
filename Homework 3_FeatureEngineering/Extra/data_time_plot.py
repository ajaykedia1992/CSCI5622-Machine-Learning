from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib import dates, pyplot

x2 = ['Jan 01', 'Jan 02', 'Jan 03', 'Jan 04', 'Jan 05', 'Jan 06', 'Jan 07', 'Jan 08', 'Jan 09', 'Jan 10', 'Jan 11', 'Jan 12', 'Jan 13', 'Jan 14', 'Jan 15', 'Jan 16', 'Jan 17', 'Jan 18', 'Jan 19', 'Jan 20', 'Jan 21', 'Jan 22', 'Jan 23', 'Jan 24', 'Jan 25', 'Jan 26', 'Jan 27', 'Jan 28', 'Jan 29', 'Jan 30', 'Jan 31', 'Feb 01', 'Feb 02', 'Feb 03', 'Feb 04', 'Feb 05', 'Feb 06', 'Feb 07', 'Feb 08', 'Feb 09', 'Feb 10', 'Feb 11', 'Feb 12', 'Feb 13', 'Feb 14', 'Feb 15', 'Feb 16', 'Feb 17', 'Feb 18', 'Feb 19', 'Feb 20', 'Feb 21', 'Feb 22', 'Feb 23', 'Feb 24', 'Feb 25', 'Feb 26', 'Feb 27', 'Feb 28', 'Mar 01', 'Mar 02', 'Mar 03', 'Mar 04', 'Mar 05', 'Mar 06', 'Mar 07', 'Mar 08', 'Mar 09', 'Mar 10', 'Mar 11', 'Mar 12', 'Mar 13', 'Mar 14', 'Mar 15', 'Mar 16', 'Mar 17', 'Mar 18', 'Mar 19', 'Mar 20', 'Mar 21', 'Mar 22', 'Mar 23', 'Mar 24', 'Mar 25', 'Mar 26', 'Mar 27', 'Mar 28', 'Mar 29', 'Mar 30']
y2 = [80.5, 81.5, 78.0, 69.5, 72.0, 75.0, 81.0, 81.0, 79.5, 77.5, 78.5, 78.0, 77.5, 78.0, 79.0, 74.5, 74.0, 72.5, 72.0, 73.0, 76.0, 74.0, 75.0, 78.0, 75.0, 70.0, 71.5, 75.0, 77.5, 68.5, 71.0, 77.0, 80.5, 76.5, 74.5, 74.0, 76.5, 78.0, 79.0, 74.5, 75.0, 70.0, 67.0, 70.5, 74.0, 72.0, 73.0, 77.0, 74.0, 72.0, 72.0, 72.0, 76.0, 79.5, 80.0, 74.0, 70.5, 72.5, 81.5, 81.5, 84.5, 79.0, 78.0, 79.5, 79.0, 73.0, 70.0, 68.0, 71.5, 76.0, 70.0, 63.5, 62.0, 63.0, 64.0, 64.0, 66.5, 60.0, 66.0, 71.0, 63.0, 61.5, 64.5, 60.5, 67.5, 71.5, 74.0, 73.0, 66.5]

x1 = ['Jul 01', 'Jul 02', 'Jul 03', 'Jul 04', 'Jul 05', 'Jul 06', 'Jul 07', 'Jul 08', 'Jul 09', 'Jul 10', 'Jul 11', 'Jul 12', 'Jul 13', 'Jul 14', 'Jul 15', 'Jul 16', 'Jul 17', 'Jul 18', 'Jul 19', 'Jul 20', 'Jul 21', 'Jul 22', 'Jul 23', 'Jul 24', 'Jul 25', 'Jul 26', 'Jul 27', 'Jul 28', 'Jul 29', 'Jul 30', 'Jul 31', 'Aug 01', 'Aug 02', 'Aug 03', 'Aug 04', 'Aug 05', 'Aug 06', 'Aug 07', 'Aug 08', 'Aug 09', 'Aug 10', 'Aug 11', 'Aug 12', 'Aug 13', 'Aug 14', 'Aug 15', 'Aug 16', 'Aug 17', 'Aug 18', 'Aug 19', 'Aug 20', 'Aug 21', 'Aug 22', 'Aug 23', 'Aug 24', 'Aug 25', 'Aug 26', 'Aug 27', 'Aug 28', 'Aug 29', 'Aug 30', 'Aug 31', 'Sep 01', 'Sep 02', 'Sep 03', 'Sep 04', 'Sep 05', 'Sep 06', 'Sep 07', 'Sep 08', 'Sep 09', 'Sep 10', 'Sep 11', 'Sep 12', 'Sep 13', 'Sep 14', 'Sep 15', 'Sep 16', 'Sep 17', 'Sep 18', 'Sep 19', 'Sep 20', 'Sep 21', 'Sep 22', 'Sep 23', 'Sep 24', 'Sep 25', 'Sep 26', 'Sep 27', 'Sep 28', 'Sep 29', 'Sep 30']
y1 = [80.5, 81.5, 78.0, 69.5, 72.0, 75.0, 81.0, 81.0, 79.5, 77.5, 78.5, 78.0, 77.5, 78.0, 79.0, 74.5, 74.0, 72.5, 72.0, 73.0, 76.0, 78.5, 80.0, 75.0, 74.0, 75.0, 78.0, 75.0, 70.0, 71.5, 75.0, 77.5, 68.5, 71.0, 77.0, 80.5, 76.5, 74.5, 74.0, 76.5, 78.0, 79.0, 74.5, 75.0, 70.0, 67.0, 70.5, 74.0, 72.0, 73.0, 77.0, 74.0, 72.0, 72.0, 72.0, 76.0, 79.5, 80.0, 74.0, 70.5, 72.5, 81.5, 81.5, 84.5, 79.0, 78.0, 79.5, 79.0, 73.0, 70.0, 68.0, 71.5, 76.0, 70.0, 63.5, 62.0, 63.0, 64.0, 64.0, 66.5, 60.0, 66.0, 71.0, 63.0, 61.5, 64.5, 60.5, 67.5, 71.5, 74.0, 73.0, 66.5]

ax = pyplot.gca()
hfmt = dates.DateFormatter('%b')
ax.xaxis.set_major_formatter(hfmt)
ax.xaxis.set_major_locator(dates.MonthLocator())

for x, y in [(x1, y1), (x2, y2)]:
    dt_x = dates.date2num([datetime.strptime(d, "%b %d").replace(year=2017) for d in x])
    plt.plot(dt_x, y)

plt.show()
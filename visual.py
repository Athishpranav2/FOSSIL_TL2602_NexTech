import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt

def plot_data(ax, df, column='Value', x_label='Time', y_label='Energy (kWh)', title=None):
    if column is None:
        ax.plot(df)
    else:
        ax.plot(df[column])
    ax.xaxis.set_tick_params(rotation=45)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    ax.grid()

def calculate_daily_consumption(df, column='Value'):
    return df.groupby([df.index.date])[column].sum()

def plot_daily_consumption(ax, df, x_label='Day', y_label='Energy (kWh)', title='Total daily consumption'):
    ax.plot(df)
    ax.xaxis.set_tick_params(rotation=45)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    ax.grid()

def calculate_mean_profile(df, column='Value'):
    mean_profile = df.groupby([df.index.time])[column].mean()
    mean_profile.index = mean_profile.index.map(lambda t: dt.datetime.combine(dt.datetime(year=1970, month=1, day=1), t))
    return mean_profile

def plot_mean_profile(ax, mean_profile, x_label='Hour', y_label='Energy (kWh)', title='Mean consumption profile'):
    ax.plot(mean_profile)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H'))
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    ax.grid()




fig, ax = plt.subplots(2, 2, figsize=(15, 10))
fig.subplots_adjust(hspace=0.35)


plot_data(ax[0, 0], df_smd)
ax[0, 0].set_title('Full timeseries')


plot_daily_consumption(ax[0, 1], calculate_daily_consumption(df_smd))


plot_data(ax[1, 0], df_smd.iloc[:96 * 7, :], x_label='Time', title='Single week of timeseries')
ax[1, 0].xaxis.set_major_formatter(mdates.DateFormatter("%a %d.%b."))
ax[1, 0].xaxis.set_major_locator(mdates.AutoDateLocator())

plot_mean_profile(ax[1, 1], calculate_mean_profile(df_smd)




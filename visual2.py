import matplotlib.pyplot as plt

def plot_stacked_daily_consumption(df, appliance_columns, labels, figsize=(10, 5), xlabel='Day', ylabel='Energy (kWh)', title='Total daily consumption'):
    fig, ax = plt.subplots(1, 1, figsize=figsize)

    # calculate the daily demand for each appliance
    daily_appliance = df.groupby([df.index.date])[appliance_columns].sum()

    # create the stacked plot
    ax.stackplot(daily_appliance.index, daily_appliance.T, labels=labels)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.legend()

    plt.show()

# Example usage:
# Assuming df_smd is your DataFrame
appliance_columns = ['Value_OtherAppliances', 'Value_HeatPump']
labels = ['Other appliances', 'Heat pump']

plot_stacked_daily_consumption(df_smd, appliance_columns, labels)

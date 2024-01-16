import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def plt_save(path='rfid/save/path/x.csv'):
    # save_name = path.split('/')[-1].split('.')[0]
    # print(save_name)
    df = pd.read_csv(path, usecols=['EPC', 'PhaseAngle(Radian)'])
    column_name = 'PhaseAngle(Radian)'
    grouped_means = df.groupby('EPC')[column_name].transform('mean')
    for i in range(len(df)):
        current_value = df.at[i, column_name]
        group_mean = grouped_means[i]
        threshold = group_mean + 2
        if abs(current_value) > threshold:
            df.at[i, column_name] = group_mean
    df.groupby('EPC')['PhaseAngle(Radian)'].plot(legend=False)
    plt.axis('off')
    plt.show()
    # plt.savefig('vis/rfid/' + save_name + '.jpg', format='jpeg', dpi=300, bbox_inches='tight')
    plt.close()


plt_save()


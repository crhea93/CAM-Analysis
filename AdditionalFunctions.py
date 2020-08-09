import numpy as np

def valenceCalc(dataframe):
    valence_avg = 0
    if len(dataframe['shape']) > 0:  # If there are any concepts!!
        for valence in dataframe['shape']:
            if valence == 'neutral':
                valence_avg += 0
            elif 'positive' in valence:
                if 'weak' in valence:
                    valence_avg += 1
                elif valence == 'positive':
                    valence_avg += 2
                elif 'strong' in valence:
                    valence_avg += 3
            elif 'negative' in valence:
                if 'weak' in valence:
                    valence_avg -= 1
                elif valence == 'negative':
                    valence_avg -= 2
                elif 'strong' in valence:
                    valence_avg -= 3
        return np.round(valence_avg/len(dataframe['shape']),2)
    else:
        return 0
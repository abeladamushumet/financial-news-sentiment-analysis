import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_clean_data():
    # Example: adjust this path to match your CSV file location
    df = pd.read_csv(r'C:\Users\hp\Desktop\10 Acadamy\VS code\solar-challenge-week1\data\benin_clean.csv')
# or the actual filename
    return df

def generate_summary_table(df):
    return df.describe()

def plot_boxplots(data, selected_metric):
    import seaborn as sns
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 6))
    sns.boxplot(data=data.select_dtypes(include='number'))
    plt.title(f'Boxplots for {selected_metric}')
    plt.tight_layout()

    return plt.gcf()  # or plt.show() if you're displaying


def plot_avg_ghi_bar(df):
    import matplotlib.pyplot as plt
    df['date'] = pd.to_datetime(df['timestamp']).dt.date
    avg_ghi = df.groupby('date')['ghi'].mean()
    avg_ghi.plot(kind='bar')
    plt.title("Average GHI by Day")
    plt.ylabel("GHI")
    plt.show()


import pandas as pd


def main():
    df = pd.read_csv("./data/winequality-white.csv", header=0, delimiter=";")
    print(df.head())


if __name__ == "__main__":
    main()

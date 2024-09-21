import polars as pl
import matplotlib.pyplot as plt

# Reading files
path = "medallists.csv"
df = pl.read_csv(path)
headdata = df.head()
summary = df.describe()


def aboutdata():
    print(headdata)
    print(summary)
    return "checked"


def createplots():
    # PLOT 1
    country_medals = (
        df.group_by("country")
        .agg(pl.col("country").count().alias("medal_count"))
        .filter(pl.col("medal_count") > 0)
    )

    country_medals = country_medals.filter(pl.col("medal_count") > 0)

    countries = country_medals["country"].to_list()
    medal_counts = country_medals["medal_count"].to_list()

    plt.figure(figsize=(20, 6))
    plt.bar(countries, medal_counts, color="blue")

    plt.xlabel("Country")
    plt.ylabel("Total Number of Medals Won")
    plt.title("Medals won per country")

    plt.grid(True)
    plt.minorticks_on()
    plt.grid(which="major", linestyle="-", linewidth=0.4)
    plt.grid(which="minor", linestyle=":", linewidth=0.4)

    plt.xticks(rotation=90)

    plt.savefig("medals_per_country.png")

    # PLOT 2
    medal_counts = df.group_by("medal_date").agg(
        pl.col("medal_date").count().alias("medal_count")
    )

    dates = medal_counts["medal_date"].to_list()
    counts = medal_counts["medal_count"].to_list()

    plt.figure(figsize=(20, 6))
    plt.plot(dates, counts, marker="o")  # Plot with lines and markers
    plt.xlabel("Date")
    plt.ylabel("Total Number of Medals Won")
    plt.title("Number of Medals Won Over Time")
    plt.grid(True)

    plt.minorticks_on()
    plt.grid(which="major", linestyle="-", linewidth=0.7)
    plt.grid(which="minor", linestyle=":", linewidth=0.7)

    plt.savefig("medals_over_time.png")
    plt.show()
    return "checked"


def createsummary():
    with open("summary_report.md", "w", encoding="utf-8") as file:
        file.write("""# Mini Project: Pandas Descriptive Statistics\n\n""")
        file.write("""Adil Keku Gazder <br>""")
        file.write(""" ag825, adil.gazder@duke.edu <br>""")
        file.write("""IDS 706: Data Engineering Systems <br>""")
        file.write("""Duke University, Fall 2024\n\n""")
        file.write(
            """The aim with this project was to read a .csv file and generate summary statistics and plots describing the data. The dataset used for this project was acquired from Kaggle (Olympic Summer Games - Paris 2024 -> medallists.csv) <br>"""
        )
        file.write(
            """\n\nLink to the dataset: (https://www.kaggle.com/datasets/muhammadehsan02/olympic-summer-games-paris-2024?select=medallists.csv)\n\n"""
        )
        file.write(
            "\n\n## Distribution of total medals achieved totally over each day of the olympics\n"
        )
        file.write("![Data Visualization](medals_over_time.png)")
        file.write("\n\n## Distribution of total medals achieved per each country\n")
        file.write("![Data Visualization](medals_per_country.png)")
        return "checked"


def df_to_markdown(df, file_path):
    # Get column names and rows from the Polars DataFrame
    columns = df.columns
    rows = df.to_numpy()

    # Create a Markdown table header
    markdown = "| " + " | ".join(columns) + " |\n"
    markdown += "| " + " | ".join(["---"] * len(columns)) + " |\n"

    # Add rows to the Markdown table
    for row in rows:
        markdown += "| " + " | ".join(map(str, row)) + " |\n"

    # Write the Markdown content to the specified file
    with open(file_path, "w") as f:
        f.write(markdown)
    return "checked"


if __name__ == "__main__":
    aboutdata()
    createplots()
    createsummary()

# Nota dado a que no se tienen los archivos a manipular, los codigos no van a correr sin error
# sin embargo, se copian los codigos para el estudio de la sintaxis

# importando lib de pandas
import pandas as pd

# Para el uso de dataframes
df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)

# Pandas Series
ages = pd.Series([22, 35, 58], name="Age")
df["Age"]
df["Age"].max

# metodo describe
df-describe()

# leer archivo csv
titanic = pd.read_csv("data/titanic.csv")
titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)

titanic.head(8)
titanic.dtypes

titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)
titanic = pd.read_excel("titanic.xlsx", sheet_name="passengers")
titanic.info()


class_23 = titanic[titanic["Pclass"].isin([2, 3])]
class_23 = titanic[(titanic["Pclass"] == 2) | (titanic["Pclass"] == 3)]
class_23.head()

age_no_na = titanic[titanic["Age"].notna()]
age_no_na.head()
age_no_na.shape

adult_names = titanic.loc[titanic["Age"] > 35, "Name"]
titanic.iloc[9:25, 2:5]
titanic.iloc[0:3, 3] = "anonymus"

air_quality["londo_mg_per_cubic"] = air_quality["static_london"] * 1.882
air_quality["ratio_paris_antwerp"] = (
    air_quality["station_paris"] / air_quality["station_antwerp"]
)

air_quality_renamed = air_quality.rename(
    columns={
        "station_antwerp": "BETR801",
        "station_antwerp": "FR04014",
        "station_london": "London Westminster",
    }
)
air_quality_renamed = air_quality_renamed.rename(columns=str.lower)


titanic["Age"].mean()
titanic[["Age", "Fare"]].median()
titanic[["Age", "Fare"]].describe()
titanic.agg(
    {
        "Age": ["min", "max", "median", "skew"],
        "Fare": ["min", "max", "median", "mean"],
    }
)

titanic[["Sex", "Age"]].groupby("Sex").mean()
titanic.groupby(["Sex", "Pclass"])["Fare"].mean()
titanic.groupby("Sex").mean(numeric_only=True)
titanic.groupby("Sex")["Age"].mean()

titanic["Pclass"].value_counts()
titanic.groupby("Pclass")["Pclass"].count()

titanic.sort_values(by="Age").head()
titanic.sort_values(by=['Pclass', 'Age'], ascending=False).head()

no2 = air_quality[air_quality["parameter"] == "no2"]
no2_subset = no2.sort_index().groupby(["location"]).head(2)
no2_subset.pivot(columns="location", values="value")

air_quality.pivot_table(
    values="value", index="location", columns="parameter", aggfunc="mean"
)
air_quality.pivot_table(
    values="value", 
    index="location", 
    columns="parameter", 
    aggfunc="mean",
    margins=True
)

no_2 = no2_pivoted.melt(id_vars="date.utc")
no_2 = no2_pivoted.melt(
    id_vars="date.utc",
    value_vars=["BETR801", "FR04014", "London Westminster"],
    value_name="NO_2",
    var_name= "id_location",
)


air_quality_no2 = pd.read_csv("data/air_quality_no2_long.csv", parse_dates=True)
air_quality_no2 = air_quality_no2[["date.utc", "location", "parameter", "value"]]
air_quality_no2.head()

air_quality_pm25 = pd.read_csv("data/air_quality_pm25_long.csv", parse_dates=True)
air_quality_pm25 = air_quality_pm25[["date.utc", "location", "parameter", "value"]]
air_quality_pm25.head()

air_quality = air_quality.sort_values("date.utc")
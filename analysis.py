import pandas as pd
 
import arcticfox  
arcticfox.projectpath('analysis.py') 

# Load dataset
df = pd.read_csv("dog_speeds.csv")

# -------------------------
# Basic inspection
# -------------------------

print("First 5 rows:")
print(df.head())

print("\nDataset info:")
print(df.info())

print("\nSummary statistics:")
print(df.describe())

# -------------------------
# Counts & distributions
# -------------------------

print("\nDogs per breed:")
print(df["breed"].value_counts())

print("\nAge distribution:")
print(df["age"].value_counts().sort_index())


# -------------------------
# Speed analysis
# -------------------------

# Average speed overall
avg_speed = df["top_speed_mph"].mean()
print(f"\nAverage top speed: {avg_speed:.2f} mph")

# Average speed by breed
avg_speed_by_breed = (
    df.groupby("breed")["top_speed_mph"]
      .mean()
      .sort_values(ascending=False)
)

#> SortedGroupMean --groupColumn age --valueColumn top_speed_mph --print 
avgByGroup = df.groupby('age')['top_speed_mph'].mean().sort_values(ascending=False)
print(avgByGroup) #)1 
##*** age
##*** 7     29.748276
##*** 5     28.838235
##*** 6     28.159259
##*** 11    28.100000
##*** 10    27.996970
##*** 0     27.746341
##*** 3     27.730000
##*** 4     27.669231
##*** 2     27.546875
##*** 14    27.319444
##*** 1     27.311538
##*** 13    27.137037
##*** 15    26.746154
##*** 9     26.644000
##*** 8     26.336667
##*** 12    26.112903
##*** Name: top_speed_mph, dtype: float64



print("\nAverage top speed by breed:")
print(avg_speed_by_breed)

# Fastest individual dogs
fastest_dogs = df.sort_values("top_speed_mph", ascending=False).head(10)

print("\nTop 10 fastest dogs:")
#> print fastest_dogs 
print(fastest_dogs) #)2 
##***             name  age      breed  top_speed_mph
##*** 404    Ruby Hope    5  Greyhound           44.8
##*** 233  Clover Hope    0  Greyhound           44.7
##*** 490    Lola Rose    7  Greyhound           43.8
##*** 152    Wren Reed    6  Greyhound           43.1
##*** 112  Birdie Cruz    5     Saluki           41.9
##*** 461   Lucy Miles    0     Saluki           40.7
##*** 96   Jasper Reed    2     Saluki           40.6
##*** 421  Archie Hope    5  Greyhound           40.4
##*** 408   Rocco Jade   10  Greyhound           40.1
##*** 24    Moose Theo   12     Vizsla           40.0




# -------------------------
# Age vs speed
# -------------------------

age_speed = (
    df.groupby("age")["top_speed_mph"]
      .mean()
      .reset_index()
)

print("\nAverage speed by age:")
print(age_speed)

# -------------------------
# Simple filters
# -------------------------

# Senior dogs (10+ years)
senior_dogs = df[df["age"] >= 10]
print(f"\nNumber of senior dogs: {len(senior_dogs)}")

# Very fast dogs (over 35 mph)
very_fast = df[df["top_speed_mph"] > 35]
print(f"Number of dogs faster than 35 mph: {len(very_fast)}")

# -------------------------
# Save derived datasets
# -------------------------

avg_speed_by_breed.to_csv("avg_speed_by_breed.csv")
fastest_dogs.to_csv("fastest_dogs.csv", index=False)

print("\nSaved:")
print("- avg_speed_by_breed.csv")
print("- fastest_dogs.csv")

import pandas as pd
 
import arcticfox  
pd.set_option('display.width', 10000)
pd.set_option('display.max_columns', None)
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

#> View 
print(df.astype(str).fillna('').head()) #)1 
##***            name age                breed top_speed_mph
##*** 0    Otis Blake   6           Great Dane          24.8
##*** 1    Piper Reed  12  Australian Shepherd          22.1
##*** 2  Tucker Grace  15      Standard Poodle          29.1
##*** 3     Hazel Ray   0           Great Dane          21.2
##*** 4    Theo Grace   3     Golden Retriever          25.5


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
print('HOWDY THERE!')
print(avgByGroup) #)3 
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


#> SortedGroupMean --groupColumn breed --valueColumn age --print 
avgByGroup_1 = df.groupby('breed')['age'].mean().sort_values(ascending=False)
print('HOWDY THERE!')
print(avgByGroup_1) #)4 
##*** breed
##*** Whippet                 8.241379
##*** Afghan Hound            8.100000
##*** German Shepherd         8.074074
##*** Siberian Husky          8.060606
##*** Australian Shepherd     7.772727
##*** Weimaraner              7.560000
##*** Greyhound               7.450000
##*** Boxer                   7.448276
##*** Vizsla                  7.437500
##*** Great Dane              7.264706
##*** Labrador Retriever      7.238095
##*** Border Collie           7.210526
##*** Standard Poodle         7.103448
##*** Jack Russell Terrier    7.076923
##*** Doberman Pinscher       7.032258
##*** Dalmatian               6.960000
##*** Golden Retriever        6.862069
##*** Rhodesian Ridgeback     6.588235
##*** Belgian Malinois        6.560000
##*** Saluki                  5.869565
##*** Name: age, dtype: float64


print("\nAverage top speed by breed:")
print(avg_speed_by_breed)

# Fastest individual dogs
fastest_dogs = df.sort_values("top_speed_mph", ascending=False).head(10)

print("\nTop 10 fastest dogs:")
#> print fastest_dogs 
print(fastest_dogs) #)5 
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

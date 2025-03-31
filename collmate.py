import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans

genders = np.array(["Male", "Female", "Other"])
repayment_frequencies = np.array(["Monthly", "Quarterly", "Yearly"])
loan_types = np.array(["Car", "Home", "Personal", "Education", "Business"])
occupations = np.array(["Salaried", "Self-Employed", "Business Owner", "Freelancer"])
sma_types = np.array(["SMA-0", "SMA-1", "SMA-2"])

def generate_synthetic_collections_data(num_samples=10000):
    names = ["Customer_" + str(i) for i in range(1, num_samples + 1)]
    import random
    account_numbers = random.sample(range(1000000000, 9999999999), num_samples)
  # Ensure unique account numbers
    monthly_income = np.random.randint(20000, 200000, size=num_samples)
    collection_attempts = np.random.randint(0, 10, size=num_samples)
    repayment_frequency = np.random.choice(repayment_frequencies, size=num_samples)
    last_payment_since = np.random.randint(1, 365, size=num_samples)
    rate_of_interest = np.random.uniform(5.0, 15.0, size=num_samples).round(2)
    emi = np.random.randint(5000, 50000, size=num_samples)
    type_of_loan = np.random.choice(loan_types, size=num_samples)
    tenure_of_loan = np.random.randint(12, 240, size=num_samples)
    age = np.random.randint(21, 65, size=num_samples)
    occupation = np.random.choice(occupations, size=num_samples)
    monthly_sma_type = np.random.choice(sma_types, size=num_samples)
    gender_column = np.random.choice(genders, size=num_samples)
    dpd = np.random.randint(0, 180, size=num_samples)

    data = pd.DataFrame({
        'Name': names,
        'Account Number': account_numbers,
        'Monthly Income': monthly_income,
        'Collection Attempts': collection_attempts,
        'Repayment Frequency': repayment_frequency,
        'Last Payment Since': last_payment_since,
        'Rate of Interest': rate_of_interest,
        'EMI': emi,
        'Type of Loan': type_of_loan,
        'Tenure of Loan': tenure_of_loan,
        'Age': age,
        'Occupations': occupation,
        'Monthly SMA Type': monthly_sma_type,
        'Gender': gender_column,
        'DPD': dpd
    })
    return data

df = generate_synthetic_collections_data(10000)

def categorize_age(age):
    if 21 <= age <= 30:
        return "21-30"
    elif 31 <= age <= 40:
        return "31-40"
    elif 41 <= age <= 50:
        return "41-50"
    elif 51 <= age <= 60:
        return "51-60"
    else:
        return "61+"

df["Age Group"] = df["Age"].apply(categorize_age)

# Convert Age Group and Monthly SMA Type to numerical values for clustering
age_group_mapping = {"21-30": 0, "31-40": 1, "41-50": 2, "51-60": 3, "61+": 4}
df["Age Group Numeric"] = df["Age Group"].map(age_group_mapping)
sma_mapping = {"SMA-0": 0, "SMA-1": 1, "SMA-2": 2}
df["Monthly SMA Type Numeric"] = df["Monthly SMA Type"].map(sma_mapping)

# Use multiple features for meaningful clustering
clustering_features_age = ["Age Group Numeric", "Monthly Income", "EMI", "DPD"]
clustering_features_sma = ["Monthly SMA Type Numeric", "Collection Attempts", "DPD"]

# Perform clustering based on Age Group
kmeans_age = KMeans(n_clusters=3, random_state=42, n_init=10)
df["Age Cluster"] = kmeans_age.fit_predict(df[clustering_features_age])

# Perform clustering based on Monthly SMA Type
kmeans_sma = KMeans(n_clusters=3, random_state=42, n_init=10)
df["SMA Cluster"] = kmeans_sma.fit_predict(df[clustering_features_sma])

# Split into train and test sets
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

print("Train set size:", train_df.shape)
print("Test set size:", test_df.shape)
print(train_df.head())
#chng

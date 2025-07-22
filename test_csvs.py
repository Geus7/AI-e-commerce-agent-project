import os
import pandas as pd

print("📁 Verifying CSV files in data/raw...\n")

data_folder = "data/raw"
expected_files = ["eligibility.csv", "ad_sales.csv", "total_sales.csv"]
all_passed = True

for file in expected_files:
    path = os.path.join(data_folder, file)
    if not os.path.exists(path):
        print(f"❌ Missing: {file}")
        all_passed = False
    else:
        try:
            df = pd.read_csv(path)
            print(f"✅ Found {file} — {len(df)} rows")
        except Exception as e:
            print(f"⚠️ Error reading {file}: {e}")
            all_passed = False

if all_passed:
    print("\n🎉 All required files loaded successfully!")
else:
    print("\n🚨 One or more files are invalid or missing.")

import os

folder_path = "C:\Users\hp\OneDrive\Documents\library"

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

for i in range(1, 2001):
    folder_name = os.path.join(folder_path, f"folder_{i}")
    os.makedirs(folder_name)

print("2000 folders created successfully!")

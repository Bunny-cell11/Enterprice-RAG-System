
import pandas as pd
from faker import Faker
import os

fake = Faker()

os.makedirs("data/csv", exist_ok=True)

employees = []

for _ in range(50):
    employees.append({
        "name": fake.name(),
        "department": fake.random_element(
            elements=("Engineering", "Executive", "Support")
        ),
        "salary": fake.random_int(min=50000, max=250000)
    })

df = pd.DataFrame(employees)
df.to_csv("data/csv/employee_salaries.csv", index=False)

print("Synthetic dataset generated.")

# Databricks notebook source
from faker import Faker
import pandas as pd
import random

fake = Faker()

departments = ["IT", "HR", "Finance", "Sales", "Marketing"]
cities = ["Mumbai", "Bangalore", "Delhi", "Pune", "Chennai"]

batch_size = 100000
total_records = 2000000

for batch in range(total_records // batch_size):

    data = []

    for i in range(batch_size):
        emp_id = batch * batch_size + i + 1

        data.append({
            "employee_id": emp_id,
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "department": random.choice(departments),
            "city": random.choice(cities),
            "country": "India",
            "salary": random.randint(30000, 300000),
            "experience": random.randint(1, 20),
            "joining_date": fake.date_between(
                start_date="-10y",
                end_date="today"
            ),
            "email": f"user{emp_id}@company.com",
            "manager_id": random.randint(100, 200),
            "status": random.choice(["Active", "Inactive"])
        })

    df = pd.DataFrame(data)

    if batch == 0:
        df.to_csv("employees_2m.csv", index=False)
    else:
        df.to_csv(
            "employees_2m.csv",
            mode="a",
            header=False,
            index=False
        )

print("CSV Generated Successfully")

# COMMAND ----------

pip install faker
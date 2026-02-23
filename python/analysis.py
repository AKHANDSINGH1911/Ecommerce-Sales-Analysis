import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# connect database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Akhand@19",
    database="ecommerce"
)

# load data
query = "SELECT * FROM sales"
df = pd.read_sql(query, conn)

print("Rows:", df.shape)

 # convert date
df['orderDate'] = pd.to_datetime(df['orderDate'])
df['month'] = df['orderDate'].dt.month

# check result
print("Month column sample:")
print(df[['orderDate','month']].head())

# analysis
monthly_sales = df.groupby('month')['sales'].sum()
top_customers = df.groupby('customerName')['sales'].sum().sort_values(ascending=False).head(10)
product_sales = df.groupby('productLine')['sales'].sum().sort_values(ascending=False)
country_sales = df.groupby('country')['sales'].sum().sort_values(ascending=False)

# charts
plt.figure()
sns.lineplot(x=monthly_sales.index, y=monthly_sales.values)
plt.title("Monthly Sales Trend")
plt.savefig("../excel/monthly_sales_chart.png")

plt.figure()
sns.barplot(x=product_sales.values, y=product_sales.index)
plt.title("Product Sales")
plt.savefig("../excel/product_sales_chart.png")

 # export excel
with pd.ExcelWriter("../excel/analysis_output.xlsx") as writer:
    monthly_sales.to_excel(writer, sheet_name="Monthly Sales")
    top_customers.to_excel(writer, sheet_name="Top Customers")
    product_sales.to_excel(writer, sheet_name="Product Sales")
    country_sales.to_excel(writer, sheet_name="Country Sales")

print("Analysis complete")
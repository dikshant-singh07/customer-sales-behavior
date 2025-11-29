import pandas as pd
# Show all columns and wider output in VS Code
pd.set_option('display.max_columns', None)   # show all columns
pd.set_option('display.width', 200)          # set display width
pd.set_option('display.max_colwidth', None)  # show full column text (no cutoff)
df = pd.read_csv('E:/Customer_sales_analysis_project/customer_shopping_behavior.csv')

# print(df.head())
# print(df.info())
# print(df.describe(include='all'))
# print(df.isnull().sum())
df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(
    lambda x: x.fillna(x.median())
)
print(df.isnull().sum())


# import matplotlib.pyplot as plt

# plt.boxplot(df['Review Rating'].dropna()) #to check the outliers
# plt.title("Review Rating Distribution")
# plt.show()
df.columns = df.columns.str.lower().str.replace(' ', '_')
df = df.rename(columns = {'purchase_amount_(usd)':'purchase_amount'})
print(df.columns)

#create age_group column
labels = ['Young Adult', 'Adult', 'Middle-Aged', 'Senior']
df['age_group'] = pd.qcut(df['age'], q=4, labels=labels)
print(df[['age', 'age_group']].head(10))

#purchase_frequency_days column
frequecy_mapping = {
    'Fortnightly': 14,
    'Weekly' : 7,
    'Monthly' : 30,
    'Quarterly' : 90,
    'Bi-Weekly' :3.5,
    'Annually' : 365,
    'Every 3 Months' : 90
}
df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequecy_mapping)
print(df[['frequency_of_purchases', 'purchase_frequency_days']].head(10))

#discount and promocode applied
print(df[['discount_applied', 'promo_code_used']].head(10))
print((df['discount_applied'] == df['promo_code_used']).all())  # True if both columns are identical

df=df.drop('promo_code_used', axis=1)
print(df.columns)


from sqlalchemy import create_engine

# Format: mysql+mysqlconnector://user:password@host:port/database
engine = create_engine("mysql+mysqlconnector://root:s4m942////@localhost:3306/customer_sales_db")

df.to_sql(
    'customer_shopping_behavior',   # table name
    con=engine,
    if_exists='replace',           # 'replace' overwrites, 'append' adds rows
    index=False
)
print("Data pushed to MySQL successfully ✅")


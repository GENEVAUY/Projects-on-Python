def rename_columns_to_lower(df):
    df = df.rename(columns=str.lower)
    return df

def rename_columns(df):
    df.rename (columns = {'customer':'customer_id', 'st':'state'}, inplace=True)
    return df

def replace_percentage_in_column(df, column_name):
    df[column_name] = df[column_name].str.replace("%", " ")
    return df

def extract_single_character(df, column_name):
    df[column_name] = df[column_name].str[2]
    return df

def get_unique_values(df, column_name):
    unique_values = df[column_name].unique()
    return unique_values

def replace_gender_values(df):
    df['gender'] = df['gender'].replace(['F', 'Femal', 'female'], 'female')
    df['gender'] = df['gender'].replace(['M', 'Male'], 'male')
    return df

def get_unique_gender_values(df):
    unique_genders = df['gender'].unique()
    return unique_genders

def convert_customer_lifetime_value_to_float(df, column_name):
    df[column_name] = df[column_name].astype("float64")
    return df

def count_nan_values(df):
    nan_count = df.isna().sum()
    return nan_count

import pandas as pd

def calculate_percent_nulls(df):
    nulls_df = pd.DataFrame(round(df.isna().sum() / len(df), 4) * 100)
    nulls_df = nulls_df.reset_index()
    nulls_df.columns = ['header_name', 'percent_nulls']
    return nulls_df

def drop_rows_with_null_customer_id(df):
    df = df.dropna(subset=["customer_id"])
    return df

def count_null_values(df):
    null_count = df.isna().sum()
    return null_count

def reset_dataframe_index(df):
    df = df.reset_index(drop=True)
    return df

def get_mode_value(df, column_name):
    mode_value = df[column_name].mode()[0]
    return mode_value

def fillna_with_mode(df, column_name):
    mode_value = df[column_name].mode()[0]
    df[column_name].fillna(mode_value, inplace=True)
    return df

def calculate_mean_value(df, column_name):
    mean_value = df[column_name].mean()
    return mean_value

def fillna_with_mean(df, column_name):
    mean_value = df[column_name].mean()
    df[column_name].fillna(mean_value, inplace=True)
    return df

def check_duplicates(df):
    duplicates = df.duplicated()
    return duplicates


import pandas as pd

def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    # 1. VALIDATION - checking if new_column has a proper name
    if not is_valid_name(new_column):
        return pd.DataFrame()

    # 2. VALIDATION - checking if all columns in original df have appropriate names
    for col in df.columns:
        if not is_valid_name(col):
            return pd.DataFrame()

    # 3. VALIDATION - checking if the role has appropriate format: no numbers, just names and operation symbols (+, -, *)
    ops_col = role.replace("+", " ").replace("-", " ").replace("*", " ").split()
    if not ops_col or not all(is_valid_name(x) and x in df.columns for x in ops_col):
        return pd.DataFrame()

    # 4. ADDING NEW COLUMN
    try:
        new_df = df.copy()
        new_df[new_column] = new_df.eval(role)
        return new_df
    except Exception:
        #In case inside role there is a column name that does not match anything in the df
        return pd.DataFrame()

# VALIDATOR FUNCTION
def is_valid_name(name: str) -> bool:
    # isinstance() checks for None or True values in columns
    # bool() checks if the string is empty, it wasn't mentioned in the task, but I assumed it shouldn't be
    # all() checks if the name is made out of letters and underscores
    # RESERVED_NAMES checks if column is not named after predefined constant which gives wrong results down the line
    RESERVED_NAMES = {'inf', 'Infinity', 'infy', 'nan', 'NaN', 'null', 'True', 'False', 'pi', 'e'}
    basic_valid = isinstance(name, str) and bool(name) and all(char.isalpha() or char == '_' for char in name)
    return basic_valid and name not in RESERVED_NAMES
import pandas as pd

def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    if not is_valid_name(new_column):
        return pd.DataFrame()

    for col in df.columns:
        if not is_valid_name(col):
            return pd.DataFrame()

    #Checking if the role has appropriate format - this assumes that role cannot have operations
    #   such as "quantity * 2". It was never mentioned in the task and depending on it, this piece of code can be removed or kept.
    ops_col = role.replace("+", " ").replace("-", " ").replace("*", " ").split()
    if not ops_col or not all(is_valid_name(x) and x in df.columns for x in ops_col):
        return pd.DataFrame()

    try:
        #Avoiding side effects outside the function
        new_df = df.copy()
        #Key line of the code that executes the operation described in 'role'
        new_df[new_column] = new_df.eval(role)
        return new_df
    except Exception:
        #In case inside role there is a column name that does not match anything in the df
        return pd.DataFrame()

#Assistant function
def is_valid_name(name: str) -> bool:
    #Checking if name passes our requirements
    #isinstance() checks for None or True values in columns, technically it won't do anything for new_column since
    #   it has to be a str but better safe than sorry
    #bool() checks if the string is empty, it wasn't mentioned in the task, but I assumed it shouldn't be
    #all() checks if the name is made out of letters and underscores
    #RESERVED_NAMES checks if column is not named after predefined constant which gives wrong results down the line
    RESERVED_NAMES = {'inf', 'Infinity', 'infy', 'nan', 'NaN', 'null', 'True', 'False', 'pi', 'e'}
    basic_valid = isinstance(name, str) and bool(name) and all(char.isalpha() or char == '_' for char in name)
    return basic_valid and name not in RESERVED_NAMES
"""Main module."""
import pandas as pd

def get_aggs_by_columns(data:pd.DataFrame, columns:list, agg_list:list, agg_columns:list)->pd.DataFrame:
    """

    Parameters
    ----------
    data : pd.DataFrame : dataframe to calculate FE on
        
    columns : list : list of values to aggregate by (the object datatype)
        
    agg_list : list : a list of statistical measure e.g mean, median
        
    agg_columns : list : a list of numerical datatype columns e.g Age, Salary
        
    
    Returns
    -------

    
    """
    for cols in columns:
        for i in agg_list:
            for j in agg_cols:
                data[cols+'_'+j+'_'+i] = data.groupby([cols])[j].transform(i)

	return data

def frequency_encode(data:pd.DataFrame, column_name:str, output_column_name:str)->pd.Series:
    """

    Parameters
    ----------
    data:pd.DataFrame : dataframe with the column to perform the frequency encoding on
        
    column_name:str : column name to apply frequency encode on
        
    output_column_name:str : new column name that will be created
        

    Returns
    -------
    A pandas Series of encoded column

    """

    freq_enc = (data.groupby(column_name).size()) / len(data)
    data[output_column_name] = data[column_name].apply(lambda x : freq_enc[x])

    return data[output_column_name]

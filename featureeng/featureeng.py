"""Main module."""
import pandas as pd

def get_aggs_by_columns(data:pd.DataFrame, columns:list, agg_list:list, agg_columns:list)->pd.DataFrame:
    """

    Parameters
    ----------
    data:pd.DataFrame : dataframe to calculate FE on
        
    columns:list : list of values to aggregate by (the object datatype)
        
    agg_list:list : a list of statistical measure e.g mean, median
        
    agg_columns:list : a list of numerical datatype columns e.g Age, Salary
        

    Returns
    -------
    A dataframe

    """
    for cols in columns:
        for i in agg_list:
            for j in agg_cols:
                data[cols+'_'+j+'_'+i] = data.groupby([cols])[j].transform(i)

	return data

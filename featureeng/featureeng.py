"""Main module."""
import pandas as pd

def aggs_by_columns(data:pd.DataFrame, columns:list, agg_list:list, agg_columns:list)->pd.DataFrame:
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
    data : pd.DataFrame : dataframe with the column to perform the frequency encoding on
        
    column_name : str : column name to apply frequency encode on
        
    output_column_name : str : new column name that will be created
        

    Returns
    -------

    
    """

    freq_enc = (data.groupby(column_name).size()) / len(data)
    data[output_column_name] = data[column_name].apply(lambda x : freq_enc[x])

    return data[output_column_name]


def agg_func(data:pd.DataFrame, object_column:str, agg_list=['nunique', 'count'])->pd.DataFrame:
    """

    Parameters
    ----------
    data:pd.DataFrame :
        
    object_column:str :
        
    agg_list :
         (Default value = ['nunique', 'count'] :
        

    Returns
    -------
    A dataframe with generated colim

    """
    column_name_agg = data.groupby([object_column]).agg({object_column: agg_list})

    column_name_agg.columns = [object_column + '_'.join(x).strip('_') for x in column_name_agg.columns]

    data = pd.merge(data, column_name_agg, on=object_column, how='left')

    return data

#!/usr/bin/env python

"""Tests for `featureeng` package."""

import pytest


from featureeng import featureeng


@pytest.fixture
def response():
    """Sample pytest fixture.
    
    See more at: http://doc.pytest.org/en/latest/fixture.html

    Parameters
    ----------

    Returns
    -------

    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_get_aggs_by_columns(data:pd.DataFrame, columns:list, agg_list:list, agg_columns:list)->pd.DataFrame:
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

    return data

def test_frequency_encode(data:pd.DataFrame, column_name:str, output_column_name:str)->pd.Series:

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

    return pd.Series
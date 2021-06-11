#!/usr/bin/env python

"""Tests for `featureeng` package."""

import pytest

import pandas as pd
from featureeng import featureeng


@pytest.mark.xfail(reason ="Being Lazy, test_aggs_by_columns() has not yet been implemented")
def test_aggs_by_columns(data:pd.DataFrame, columns:list, agg_list:list, agg_columns:list)->pd.DataFrame:
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

    pass

def test_frequency_encode(data, column_name):

    expected_column_name = 'test_column'
    expected_data = pd.DataFrame(data=[[2,3,4,4], [5,6,7,7]], columns=[expected_column_name, 'column_two'])
    assert type(featureeng.frequency_encode(data=expected_data, column_name=expected_column_name)) == pd.Series, "Not Compatible"

    return pd.Series
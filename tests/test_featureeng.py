#!/usr/bin/env python

"""Tests for `featureeng` package."""

import pytest

import pandas as pd
from featureeng import featureeng
from numpy.testing import assert_almost_equal, assert_equal


# @pytest.mark.xfail(reason ="Being Lazy, test_aggs_by_columns() has not yet been implemented")
def test_aggs_by_columns():

    expected_data = pd.DataFrame()
    expected_columns = []
    expected_agg_list = []
    expected_agg_cols = []

    assert isinstance(expected_data, pd.DataFrame), "Expected Value = DataFrame"
    assert isinstance(expected_columns, list), "Expected Value = list"
    assert isinstance(expected_agg_list, list), "Expected Value = list"
    assert isinstance(expected_agg_cols, list), "Expected Value = list"

    assert_equal( isinstance(featureeng.aggs_by_columns(expected_data, expected_columns, expected_agg_list, expected_agg_cols), pd.DataFrame), True)
   
def test_frequency_encode():

    expected_column_name = 'test_column'
    expected_data = pd.DataFrame(data=[[4,7], [4,7]], columns=[expected_column_name, 'column_two'])

    assert isinstance(expected_column_name, str), "Expected Value = str"
    assert isinstance(expected_data, pd.DataFrame), "Expected Value = pd.DataFrame"

    assert type(featureeng.frequency_encode(data=expected_data, column_name=expected_column_name)) == pd.Series, "Not Compatible"

def test_agg_func():
    
    expected_object_column = 'test_column'
    expected_data = pd.DataFrame(data=[[4,7], [4,7]], columns=[expected_object_column, 'column_two'])
    expected_agg_list = []

    assert isinstance(expected_data, pd.DataFrame), "Expected Value = pd.DataFrame"
    assert isinstance(expected_object_column, str), "Expected Value = str"
    assert isinstance(expected_agg_list, list), "Expected Value = list"

    assert type(featureeng.agg_func(data=expected_data, object_column=expected_object_column)) == pd.DataFrame, "Expected a DataFrame Compatible"


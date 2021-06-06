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
    data:pd.DataFrame :
        
    columns:list :
        
    agg_list:list :
        
    agg_columns:list :
        

    Returns
    -------

    """

    return data
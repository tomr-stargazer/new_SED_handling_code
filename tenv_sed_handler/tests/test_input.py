import pytest
import numpy as np
from numpy.testing import assert_allclose

from ._testdata import expected_data_array_17
from ..input import read_file_17_SED



def test_read_file_17_SED():

    # arrange
    test_data = "_testfile_17_SED.txt"

    # act
    data_array = read_file_17_SED(test_data)

    # assert
    assert_allclose(data_array, expected_data_array_17)

    pass


def test_tabulate_file_17_SED():

    pass


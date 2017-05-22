import pytest
import numpy as np
from numpy.testing import assert_allclose
from numpy.testing import assert_approx_equal
from ._testdata import expected_data_array_17, expected_data_array_cono16
from ..input import read_file_17_SED, read_file_cono16_SED, tabulate_file_17_SED, tabulate_file_cono16_SED


def test_read_file_17_SED():

    # arrange
    test_data = "_testfile_17_SED.txt"

    # act
    data_array = read_file_17_SED(test_data)

    # assert
    assert_allclose(data_array, expected_data_array_17)

    pass


def test_tabulate_file_17_SED():
    import astropy.table
    import astropy.units as u

    # arrange
    data_array = np.array([
        [1, 1, 1, 1, 1, 1],
        [2, 100, 200, 300, 400, 500]]
        ).astype(float)
    expected_table = astropy.table.Table(data_array, names=['index', 'frequency', 'wavelength', 'H', '??', 'luminosity'])
    expected_table['frequency'].unit = u.Hz
    expected_table['wavelength'].unit = u.um
    expected_table['luminosity'].unit = u.erg/u.s

    # act
    table = tabulate_file_17_SED(data_array)

    # assert
    assert table.colnames == expected_table.colnames
    for col in table.colnames:
        assert_allclose(table[col], expected_table[col])
        assert table[col].unit == expected_table[col].unit


def test_read_file_cono16_SED():

    # arrange
    test_data = "_testfile_cono16_SED.txt"

    # act
    data_array = read_file_cono16_SED(test_data)

    # assert
    assert_allclose(data_array, expected_data_array_cono16)


def test_tabulate_file_cono16_SED():
    import astropy.table
    import astropy.units as u

    # arrange
    data_array = np.array([
        [1, 1, 1, 1, 1],
        [100, 200, 300, 400, 500]]
        ).astype(float)
    expected_table = astropy.table.Table(data_array, names=['frequency', 'wavelength', 'H', '??', 'luminosity'])
    expected_table['frequency'].unit = u.Hz
    expected_table['wavelength'].unit = u.um
    expected_table['luminosity'].unit = u.erg/u.s

    # act
    table = tabulate_file_cono16_SED(data_array)

    # assert
    assert table.colnames == expected_table.colnames
    for col in table.colnames:
        assert_allclose(table[col], expected_table[col])
        assert table[col].unit == expected_table[col].unit
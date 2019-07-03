from hipo_drf_exceptions import __version__


def test_version():
    assert __version__ == '0.1.0'


def test_field_error():
    import pdb; pdb.set_trace()
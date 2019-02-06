import pytest


def test_is_tachycardic():
    from tachycardia import is_tachycardic

    result = is_tachycardic("TAChycardic")
    assert result is True


@pytest.mark.parametrize("test_list, expected", [("tachycardic", True),
                                                 ("   TACHycardic", True),
                                                 ("tachycaric", False),
                                                 ("  Tachycardic  ,.,. ",
                                                  True),
                                                 ("..Tachycaey", False),
                                                 ("Apple", False),
                                                 ("!!TACHYCARDIC??!!", True)
                                                 ])
def test_is_tachycardic(test_list, expected):
    from tachycardia import is_tachycardic

    result = is_tachycardic(test_list)
    assert result == expected

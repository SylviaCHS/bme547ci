def test_is_tachycardic():
    from tachycardia import is_tachycardic

    expected = is_tachycardic("TAChycardic")
    assert expected == "True"


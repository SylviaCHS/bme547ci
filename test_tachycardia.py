def test_is_tachycardic():
    from tachycardia import is_tachycardic

    result = is_tachycardic("TAChycardic")
    assert result == "True"

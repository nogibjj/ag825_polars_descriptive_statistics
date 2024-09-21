from main import aboutdata, createplots, createsummary, df_to_markdown


def test_aboutdata():
    assert (aboutdata()) is not None


def test_createplots():
    assert (createplots()) is not None


def test_createsummary():
    assert (createsummary()) is not None


def test_df_to_markdown():
    assert (df_to_markdown(df, file_path)) is not None


if __name__ == "__main__":
    test_aboutdata()
    test_createplots()
    test_createsummary()

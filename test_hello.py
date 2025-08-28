from hello import abs_diff, introduce_me


def test_introduce_me():
    assert introduce_me("Tully") == "Hello, Tully, my name is Trey, your new classmate!"


def test_abs_diff():
    assert abs_diff(2, 3) == 1

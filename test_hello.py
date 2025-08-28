from hello import abs_diff, introduce_me


def test_introduce_me():
    assert introduce_me("Tully") == "Hello, Tully, my name is Trey, your new classmate!"
    assert introduce_me("Katie") == "Hello, Katie, my name is Trey, your new classmate!"
    # Edge case with special character
    assert introduce_me(";") == "Hello, ;, my name is Trey, your new classmate!"


def test_abs_diff():
    assert abs_diff(2, 3) == 1
    # Trying a negative number
    assert abs_diff(-5, 4) == 9
    assert abs_diff(1_000, 1_000) == 0

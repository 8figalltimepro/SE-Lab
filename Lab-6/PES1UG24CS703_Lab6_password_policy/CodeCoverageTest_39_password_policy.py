from password_policy import check_password, strength, suggest_fix


def test_valid_password_has_no_issues():
    assert check_password("Abcdef1!") == []


def test_too_short_password():
    assert check_password("Ab1!") == ["too short"]


def test_too_long_password():
    assert check_password("Aa1!" + "a" * 61) == ["too long"]


def test_common_password():
    assert "common" in check_password("password")


def test_no_uppercase():
    assert "no uppercase" in check_password("abcdefg1!")


def test_no_lowercase():
    assert "no lowercase" in check_password("ABCDEFG1!")


def test_no_digit():
    assert "no digit" in check_password("Abcdefg!")


def test_no_special():
    assert "no special" in check_password("Abcdefg1")


def test_strength_good():
    assert strength("Abcdef1!") == "good"


def test_strength_strong():
    assert strength("Abcdefgh1234!x") == "strong"


def test_strength_weak():
    assert strength("abcdefg1") == "weak"


def test_strength_very_weak():
    assert strength("abc") == "very weak"


def test_suggest_fix():
    assert suggest_fix([]) == "none needed"
    assert suggest_fix(["too short"]) == "add more characters"
    assert suggest_fix(["common"]) == "avoid common passwords"
    assert suggest_fix(["no uppercase"]) == "add uppercase"
    assert suggest_fix(["too long"]) == "shorten it"

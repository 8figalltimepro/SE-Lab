from password_policy import check_password, strength, suggest_fix


# ---------- length boundaries ----------

def test_seven_characters_is_too_short():
    assert check_password("Abc1!xy") == ["too short"]


def test_eight_characters_is_allowed():
    assert check_password("Abc1!xyz") == []


def test_sixty_four_characters_is_allowed():
    assert check_password("Ab1!" + "a" * 60) == []


def test_sixty_five_characters_is_too_long():
    assert check_password("Ab1!" + "a" * 61) == ["too long"]


# ---------- common passwords ----------

def test_listed_common_passwords_are_flagged():
    for pw in ["password", "123456", "qwerty", "letmein"]:
        assert "common" in check_password(pw)


def test_common_password_check_is_case_insensitive():
    assert "common" in check_password("PASSWORD")


# ---------- missing character classes ----------

def test_missing_uppercase():
    assert "no uppercase" in check_password("abcdefg1!")


def test_missing_lowercase():
    assert "no lowercase" in check_password("ABCDEFG1!")


def test_missing_digit():
    assert "no digit" in check_password("Abcdefg!")


def test_missing_special():
    assert "no special" in check_password("Abcdefg1")


# ---------- strength ratings ----------

def test_strength_good_under_fourteen():
    assert strength("Abcdef1!") == "good"


def test_strength_strong_at_fourteen():
    assert strength("Abcdefgh123!xy") == "strong"


def test_strength_weak_with_two_issues():
    assert strength("abcdefg1") == "weak"


def test_strength_very_weak_with_three_issues():
    assert strength("abcdefgh") == "very weak"


# ---------- suggest_fix ----------

def test_suggest_fix_none_needed():
    assert suggest_fix([]) == "none needed"


def test_suggest_fix_too_short():
    assert suggest_fix(["too short"]) == "add more characters"


def test_suggest_fix_common():
    assert suggest_fix(["common"]) == "avoid common passwords"


def test_suggest_fix_missing_classes():
    assert suggest_fix(["no uppercase"]) == "add uppercase"
    assert suggest_fix(["no lowercase"]) == "add lowercase"
    assert suggest_fix(["no digit"]) == "add digit"
    assert suggest_fix(["no special"]) == "add special"


def test_suggest_fix_too_long():
    assert suggest_fix(["too long"]) == "shorten it"


def test_suggest_fix_uses_first_issue():
    assert suggest_fix(["common", "no digit"]) == "avoid common passwords"

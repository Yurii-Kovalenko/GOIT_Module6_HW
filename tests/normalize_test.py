import pytest

from file_sorter import normalize_string

list_of_correct_date = [
    ("abсdf", "absdf"),
    ("Ёлки-палки", "Jolki_palki"),
    ("аbcdeфghijklm!", "abcdefghijklm_"),
    ("", ""),
    ("II квартал 2020 року!", "II_kvartal_2020_roku_"),
    ("Щось іще", "Schos_ische"),
    ("Колись перегляну", "Kolis_pereglyanu"),
    ("Їхали козаки № 5, 7-10", "Jihali_kozaki___5__7_10"),
    ("два characters", "dva_characters")
]

list_of_incorrect_date = [
    ("фbbbccdf", "abbbccdf"),
    ("аbcdefghijklm!", "abcdefghijklm!"),
    ("", " "),
    ("II квартал 2020 року!", "II_kvartal_2020_roku"),
    ("два characters", "dva characters")
]

@pytest.mark.parametrize('string, result', list_of_correct_date)
def test_correct_date(string: str, result: str) -> None:
    assert normalize_string(string) == result

@pytest.mark.parametrize('string, result', list_of_incorrect_date)
def test_incorrect_date(string: str, result: str) -> None:
    assert normalize_string(string) != result


if __name__ == '__main__':
    pytest.main()
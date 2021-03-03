import pytest
from math import sqrt


# Тест на проверку типа числа
def test_int_type():
    number_a =  10
    rl_value = type(number_a)
    exp_value = type(100)
    assert rl_value == exp_value, f'Error number:{number_a}, exp_value:{exp_value}, rl_value{rl_value}'


# Параметризованный тест на проверку квадратов целых чисел
@pytest.mark.parametrize('number,exp_value', [(10, 100), (-10, 100), (0, 0)])
def test_int_par(number, exp_value):
    rl_value = number**2
    assert rl_value == exp_value, f'Error number:{number}, exp_value:{exp_value}, rl_value:{rl_value}'


# Негативный тест на проверку корня из отрицательного числа
def test_int_neg():
    try:
        int_number = -100
        rl_value = sqrt(int_number)
        assert rl_value == 10
    except ValueError:
        pass


# Тест на проверку пересечения множеств
def test_set_len():
    set_a = {1,3,4}
    set_b = {2,3,6}
    exp_value = 1
    rl_value = len(set_a & set_b)
    assert  rl_value == exp_value,  f'Error sets:{set_a, set_b}, exp_value:{exp_value}, rl_value:{rl_value}'


# Параметризованный тест на проверку объединения множеств
@pytest.mark.parametrize('fst_set, snd_set, rez_set', [[{1,2}, {3,4}, {1,2,3,4}], [set({}), set({}), set({})], [{"Set"}, {1}, {"Set",1}]])
def test_list_3_parameters(fst_set, snd_set, rez_set):
    rl_value = fst_set | snd_set
    assert rl_value == rez_set, f'Error sets:{fst_set, snd_set}, exp_set:{rez_set}, rl_set:{rl_value}'


# Негативный тест на провку удаления элемента из множества
def test_negative_set():
    test_set = {"A", "B", "C"}
    try:
        assert test_set.remove("D")
    except KeyError:
        pass
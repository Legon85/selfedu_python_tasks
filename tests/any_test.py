from tasks.while_tasks import hellow_world, wh_5_1_10


def test_hw():
    assert hellow_world.hello_world("world") == "hellow world"


def test_cash_sum():
    assert wh_5_1_10.cash_sum(1000, 5) == 1276.28


def test_cash_sum():
    assert wh_5_1_10.cash_sum(1000, 7) == 1407.1

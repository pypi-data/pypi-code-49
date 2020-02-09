import pytest
from pyraceview.messages import MsgCarPosition


raw = (
    b"\xab\xcd\x00\x02\x00\xf5W\x14\x037\xfex\x02\xf3M\x81`\xa0\xcd\x0f\xff\x00\x00"
    b"\x00\x04\xf1\x87\x00\xc4\x80\xcc\xef\xfd\x00 \x00\x06\xf2,\xc0\xfd\xe0\xcc"
    b"\xef\xff\x00\x00\x00\x08\xf1\xdc\xc0\xe1\xf0\xcc\xef\xfd\x00 \x00\x0c\xf1\xa1"
    b"\x80\xce@\xcc\xef\xff\x00\x00\x00\x12\xf3\x00\x81G\x00\xcd\x0f\xff\x00\x00"
    b"\x00\x14\xf33\x01W\x80\xcd\x0f\xff\x00\x00\x00\x16\xf3\x1b\x01O \xcd\x0f\xff"
    b"\x00\x00\x00\x18\xf2\x14@\xf5\x80\xcc\xef\xff\x00\x00\x00\x1c\xf2\xe7A>p\xcd"
    b"\x0f\xff\x00\x00\x00$\xf1j\x00\xbap\xcc\xef\xfb\x00 \x00&\xf2\x94\x01 \xf0\xcd"
    b"\x0f\xff\x00\x00\x00(\xf3jAj@\xcd\x0f\xff\x00\x00\x00*\xf1M\xc0\xb0\xa0\xcc"
    b"\xef\xfb\x00 \x00,\xf1\xf8\x80\xeb\xb0\xcc\xef\xff\x00\x00\x00P\xf2t\x81\x16"
    b"\x90\xcd\x0f\xff\x00\x00\x00R\xf2GA\x06p\xcc\xef\xff\x00\x00\x00T\xf2\xce\x015"
    b"\x10\xcd\x0f\xff\x00\x00\x00`\xf2\xb1A+0\xcd\x0f\xff\x00\x00\x00\xb0\xf1\xc2"
    b"\x80\xd8\xd0\xcc\xef\xfd\x00 \x00"
)


@pytest.fixture
def car():
    return MsgCarPosition(raw).car_data[-1]


def test_car_id(car):
    car_id = car.car_id
    assert car_id == 176


def test_position(car):
    x = car.pos_x
    y = car.pos_y
    z = car.pos_z
    assert (x, y, z) == (-1458.2, 346.90000000000003, 81.95)


def test_heading(car):
    x = car.heading_x
    y = car.heading_y
    z = car.heading_z
    assert (x, y, z) == (
        0.999998823451702,
        1.176549336290695e-06,
        -0.0015339797350831937,
    )


def test_norm(car):
    x = car.norm_x
    y = car.norm_y
    z = car.norm_z
    assert (x, y, z) == (
        0.001533980186284766,
        -0.0007669903187427239,
        0.999998529314238,
    )

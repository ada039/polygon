from shadow.polyedr import Polyedr


class TestFacet:

    # Вершины не хорошие
    def test1(self):
        assert Polyedr(f"data/test1.geom").area == 0

    # Центр не хороший
    def test2(self):
        assert Polyedr(f"data/test2.geom").area == 0

    # 1 из 4х граней
    def test3(self):
        assert Polyedr(f"data/test3.geom").area == 0.015625

    # 64 хороших квадратных грани друг над другом
    def test4(self):
        assert Polyedr(f"data/test4.geom").area == 1

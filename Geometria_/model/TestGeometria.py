import unittest
from Geometria import Geometria


class TestGeometria(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("SetUpClass() --> Ok")

    @classmethod
    def tearDownClass(cls):
        print("teardownclass() --> OK")

    def setUp(self):
        self.a = 2.00
        self.b = 3.10
        self.c = 4.00
        self.cases_string = ["Cuadrado",
                             "Circulo",
                             "Tiangulo",
                             "Rectangulo",
                             "Pentagono",
                             "Rombo",
                             "Romboide",
                             "Trapecio"]
        self.Test_Geometria = Geometria(self.a, self.b, self.c)

    def test_a(self):
        result = self.Test_Geometria.a
        self.assertEqual(result, self.a)

    def test_b(self):
        result = self.Test_Geometria.b
        self.assertEqual(result, self.b)

    def test_c(self):
        result = self.Test_Geometria.c
        self.assertEqual(result, self.c)

    def test_areaCuadrado(self):
        a = self.Test_Geometria.a
        result = self.Test_Geometria.areaCuadrado(a)
        self.assertEqual(result, a * a)

    def test_areaCirculo(self):
        a = self.Test_Geometria.a
        PI = 3.1416
        result = self.Test_Geometria.areaCirculo(a)
        self.assertEqual(result, PI * pow(self.a, 2))
        self.assertEqual(type(result), float)

    def test_areaTiangulo(self):
        a = self.Test_Geometria.a
        b = self.Test_Geometria.b
        againts = (self.a * self.b) / 2
        result = self.Test_Geometria.areaTiangulo(a, b)
        self.assertEqual(result, againts)
        self.assertEqual(type(result), float)

    def test_areaRectangulo(self):
        a = self.Test_Geometria.a
        b = self.Test_Geometria.b
        result = self.Test_Geometria.areaRectangulo(a, b)
        self.assertEqual(result, self.a * self.b)
        self.assertEqual(type(result), float)

    def test_areaPentagono(self):
        a = self.Test_Geometria.a
        b = self.Test_Geometria.b
        result = self.Test_Geometria.areaPentagono(a, b)
        self.assertEqual(result, (self.a * self.b) / 2)
        self.assertEqual(type(result), float)

    def test_areaRombo(self):
        a = self.Test_Geometria.a
        b = self.Test_Geometria.b
        result = self.Test_Geometria.areaRombo(a, b)
        self.assertEqual(result, (self.a * self.b) / 2)
        self.assertEqual(type(result), float)

    def test_areaRomboide(self):
        a = self.Test_Geometria.a
        b = self.Test_Geometria.b
        result = self.Test_Geometria.areaRomboide(a, b)
        self.assertEqual(result, (self.a * self.b))
        self.assertEqual(type(result), float)

    def test_areaTrapecio(self):
        a = self.Test_Geometria.a
        b = self.Test_Geometria.b
        c = self.Test_Geometria.c
        result = self.Test_Geometria.areaTrapecio(a, b, c)
        self.assertEqual(result, ((self.a + self.b) / 2) * self.c)
        self.assertEqual(type(result), float)

    def test_set_figuraName(self):
        aux = []
        for cases in range(1, self.cases_string.__len__() + 1):
            self.Test_Geometria.set_figuraName(cases)
            self.assertEqual(type(self.Test_Geometria.figuraName), str)
            aux.append(self.Test_Geometria.figuraName)
        self.assertEqual(aux, self.cases_string)
        self.assertNotEqual(aux, ["do", "re", "fo", "la", "si", "o", "p"])

    def test_switch(self):
        aux_results = [(self.a * self.a),
               (3.1416 * pow(self.a, 2)),
               ((self.a * self.b) / 2),
               (self.a * self.b),
               ((self.a * self.b) / 2),
               ((self.a * self.b) / 2),
               ((self.a * self.b)),
               (((self.a + self.b) / 2) * self.c)]
        aux = []

        for case in range(1, aux_results.__len__() + 1):
            aux.append(self.Test_Geometria.switch(case))
        self.assertEqual(aux, aux_results)

    def tearDown(self):
        print("Destruyendo el contexto -> OK")
        del self.a
        del self.b
        del self.c
        del self.Test_Geometria
        del self.cases_string


if __name__ == "__main__":
    unittest.main()
# tests/test_module.py
import unittest
import medical_data_visualizer as mdv
import matplotlib as mpl
import pandas as pd

class TestMedicalDataVisualizer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Load CSV once for all tests
        cls.data = mdv.load_data("medical_examination.csv")

    def test_cat_plot(self):
        fig = mdv.draw_cat_plot(self.data)
        self.assertIsInstance(fig, mpl.figure.Figure)

    def test_heat_map(self):
        fig = mdv.draw_heat_map(self.data)
        self.assertIsInstance(fig, mpl.figure.Figure)

if __name__ == "__main__":
    unittest.main()

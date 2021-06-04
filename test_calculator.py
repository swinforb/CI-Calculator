"""
Tests for calc app
"""

import calculator

"""
class TestCalculatorApp:
	def test_add(self):
		assert 5 == calculator.add(3, 2)

	def test_subtract(self):
		assert 5 == calculator.subtract(10, 5)
"""

class TestCalculatorApp:

    def test_add(self):
        assert 5 == calculator.add(1, 4)

    def test_subtract(self):
        assert 2 == calculator.subtract(5, 3)

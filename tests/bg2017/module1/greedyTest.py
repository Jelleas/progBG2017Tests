import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib

@t.test(0)
def exactChange0(test):
	test.test = lambda : assertlib.numberOnLine(0, lib.getLine(lib.outputOf(_fileName, [0]), 0))
	test.description = lambda : "0$ aan wisselgeld staat gelijk aan 0 munten"

@t.test(1)
def exactChange41(test):
	test.test = lambda : assertlib.numberOnLine(4, lib.getLine(lib.outputOf(_fileName, [0.41]), 0))
	test.description = lambda : "0.41$ aan wisselgeld staat gelijk aan 4 munten"

@t.test(2)
def exactChange9999(test):
	test.test = lambda : assertlib.numberOnLine(39996, lib.getLine(lib.outputOf(_fileName, [9999]), 0))
	test.description = lambda : "9999$ aan wisselgeld staat gelijk aan 39996 munten"

@t.test(3)
def exactChange402(test):
	test.test = lambda : assertlib.numberOnLine(18, lib.getLine(lib.outputOf(_fileName, [4.02]), 0))
	test.description = lambda : "4.02$ aan wisselgeld staat gelijk aan 18 munten"

@t.test(10)
def handlesWrongInput(test):
	test.test = lambda : assertlib.numberOnLine(1, lib.getLine(lib.outputOf(_fileName, [-9.50, -327, 0.01]), 0))
	test.description = lambda : "handelt een verkeerde input van -9.50 en -327 af"
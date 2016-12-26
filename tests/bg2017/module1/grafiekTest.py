import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib

def before():
	import matplotlib.pyplot as plt
	plt.switch_backend("Agg")
	lib.neutralizeFunction(plt.pause)

def after():
	import matplotlib.pyplot as plt
	plt.switch_backend("TkAgg")
	reload(plt)

@t.test(0)
def showsGraph(test):
	test.test = lambda : assertlib.fileContainsFunctionCalls(_fileName, "show")
	test.description = lambda : "vertoont een grafiek"

@t.test(1)
def exactZeroPoint(test):
	test.test = lambda : assertlib.numberOnLine(0.37, lib.getLine(lib.outputOf(_fileName), 0), deviation = 0.01)\
				     and assertlib.numberOnLine(0.69, lib.getLine(lib.outputOf(_fileName), 0), deviation = 0.01)
	test.description = lambda : "print het nulpunt (x = 0.37 en y = 0.69)"
import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib

@t.test(0)
def exactHello(test):
	test.test = lambda : assertlib.exact(lib.outputOf(_fileName).split("\n")[0], "Hello, world!")
	test.description = lambda : "print precies: Hello, world!"

@t.failed(exactHello)
@t.test(1)
def oneLine(test):
	test.test = lambda : assertlib.exact(len(lib.outputOf(_fileName).split("\n")), 2)
	test.description = lambda : "print precies 1 regel"
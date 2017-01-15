import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib

#### split_needle

@t.test(0)
def has_levensteihn(test):
    test.test = lambda : assertlib.fileContainsFunctionDefinitions(_fileName, "levensteihn")
    test.description = lambda : "definieert de functie levensteihn"

@t.passed(has_levensteihn)
@t.test(1)
def is_int_levensteihn(test):
    test.test = lambda : assertlib.sameType(lib.getFunction("levensteihn", _fileName)("a", "b"), 0)
    test.description = lambda : "levensteihn geeft een int terug"

@t.passed(has_levensteihn)
@t.test(2)
def levensteihn_a(test):
    test.test = lambda : assertlib.exact(lib.getFunction("levensteihn",
        _fileName)("majeur", "mineur"), 4)
    test.description = lambda : "levensteihn werkt voor de invoer 'majeur', 'mineur'"

@t.passed(has_levensteihn)
@t.test(3)
def levensteihn_b(test):
    test.test = lambda : assertlib.exact(lib.getFunction("levensteihn",
        _fileName)("mineur", "majeur"), 4)
    test.description = lambda : "levensteihn werkt voor de invoer 'mineur', 'majeur'"

@t.passed(has_levensteihn)
@t.test(4)
def levensteihn_c(test):
    test.test = lambda : assertlib.exact(lib.getFunction("levensteihn",
        _fileName)("kitten", "sitting"), 5)
    test.description = lambda : "levensteihn werkt voor de invoer 'kitten', 'sitting'"

@t.passed(has_levensteihn)
@t.test(5)
def levensteihn_d(test):
    test.test = lambda : assertlib.exact(lib.getFunction("levensteihn",
        _fileName)("sitten", "sittin"), 2)
    test.description = lambda : "levensteihn werkt voor de invoer 'sitten', 'sittin'"

@t.passed(has_levensteihn)
@t.test(6)
def levensteihn_e(test):
    test.test = lambda : assertlib.exact(lib.getFunction("levensteihn",
        _fileName)("sitting", "sittin"), 1)
    test.description = lambda : "levensteihn werkt voor de invoer 'sitting', 'sittin'"

@t.passed(has_levensteihn)
@t.test(7)
def levensteihn_f(test):
    test.test = lambda : assertlib.exact(lib.getFunction("levensteihn",
        _fileName)("hello", "hello"), 0)
    test.description = lambda : "levensteihn werkt voor de invoer 'hello', 'hello'"

@t.passed(has_levensteihn)
@t.test(8)
def levensteihn_f(test):
    test.test = lambda : assertlib.exact(lib.getFunction("levensteihn",
        _fileName)("hello", ""), 5)
    test.description = lambda : "levensteihn werkt voor de invoer 'hello', ''"

@t.passed(has_levensteihn)
@t.test(9)
def levensteihn_g(test):
    test.test = lambda : assertlib.exact(lib.getFunction("levensteihn",
        _fileName)("", "hello"), 5)
    test.description = lambda : "levensteihn werkt voor de invoer '', 'hello'"

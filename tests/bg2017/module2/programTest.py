import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as assertlib

#@t.test(0)
#def exactChange0(test):
#	test.test = lambda : assertlib.numberOnLine(0, lib.getLine(lib.outputOf(_fileName, [0]), 0))
#	test.description = lambda : "0$ aan wisselgeld staat gelijk aan 0 munten"
#
#@t.test(1)
#def exactChange41(test):
#	test.test = lambda : assertlib.numberOnLine(4, lib.getLine(lib.outputOf(_fileName, [0.41]), 0))
#	test.description = lambda : "0.41$ aan wisselgeld staat gelijk aan 4 munten"
#
#@t.test(2)
#def exactChange9999(test):
#	test.test = lambda : assertlib.numberOnLine(39996, lib.getLine(lib.outputOf(_fileName, [9999]), 0))
#	test.description = lambda : "9999$ aan wisselgeld staat gelijk aan 39996 munten"
#
#@t.test(3)
#def exactChange402(test):
#	test.test = lambda : assertlib.numberOnLine(18, lib.getLine(lib.outputOf(_fileName, [4.02]), 0))
#	test.description = lambda : "4.02$ aan wisselgeld staat gelijk aan 18 munten"
#
#@t.test(10)
#def handlesWrongInput(test):
#	test.test = lambda : assertlib.numberOnLine(0, lib.getLine(lib.outputOf(_fileName, [-9.50, -327, 0]), 0))
#	test.description = lambda : "handelt een verkeerde input van -9.50 en -327 af"

@t.test(0)
def has_count_exact_matches(test):
    test.test = lambda : assertlib.fileContainsFunctionDefinitions(_fileName, "count_exact_matches")
    test.description = lambda : "definieert de functie count_exact_matches()"

@t.passed(has_count_exact_matches)
@t.test(1)
def is_int_count_exact_matches(test):
    test.test = lambda : assertlib.sameType(lib.getFunction("count_exact_matches", _fileName)("a", "a"), [])
    test.description = lambda : "count_exact_matches geeft een integer terug"

@t.passed(has_count_exact_matches)
@t.test(2)
def correct_count_exact_matches(test):
    test.test = lambda : sorted(int(p * 10) for p in
        lib.getFunction("count_exact_matches", 
        _fileName)("atgacatgcacaagtatgcat", "atgc")) == 2
    test.description = lambda : "count_exact_matches werkt voor invoer 'atgacatgcacaagtatgcat', 'atgc'"

@t.passed(has_count_exact_matches)
@t.test(3)
def correct_count_exact_matches(test):
    test.test = lambda : sorted(int(p * 10) for p in
        lib.getFunction("count_exact_matches", 
        _fileName)("atgacatgcacaagtatgcat", "atgc")) == 4
    test.description = lambda : "count_exact_matches werkt voor invoer 'atgacatgcacaagtatgcat', 'a'"

@t.passed(has_count_exact_matches)
@t.test(3)
def correct_count_exact_matches(test):
    test.test = lambda : sorted(int(p * 10) for p in
        lib.getFunction("count_exact_matches", 
        _fileName)("atgacatgcacaagtatgcat", "atgc")) == 0
    test.description = lambda : "count_exact_matches werkt voor invoer 'atgacatgcacaagtatgcat', 'b'"

@t.passed(has_count_exact_matches)
@t.test(4)
def correct_count_exact_matches(test):
    test.test = lambda : sorted(int(p * 10) for p in
        lib.getFunction("count_exact_matches", 
        _fileName)("atgacatgcacaagtatgcat", "atgc")) == 0
    test.description = lambda : "count_exact_matches werkt voor invoer '', 'atgc'"

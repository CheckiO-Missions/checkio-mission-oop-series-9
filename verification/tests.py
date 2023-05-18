init_code = """
if not "Car" in USER_GLOBAL:
    raise NotImplementedError("Where is 'Car'?")

Car = USER_GLOBAL['Car']

if not '__init__' in vars(Car):
    raise NotImplementedError("Where is '__init__' method?")

from inspect import signature

params = signature(Car.__init__).parameters
if not all((len(params) ==  3, 'self' in params, 'brand' in params, 'model' in params)):
    raise NotImplementedError("Check '__init__' arguments")

if not 'drive' in vars(Car):
    raise NotImplementedError("Where is 'drive' method?")

params2 = signature(Car.drive).parameters
if not all((len(params2) ==  2, 'self' in params2, 'distance' in params2)):
    raise NotImplementedError("Check 'drive' arguments")

if not "ElectricCar" in USER_GLOBAL:
    raise NotImplementedError("Where is 'ElectricCar'?")

ElectricCar = USER_GLOBAL['ElectricCar']

if not issubclass(ElectricCar, Car):
    raise TypeError("'ElectricCar' should be a child of 'Car' class")

if not '__init__' in vars(ElectricCar):
    raise NotImplementedError("Where is '__init__' method?")

params3 = signature(ElectricCar.__init__).parameters
if not all((len(params3) ==  4, 'self' in params3, 'brand' in params3, 'model' in params3, 'battery_capacity' in params3)):
    raise NotImplementedError("Check '__init__' arguments")
    

"""

run_test = """
RET['code_result'] = {}
"""

def prepare_test(test="", answer=None, middle_code="", show_code=None):
    if show_code is None:
        show_code = middle_code + "\n" + test
    if not test:
        return_code = "\nRET['code_result'] = ''"
        answer = ''
    else:
        return_code = run_test.format(test)
    return {"test_code": {"python-3": init_code + middle_code + return_code},
            "show": {"python-3": show_code},
            "answer": answer}

TESTS = {
    "First": [
        prepare_test(middle_code='''c1 = Car("Volvo", "s90")
c2 = ElectricCar("Tesla", "Model 3", 50)
c3 = ElectricCar("WV", "ID4", 35)
c4 = Car("BMW", "X6")
c5 = Car("Audi", "Q7")
cars = [c1, c2, c3, c4, c5]
[i.drive(10) for i in cars]''',
                     test="[i.is_used for i in cars]",
                     answer=[True, "Yes", "Yes", True, True])]}
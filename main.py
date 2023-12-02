def plus_numbers(a: float, b: float) -> dict:
    result = a + b
    return {"operation": "plus", "result": result}
def minus_numbers(a: float, b: float) -> dict:
    result = a - b
    return {"operation": "minus", "result": result}
def umnoj_numbers(a: float, b: float) -> dict:
    result = a * b
    return {"operation": "umnoj", "result": result}

num1 = 10.5
num2 = 5.2

plus_numbers = plus_numbers(num1, num2)
print(plus_numbers)

minus_result = minus_numbers(num1, num2)
print(minus_result)

umnoj_numbers = umnoj_numbers(num1, num2)
print(umnoj_numbers)


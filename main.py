import logging

logging.basicConfig(filename='errors.log', level=logging.ERROR)

def plus_numbers(a: float, b: float) -> dict:
    try:
        result = a + b
        return {"operation": "plus", "result": result}
    except Exception as e:
        logging.error(f"Error in plus_numbers: {e}")
        return {"error": f"Error in plus_numbers: {e}"}

def minus_numbers(a: float, b: float) -> dict:
    try:
        result = a - b
        return {"operation": "minus", "result": result}
    except Exception as e:
        logging.error(f"Error in minus_numbers: {e}")
        return {"error": f"Error in minus_numbers: {e}"}

def umnoj_numbers(a: float, b: float) -> dict:
    try:
        result = a * b
        return {"operation": "umnoj", "result": result}
    except Exception as e:
        logging.error(f"Error in umnoj_numbers: {e}")
        return {"error": f"Error in umnoj_numbers: {e}"}

num1 = 10.5
num2 = "5.2"

plus_result = plus_numbers(num1, num2)
print(plus_result)

minus_result = minus_numbers(num1, num2)
print(minus_result)

umnoj_result = umnoj_numbers(num1, num2)
print(umnoj_result)

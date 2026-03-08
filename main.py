from fastapi import FastAPI, status, HTTPException

app = FastAPI()


@app.get("/", status_code=200)
def read_root():
    """Health check endpoint"""
    return {"status": "healthy"}


@app.get("/add/{a}/{b}", status_code=200)
def add(a: str, b: str):
    """
    Add two numbers together.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="both a and b must be numbers")
    
    result = a + b
    return {
        "operation": "add",
        "a": a,
        "b": b,
        "result": result}


@app.get("/subtract/{a}/{b}", status_code=200)
def subtract(a: str, b: str):
    """
    subtract two numbers together. the second number will subtract from the first.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="both a and b must be numbers")
    
    result = a - b
    return {
        "operation": "subtract",
        "a": a,
        "b": b,
        "result": result}


@app.get("/multiply/{a}/{b}", status_code=200)
def multiply(a: str, b: str):
    """
    multiply two numbers together.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="both a and b must be numbers")
    
    result = a * b
    return {
        "operation": "multiply",
        "a": a,
        "b": b,
        "result": result}


@app.get("/divide/{a}/{b}", status_code=200)
def divide(a: str, b: str):
    """
    divide two numbers together. second number divides the first.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="both a and b must be numbers")
    
    if b == 0:
        return{"error": "division by 0 is not possible, please choose a different number"}
    else:
        result = a / b
    return {
        "operation": "divide",
        "a": a,
        "b": b,
        "result": result}


@app.get("/KPHtoMPH/{a}", status_code=200)
def KPHtoMPH(a: str):
    """
    converts kilometers per hour to miles per hour.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """
    try:
        a = float(a)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="both a and b must be numbers")
    
    result = round(a * 0.621371, 0)
    return {
        "operation": "KPHtoMPH",
        "a": a,
        "result": result}


@app.get("/standardDeviation/{a}/{b}/{c}", status_code=200)
def standardDeviation(a: str, b: str, c: str):
    """
    calculates the standard deviation of 3 numbers.
    
    Parameters:
    - a: First number
    - b: Second number
    - c: third number
    
    Returns:
    - JSON object with the result
    """
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="a, b and c must be numbers")
    
    mean = (a + b + c) / 3
    variance = ((a - mean) ** 2 + (b - mean) ** 2 + (c - mean) ** 2) / 3
    std = variance ** 0.5

    result = std
    return {
        "operation": "standardDeviation",
        "a": a,
        "b": b,
        "c": c,
        "result": result}


@app.get("/percentage/{a}/{b}", status_code=200)
def percentage(a: str, b: str):
    """
    finds the percentage of the first number compared to the second number.
    
    Parameters:
    - a: First number
    - b: Second number
    
    Returns:
    - JSON object with the result
    """
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="both a and b must be numbers")
    
    if b == 0:
        return{"error": "division by 0 is not possible, please choose a different number"}
    else:
        result = a / b * 100
    return {
        "operation": "percentage",
        "a": a,
        "b": b,
        "result": result}
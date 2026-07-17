from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="Calculator API")

# Store calculation history
calculation_history = []
calculation_id = 1


# Request Model
class CalculationRequest(BaseModel):
    a: float
    b: float


# Update Request Model
class UpdateCalculationRequest(BaseModel):
    a: float
    b: float
    operation: str


# Helper function
def save_calculation(operation, a, b, result):
    global calculation_id

    record = {
        "id": calculation_id,
        "operation": operation,
        "a": a,
        "b": b,
        "result": result
    }

    calculation_history.append(record)
    calculation_id += 1

    return record


# Home API
@app.get("/")
def home():
    return {"message": "Welcome to Calculator API"}


# -------------------------
# ADDITION
# -------------------------
@app.post("/add")
def add(data: CalculationRequest):
    result = data.a + data.b
    return save_calculation("Addition", data.a, data.b, result)


# -------------------------
# SUBTRACTION
# -------------------------
@app.post("/subtract")
def subtract(data: CalculationRequest):
    result = data.a - data.b
    return save_calculation("Subtraction", data.a, data.b, result)


# -------------------------
# MULTIPLICATION
# -------------------------
@app.post("/multiply")
def multiply(data: CalculationRequest):
    result = data.a * data.b
    return save_calculation("Multiplication", data.a, data.b, result)


# -------------------------
# DIVISION
# -------------------------
@app.post("/divide")
def divide(data: CalculationRequest):

    if data.b == 0:
        raise HTTPException(
            status_code=400,
            detail="Division by zero is not allowed."
        )

    result = data.a / data.b
    return save_calculation("Division", data.a, data.b, result)


# -------------------------
# GET ALL HISTORY
# -------------------------
@app.get("/history")
def get_history():

    return {
        "total_calculations": len(calculation_history),
        "history": calculation_history
    }


# -------------------------
# GET HISTORY BY ID
# -------------------------
@app.get("/history/{calc_id}")
def get_history_by_id(calc_id: int):

    for record in calculation_history:
        if record["id"] == calc_id:
            return record

    raise HTTPException(
        status_code=404,
        detail="Calculation not found."
    )


# -------------------------
# UPDATE CALCULATION
# -------------------------
@app.put("/history/{calc_id}")
def update_calculation(calc_id: int, data: UpdateCalculationRequest):

    for record in calculation_history:

        if record["id"] == calc_id:

            operation = data.operation.lower()

            if operation == "add":
                result = data.a + data.b
                operation_name = "Addition"

            elif operation == "subtract":
                result = data.a - data.b
                operation_name = "Subtraction"

            elif operation == "multiply":
                result = data.a * data.b
                operation_name = "Multiplication"

            elif operation == "divide":

                if data.b == 0:
                    raise HTTPException(
                        status_code=400,
                        detail="Division by zero is not allowed."
                    )

                result = data.a / data.b
                operation_name = "Division"

            else:
                raise HTTPException(
                    status_code=400,
                    detail="Invalid operation."
                )

            record["operation"] = operation_name
            record["a"] = data.a
            record["b"] = data.b
            record["result"] = result

            return {
                "message": "Calculation updated successfully.",
                "calculation": record
            }

    raise HTTPException(
        status_code=404,
        detail="Calculation not found."
    )


# -------------------------
# DELETE SINGLE HISTORY
# -------------------------
@app.delete("/history/{calc_id}")
def delete_history_by_id(calc_id: int):

    for record in calculation_history:

        if record["id"] == calc_id:
            calculation_history.remove(record)

            return {
                "message": f"Calculation ID {calc_id} deleted successfully."
            }

    raise HTTPException(
        status_code=404,
        detail="Calculation not found."
    )


# -------------------------
# DELETE ALL HISTORY
# -------------------------
@app.delete("/history")
def delete_all_history():

    calculation_history.clear()

    return {
        "message": "All calculation history deleted successfully."
    }


# Run Application
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
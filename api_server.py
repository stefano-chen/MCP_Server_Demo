from fastapi import FastAPI

app = FastAPI(title="Time Zone Converter API")

@app.get("/convert/meters")
def meters_to_miles(m: float):
    """
    Convert distance from meters to miles.
    
    1 meter = 0.00062 miles
    """
    miles = m * 0.00062
    return {
        "meters": m,
        "miles": miles
    }

@app.get("/convert/kg")
def kg_to_pounds(kg: float):
    """
    Convert weight from kilograms to pounds.
    
    1 kilogram = 2.20462 pounds
    """
    pounds = kg * 2.20462
    return {
        "kg": kg,
        "pounds": pounds
    }

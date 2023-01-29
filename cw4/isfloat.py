# Check if the entry value is float
def isfloat(str):
    try:
        float(str)
        return True
    except ValueError:
        return False
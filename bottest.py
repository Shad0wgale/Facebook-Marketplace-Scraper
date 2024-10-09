def Marketplace(city, product, minimum, maximum, listed):
    # Create a result string with the details
    result = (f"Searching for {product} in {city}.\n"
              f"Price range: ${minimum} - ${maximum}\n"
              f"Listed within the past {listed} days.")
    # Return the result string
    return result
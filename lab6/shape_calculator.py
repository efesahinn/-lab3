import geometry_utils


operations = {
    "circle_area": geometry_utils.circle_area,
    "circle_perimeter": geometry_utils.circle_perimeter,
    "rectangle_area": geometry_utils.rectangle_area,
    "rectangle_perimeter": geometry_utils.rectangle_perimeter,
    "triangle_area": geometry_utils.triangle_area
}


print("Available shapes: circle, rectangle, triangle")
print("Available calculations: _area, _perimeter (e.g., circle_area)")

operation = input("Enter the operation you want to perform: ").strip().lower()

try:
    if operation not in operations:
        raise ValueError("Invalid operation selected.")

    if operation == "circle_area" or operation == "circle_perimeter":
        radius = float(input("Enter radius: "))
        result = operations[operation](radius)

    elif operation == "rectangle_area" or operation == "rectangle_perimeter":
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))
        result = operations[operation](width, height)

    elif operation == "triangle_area":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        result = operations[operation](base, height)

    print(f"Result: {result:.2f}")

except ValueError as e:
    print(f"Input Error: {e}")
try:
    x=int(input("Enter a number below 100 : "))
    if x > 100:
        raise ValueError(x)

except ValueError:
    print(x, "is out of allowed range")
else:
    print(x, "is within the allowed range")
from decimal import Decimal

def main():
    print("(Negative numbers get automaticaly converted to positive)")
    fraction = str(input("input a ratio! "))
    print(gauge(convert(fraction)))

def convert(fraction):
    ratio = fraction
    if len(ratio.split('/')) != 2:
        raise ValueError("Wrong amount of values!")
    elif ratio.split('/')[0].isnumeric() == False or ratio.split('/')[1].isnumeric() == False:
        raise ValueError("Wrong type of values!")
    else:
        divisor = abs(int(ratio.split('/')[1]))
        divided = abs(int(ratio.split('/')[0]))
        if divisor == 0:
            raise ZeroDivisionError("Divisor is 0")
        if divided > divisor:
            """ print("Divisor is bigger then divided, or divisor is 0")
            main() """
            raise ValueError("Divisor is bigger then the divided")
        else:
            before_percentage = Decimal(round(divided/divisor*100, 2))
            percentage = before_percentage.quantize(Decimal('0.00'))
            return percentage

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return (str(percentage) + ' %')
    
if __name__ == "__main__":
    main()
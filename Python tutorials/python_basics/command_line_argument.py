 #  COMMAND LINE ARGUMENTS IN PYTHON 
# command line arguments is used to pass the arguments in the terminal and check the behaviour of the programme 
import argparse

def main():
    parser = argparse.ArgumentParser(description='A python script that adds or subtracts two numbers')
    parser.add_argument('number1', type=float, help='Please enter the value of the first number')
    parser.add_argument('number2', type=float, help='Please enter the value of the second number')
    parser.add_argument("-a", "--addition", action="store_true", help='Performs addition')
    parser.add_argument("-s", "--subtract", action="store_true", help='Performs subtraction')
    
    args = parser.parse_args()

    if args.addition:
        result = args.number1 + args.number2
        operation_done = "Addition"
    elif args.subtract:
        result = args.number1 - args.number2
        operation_done = "Subtraction"
    else:
        parser.error("Please use -a or --addition for addition and -s or --subtract for subtraction")
        return 

    print(f"The {operation_done} of {args.number1} and {args.number2} is = {result}")

if __name__ == '__main__':
    main()

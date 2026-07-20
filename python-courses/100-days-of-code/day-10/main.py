import art
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

math ={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
logo_bas=1
with_result="n"
previous_result=0
while True:
    if logo_bas==1:
        print(art.logo)
    if with_result=="n":
        a=float(input("What's the first number?: "))
    elif with_result=="y":
        a=previous_result
    print("- \n+ \n*\n/" )
    operation=str(input("Pick an operation: "))
    b=float(input("What's the next number?: "))
    result=math[operation](a,b)
    print(f"{a} {operation} {b} = {result}")
    decision=input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    if decision=="y":
        previous_result=result
        with_result="y"
        logo_bas=0
    elif decision=="n":
        with_result="n"
        print("\n"*20)
        logo_bas=1
from pyfiglet import figlet_format
from sys import exit


def Menu_1(X_list) -> int:
    print(f"""{figlet_format("Regression lab : ", "big")}
    
=================================================
""")
    try:
        Chart_number = int(input("\nChart number >>> ")) - 1

        is_in = Chart_number >= 0 and Chart_number <= (len(X_list) - 1)

        if is_in == True:
            return Chart_number

        elif is_in == False:
            input("\nChart number is out of index\n\nPress any kay to exit ... ")
            exit()

    except ValueError:
        input("\n1Input is incorrect\n\nPress any kay to exit ... ")
        exit()


def Menu_2() -> tuple[int, int | None]:
    print(f"""{figlet_format("Regression lab : ", "big")}

=================================================

[1]. Polynomial
[2]. Non-polynomial

=================================================
""")

    try:
        Type = int(input(">>> "))

        if Type == 1:
            Degree = int(input("\nDegree >>> "))

            if Degree > 0:
                return Type, Degree

            else:
                input("\nnumber is out of index\n\nPress any kay to exit ... ")
                exit()

        elif Type == 2:
            return Type, None

        else:
            input("\nnumber is out of index\n\nPress any kay to exit ... ")
            exit()

    except ValueError:
        input("\nInput is incorrect\n\nPress any kay to exit ... ")
        exit()

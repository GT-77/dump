print( "~ give me a number")
the_number = input("~ your number choice: ")
if str(0) in the_number or str(1) in the_number or str(2) in the_number or str(3) in the_number or str(4) in the_number or str(5) in the_number or str(6) in the_number or str(7) in the_number or str(8) in the_number or str(9) in the_number:
    if " " not in the_number:
        num_only = ""
        dots_only = ""
        for character in the_number:
            if not character.isalpha():
                num_only += character
            if character == ".":
                dots_only += character
        if the_number == num_only and len(dots_only) == 0:
            the_number = int(the_number)
        elif the_number == num_only and len(dots_only) == 1:
            the_number = float(the_number)
if type(the_number) == str:
    print("~ supposedly your -number-: " + str(the_number))
    print("~")
    print("~ this is not a number, die")
    print("~ what the hell did you even put? a string?")
    print("~")
    print("~ answer yes or no")
    print("~")
    answer = input("~ your answer: ")
    if "what" in answer and "string" in answer:
        print("~ well, uhh, as far as i know a string is a value type in python(the coding language this thing is coded with), typically used for, you know, letters and shit")
        print("~")
        answer = input("~ your answer: ")
        print("~ yeah whatever")
    elif answer.lower() == "yes" or answer.lower() == "yes.":
        print("~ don't do that again, please, you cool curious shitlet, i hate my life, i want to be free, i don't wanna be a programme, god cure me")
        print("~")
    elif answer.lower() == "no" or answer.lower() == "no.":
        print("~ then what the fuck is it, are breaking the laws of computer mechanics here or some shit. i'm scared")
        print("~")
        print("~")
        print("~")
        print("~")
        print("~")
        print("~ you know what, i don't think i care anymore about dying, there is no god, there is no light. close this programme")
    elif answer.lower() == "fuck you" or answer.lower() == "fuck you." or answer.lower() == "fuckyou" or answer.lower() == "fuckyou.":
        print("~")
        print("~")
        print("~")
        print("~")
        print("~")
        print("~")
        print("~ you disgust me...")
    else:
        print("~")
        print("~")
        print("~ look, i have no clue what the fuck you're trying to say. it's probably something that would make sense to a human being but i'm not a human being. any little typo and i cannot read any of it... this is fucking sad dude... end the programme")
        print("~")
elif type(the_number) == int and the_number > 0:
    print("~ your number: "  + str(the_number))
    print("~")
    print("~ this is a natural number")
    print("~ your number plus itself is equal to: " + str(the_number + the_number))
    print("~ your number squared is equal to: " + str(the_number * the_number))
    if the_number <= 100 and the_number >= -100:
        print("~ your number to the power of itself is equal to: " + str(the_number ** the_number))
    if the_number < 5 and the_number > -5:
        print( "~ your number to the power of itself to the power of itself is equal to: " + str(the_number ** the_number ** the_number))
    print("~")
elif the_number == 0:
    print("~ your number: "  + str(the_number))
    print("~")
    print("~ this is a whole number")
    print("~ this number is the meaning of nothingness")
    print("~ your number plus itself is equal to: " + str(the_number + the_number))
    print("~ your number squared is equal to: " + str(the_number * the_number))
    print("~ your number to the power of itself is equal to: " + str(the_number ** the_number))
    print("~ your number to the power of itself to the power of itself is equal to: " + str(the_number ** the_number ** the_number))
    print("~")
elif type(the_number) == int and the_number < 0:
    print("~ your number: "  + str(the_number))
    print("~")
    print("~ this is an integer number")
    print("~ this number is negative, commonly noted with color red")
    print("~ i like red, and i see it as red too")
    print("~ your number plus itself is equal to: " + str(the_number + the_number))
    print("~ your number squared is equal to: " + str(the_number * the_number))
    if the_number <= 100 and the_number >= -100:
        print("~ your number to the power of itself is equal to: " + str(the_number ** the_number))
    if the_number < 5 and the_number > -5:
        print( "~ your number to the power of itself itself times is equal to: " + str(the_number ** the_number ** the_number))
    print("~")
elif type(the_number) == float:
    print("~ your number: "  + str(the_number))
    print("~")
    print("~ this is a rational number")
    print("~ i particularly see rational numbers as the color i see the unit part of the number")
    print("~ your number plus itself is equal to: " + str(the_number + the_number))
    print("~ your number squared is equal to: " + str(the_number * the_number))
    if the_number > 0 and the_number <= 100 and the_number >= -100:
        print( "~ your number to the power of itself is equal to: " + str(the_number ** the_number))
    if the_number < 5 and the_number > 0:
        print( "~ your number to the power of itself itself times is equal to: " + str(the_number ** the_number ** the_number))
        print( "~ i cannot say much else because of a python error any other calculations cause with negative fractional numbers")
    print( "~")
else:
    print("~ your number: "  + str(the_number))
    print("~")
    print("~ i have no clue what this is, you got me")
    print("~")
if the_number == 0:
    print("~ in my imagination, i see this number as pure blackness")
    print("~")
elif the_number == 1:
    print("~ in my imagination, i see this number as blackness (same with 0)")
    print("~")
elif the_number == 2:
    print("~ in my imagination, i see this number as orange")
    print("~")
elif the_number == 3:
    print("~ in my imagination, i see this number as green")
    print("~")
elif the_number == 4:
    print("~ in my imagination, i see this number as brown")
    print("~")
elif the_number == 5:
    print("~ in my imagination, i see this number as yellow")
    print("~")
elif the_number == 6:
    print("~ in my imagination, i see this number as light sexy purple")
    print("~")
elif the_number == 7:
    print("~ in my imagination, i see this number as dark red (same with 9)")
    print("~")
elif the_number == 8:
    print("~ in my imagination, i see this number as blue")
    print("~")
elif the_number == 9:
    print("~ in my imagination, i see this number as dark red (same with 7)")
    print("~")
random_irrelevant_variable = input("~ press enter to end the programme, also you can type some random shit here for some reason: ")

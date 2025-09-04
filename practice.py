for alyssa in range(11):
    for ben in range(11):
        for cal in range(11):
            total =(alyssa + ben + cal == 10)
            two_less = (ben == alyssa-2)
            twice = (cal == 2*alyssa)
            if total and two_less and twice:
                print(f"Alyssa sold {alyssa}, tickets")
                print(f"Ben sold {ben}, tickets")
                print(f"cal sold {cal}, tickets ")

        
rating = int(input("Enter rating: "))
if rating < 0:
    print("invalid")

ranks = [(2100, "Grand Master"),
         (1900, "Candidate Master"),
         (1600, "Expert"),
         (1400, "Pupil"),
         (0,    "Newbie")
        ]

for boundary, name in ranks:
    if rating >= boundary:
        if rating % 2 == 0:
            print(name.upper())
        else:
            print(name.lower())
        break



def mad_libs():
    print("Hello world")
    print(" O")
    print("-()-")
    print(" ^")

    noun_1 = input("Give me a noun: ")
    name = input("Give me a name: ")
    noun_2 = input("Give me another noun: ")
    verb = input("Give me a verb: ")
    adjective_1 = input("Give me a adjective: ")
    noun_3 = input("Give me another noun: ")
    place = input("Give me a place: ")
    adverb = input("Give me a adverb: ")
    silly_word = input("Give me a silly word: ")
    plural_noun_1 = input("Give me a plural noun: ")
    adjective_2 = input("Give me another adjective: ")
    adjective_3 = input("Give me another adjective: ")
    plural_noun_2 = input("Give me another plural noun: ")
    feeling = input("Give me a feeling: ")
    adjective_4 = input("Give me another adjective: ")

    story = "===================================================\n" \
            "\t\tHere is your story.\n" \
            "===================================================\n" \
            "Once there was a " + noun_1 + " named " + name + " who lived on/in a " + noun_2 + ".\n" \
            "One day he/she " + verb + " in his/her " + adjective_1 + " " + noun_3 + "." \
            "He/she went to " + place + " " + adverb + "\n" \
            " and met " + silly_word + " " + plural_noun_1 + ".\n" \
            "They became " + adjective_2 + " friends. Soon they became " + adjective_3 + \
            ". " + plural_noun_2 + " knew their names.\n" \
            "They felt " + feeling + " because they were " + adjective_4 + ".\n" \
            "==================================================="

    print(story)
    print("Thank you for using my program.")

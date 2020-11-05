import webbrowser, sys #12:30 am 11/5/2020 Lets do this!

def main():

    def preterite():
        preteriteverb = input("Whats your spanish verb?\n")
        webbrowser.open_new('https://www.livelingua.com/spanish/verbs/tenses/preterite/' + preteriteverb)
        again = input("Stay in this tense?(y/n)\n")
        if again == 'y':
            preterite()
        else:
            main()

    def present():
        presentverb = input("Whats your spanish verb?\n")
        webbrowser.open_new('https://www.livelingua.com/spanish/verbs/tenses/present/' + presentverb)
        again = input("Stay in this tense?(y/n)\n")
        if again == 'y':
            present()
        else:
            main()

    def future():
        futureverb = input("Whats your spanish verb?\n")
        webbrowser.open_new('https://www.livelingua.com/spanish/verbs/tenses/future/' + futureverb)
        again = input("Stay in this tense?(y/n)\n")
        if again == 'y':
            future()
        else:
            main()
    
    def imperfect():
        imperfectverb = input("Whats your spanish verb?\n")
        webbrowser.open_new('https://www.livelingua.com/spanish/verbs/tenses/imperfect/' + imperfectverb)
        again = input("Stay in this tense?(y/n)\n")
        if again == 'y':
            imperfect()
        else:
            main()
            
    def presentperfect():
        presentperfectverb = input("Whats your spanish verb?\n")
        webbrowser.open_new('https://www.livelingua.com/spanish/verbs/tenses/present-perfect/' + presentperfectverb)
        again = input("Stay in this tense?(y/n)\n")
        if again == 'y':
            presentperfect()
        else:
            main()
            
    def pastperfect():
        pastperfectverb = input("Whats your spanish verb?\n")
        webbrowser.open_new('https://www.livelingua.com/spanish/verbs/tenses/past-perfect/' + pastperfectverb)
        again = input("Stay in this tense?(y/n)\n")
        if again == 'y':
            pastperfect()
        else:
            main()
            
    def futureperfect():
        futureperfectverb = input("Whats your spanish verb?\n")
        webbrowser.open_new('https://www.livelingua.com/spanish/verbs/tenses/future-perfect/' + futureperfectverb)
        again = input("Stay in this tense?(y/n)\n")
        if again == 'y':
            futureperfect()
        else:
            main()
            
    Tense = input("What tense is the verb you need conjugated?\n1.Present Tense\n2.Preterite Tense\n3.Future Tense\n4.Imperfect Tense\n5.Present Perfect Tense\n6.Past Perfect Tense\n7.Future Perfect Tense\n\n8. Quit\n")

    if Tense == '1':
        preterite()

    elif Tense == '2':
        present()

    elif Tense == '3':
        future()

    elif Tense == '4':
        imperfect()

    elif Tense == '5':
        presentperfect()

    elif Tense == '6':
        pastperfect()

    elif Tense == '7':
        futureperfect()

    elif Tense == '8':
        sys.exit()
    else:
        print("Please enter 1,2,3,4,5,6 to chose what tense.\n")
        main()

    # I have plans to improve this with webscraping but I need to learn how to pull from html tables
main()

# Finished at 1:07 am 11/5/2020

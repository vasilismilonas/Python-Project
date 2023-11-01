# Οι βιβλιοθήκες που χρησιμοποιούμε
import pandas as pd
import datetime
from random import randint


# Γίνεται χρήση ενός dictionary για να αποθηκεύονται οι επιλογές στο μενού
menu_options = {
    1: 'Ημέρες για Αποφοίτηση',
    2: 'Καλάθι Αγορών',
    3: 'Μάντεψε τον Αριθμό',
    4: 'Παιχνίδι Σκορ 4',
    5: 'Έξοδος'
}


def print_menu():
    """Συνάρτηση Μενού που εκτυπώνει τις επιλογές"""
    for key in menu_options:
        print(key, '--', menu_options[key])


def askisi1():
    """Άσκηση 1 
    • Ο χρήστης θα πρέπει να εισάγει την πιθανή ημερομηνία αποφοίτησης του από τη σχολή.
    • Ο υπολογιστής θα του εμφανίζει τον υπολειπόμενο χρόνο που του απομένει μέχρι να
    ολοκληρώσει τις σπουδές του.
        • Ο χρόνος θα πρέπει να εμφανίζεται σε Έτη, Μήνες και Ημέρες.
•    Η τρέχουσα ημερομηνία θα πρέπει να υπολογίζεται δυναμικά."""
    # Ορίζεται ένα pandas dataframe για να αποθηκεύονται οι απαντήσεις της άσκησης σε αυτό
    results1 = pd.DataFrame()
    flag = False
    print("Εισάγετε την πιθανή ημερομηνία αποφοίτησης (μορφή: ΗΗ/ΜΜ/ΕΕΕΕ)")

    # Με τη χρήση του while πραγματοποιείται επανάληψη
    while(flag == False):
        # Το try είναι ένα exception handler έτσι ώστε να μην γίνει διακοπή του προγράμματος αν εισαχθεί λάθος ηερομηνία
        try:
            user_input = str(input())
            # Παίρνει την είσοδο του χρήστη και την χωρίζει με βάση το /
            temp = user_input.split("/")
            # Μετατρέπει σε μορφή datetime τις τρείς τιμές που χώρισε (ΗΗ/ΜΜ/ΕΕΕΕ)
            user_date = datetime.datetime(
                int(temp[2]), int(temp[1]), int(temp[0]))
            # Θέτει το flag σε True για να σταματήσει το while
            flag = True
            # Παίρνει τη σημερινή ημερομηνία
            now = datetime.datetime.now()
            # Ελέγχει εάν η ημερομηνία που έδωσε ο χρήστης είναι μικρότερη από τη σημερινή
            if(user_date < now):
                print("Εισάγετε μια μελλοντική ημερομηνία!")
                flag = False
            else:
                remaining = user_date - now
                # Το except πιάνει όλες τις περιπτώσεις λανθασμένης εισόδου και εκτυπώνει το παρακάτω μήνυμα
        except:
            print("Εισάγετε έγκυρη ημερομηνία!")

    print(f'Για την αποφοίτηση, απομένoυν: {remaining.days} μέρες.')
    # Γίνεται append η ημέρα αποθήκευσης στο dataframe με τα αποτελέσματα της άσκησης
    results1 = results1.append(
        {'Ημέρες Αποφοίτησης': remaining.days}, ignore_index=True)
    results1.to_csv("Apotelesmata1.csv")
    return str(remaining.days)


def askisi2():
    """Συνάρτηση ->  Το Καλάθι Της Εβδομάδας.
    Ο Χρήστης επιλέγει τα προιόντα που που θέλει να προσθέσει στο καλάθι 
    από μια υπάρχουσα λίστα προιόντων """

    # Δημιουργείται λίστα με τα προιόντα
    product_list = ["Eggs", "Milk", "Bread", "Cereal", "Pasta",
                    "Coffee", "Beef", "Chicken", "Lamb", "Flour", "Honey", "Cheese"]
    # Δημιουργείται λίστα με τις τιμές των προιώντων
    price_list = [5, 3, 2, 5, 2, 6, 9, 7, 10, 1.6, 12, 9.6]
    # Δημιουργείται λίστα με τις διαθέσιμες ποσότητες των προιώντων
    quantity_list = [12, 20, 5, 3, 12, 3, 16, 12, 12, 19, 8, 7]
    # Δημιουργείται DataFrame από τις παραπάνω λίστες
    df = pd.DataFrame({"Products": product_list,
                      "Price(in Euros)": price_list, "Quantity": quantity_list})
    print("Please view the Super Market List\n\n", df, "\n\n")
    shopping_cart = pd.DataFrame()
    # Ο χρήστης επιλέγει τον αριθμό του προιόντος που επιθυμεί
    i = int(input("Enter your desired product: "))
    # Έλεγχος για το αν υπάρχει το index +1 αυτού του προιόντος στο dataframe
    if (i+1) in list(df.index.values):
        # Βρόγχος επανάληψης
        while(True):
            # Εάν υπάρχει τότε μπαίνει στο shopping cart
            shopping_cart = shopping_cart.append(df.loc[[i]])
            print(shopping_cart)
            # Ερώτηση στον χρήστη για το εάν επιθυμεί να προσθέσει και άλλο προιόν
            mp = input(
                "This is your current shopping cart. Would you like to add more products Yes/No ?\n\n")
            if mp == "Yes":
                print("Please view the Super Market List\n\n", df, "\n\n")
                i = int(input("Enter your desired product: "))
            else:
                # Ερώτηση για το εάν θέλει να βγάλει κάποιο προιόν από το καλάθι
                print(shopping_cart)
                inp = input(
                    "This is your current shopping cart. Would you like to remove any product Yes/No ?\n\n")
                if inp == "Yes":
                    # Εισάγει τον αριθμό του προιόντος που θέλει να βγάλει
                    rem = int(input("Enter which product you want to remove: "))
                    if rem in list(shopping_cart.index.values):
                        shopping_cart = shopping_cart.drop([rem])
                        # Εκτυπώνεται το καλάθι και το υπόλοιπο('αθροισμα στήλης Price)
                        print(shopping_cart, "\nYour total is\t" +
                              str(shopping_cart['Price(in Euros)'].sum()) + "\tEuros")
                        # To shopping cart dataframe μετατρέπεται σε csv για να μπορεί να δεί ο χρήστης τα αποτελέσματα
                        shopping_cart.to_csv("Apotelesmata2.csv")
                        break
                else:
                    print(shopping_cart, "\nYour total is\t" +
                          str(shopping_cart['Price(in Euros)'].sum()) + "\tEuros")
                    shopping_cart.to_csv("Apotelesmata2.csv")
                    break


def askisi3():
    """• Ο υπολογιστής προσπαθεί να μαντέψει τον αριθμό που σκέφτηκε ο χρήστης.
    • Ο χρήστης σκέφτεται έναν αριθμό από το 1 έως το 100.
    • Ο υπολογιστής προσπαθεί να τον μαντέψει.
    • Κάθε φορά που ο υπολογιστής δίνει μία εκτίμηση, ο χρήστης του αναφέρει, εάν αριθμός είναι
    μεγαλύτερος ή μικρότερος από αυτόν που πρέπει να μαντέψει.
    • Ομοίως, η διαδικασία επαναλαμβάνεται μέχρι ο υπολογιστής να μαντέψει τον αριθμό.
    • Στο τέλος εκτυπώνεται μήνυμα επιτυχίας μαζί με το πλήθος των προσπαθειών για να μαντεύσει
    ο χρήστης τον ο αριθμό.
"""
    # Ορίζεται η κλάση Guess για το παιχνίδι

    class Guess():
        # Ορίζεται ο constructor της κλάσης Guess
        def __init__(self):
            self.number = randint(0, 100)  # Τυχαίος ακέραιος αριθμός από 0-100
            self.secret = 0
            self.guesses = 0
            self.game()
        # Συναρτηση της κλάσης Guess που ορίζει το παιχνίδι

        def game(self):
            # Ορίζεται dataframe που θα αποθηκεύει τα αποτελέσματα του παιχνιδιού
            results3 = pd.DataFrame()
            # Ο χρήστης καλείται να εισάγει έναν ακέραιο αριθμό(μυστικός)
            self.secret = int(
                input("Παρακαλώ εισάγετε έναν ακέραιο αριθμό μεταξύ 0-100\n"))
            if self.secret > 100:
                # Έλεγχος για το αν ο αριθμός έχει τη σωστή μορφή (0-100)
                print("Παρακαλώ εισάγετε αριθμό μικρότερο του 100")
                exit()
            while(True):
                # Ερώτηση ως προς τον χρήστη για το εάν ο αριθμός είναι μικρότερος ή μεγαλύτερος απο τον τχαίο αριθμό
                ret = str(input("Ο αριθμός είναι μεγαλύτερος/μικρότερος/ίσος από τον αριθμό\t" +
                          str(self.number) + "; Smaller/Bigger/Equals\n"))
                if ret == "Bigger":
                    self.number = self.number + 1
                    self.guesses = self.guesses + 1
                if ret == "Smaller":
                    self.number = self.number - 1
                    self.guesses = self.guesses + 1
                if self.number == self.secret:
                    print("Ο αριθμός σας είναι ο \t" + str(self.number) +
                          "  Εκανα\t" + str(self.guesses)+"\tΠροσπάθειες")
                    break
                else:
                    print("Παρακαλώ εισάγετε σωστή είσοδο")
            results3 = results3.append(
                {'Μυστικός Αριθμός': self.number, "Προσπάθειες":self.guesses}, ignore_index=True)
                #Παίρνουμε τον αριθμό και τις προσπάθειες και τις κάνουμε append σε στο dataframe και έπειτα σε csv
            results3.to_csv("Apotelesmata3.csv")
    # Συνάρτηση που καλεί το παιχνίδι

    def new_game():
        user_play = input("Παρακαλώ εισάγετε το 1 για να παίξετε\n")
        while user_play != "1":
            new_game()
        if user_play == "1":
            Guess()
    new_game()


def askisi4():
    """• Υπάρχουν δύο χρήστες.
    • Ο πρώτος έχει το σύμβολο Χ και ο δεύτερος στο Ο.
    • Εναλλάξ οι χρήστες πληκτρολογούν τη στήλη στην οποία επιθυμούν να ρίξουν την βολή τους.  
    • Ο πίνακας αποτελείται από 6 γραμμές και 7 στήλες.
 """
    import numpy as np
    # Ορίζεται dataframe που θα αποθηκεύει τα αποτελέσματα του παιχνιδιού
    results4 = pd.DataFrame()
    #Ορίζεται ο αριθμός στηλών και γραμμών που θα έχει ο πίνακας
    NUM_OF_ROWS = 6
    NUM_OF_COL = 7

    def create_board():
        """Συνάρτηση που δημιουργεί πίνακα με διαστάσεις και τον γεμίζει με ."""
        board = np.chararray((NUM_OF_ROWS, NUM_OF_COL), unicode=True)
        board.fill('.')
        return board

    def put_symbol(board, row, col, symbol):
    #Συνάρτηση που εισάγει σύμβολο σε θέση του πίνακα
    
        board[row][col] = symbol
    #Συνάρτηση που ελέγχει εάν είναι έγκυρη η θέση
    def is_valid_row(board, col):
        return board[NUM_OF_ROWS-1][col] == '.'

    def get_next_open_row(board, col):
        for r in range(NUM_OF_ROWS):
            if board[r][col] == '.':
                return r

    def print_board(board):
        #print(np.flip(board, 0))
        print(board)
    #Συνάρτηση που ελέγχει εάν έχει γίνει κίνηση που κερδίζει το παιχνίδι
    def winning_move(board, symbol):
        for c in range(NUM_OF_COL-3):  # ελέγχεται εάν υπάρχει οριζόντια νίκη
            for r in range(NUM_OF_ROWS):
                if board[r][c] == symbol and board[r][c+1] == symbol and board[r][c+2] == symbol and board[r][c+3] == symbol:
                    return True

        for c in range(NUM_OF_COL):  # ελέγχεται εάν υπάρχει κάθετη νίκη
            for r in range(NUM_OF_ROWS):
                if board[r][c] == symbol and board[r+1][c] == symbol and board[r+2][c] == symbol and board[r+3][c] == symbol:
                    return True

        for c in range(NUM_OF_COL-3):  # ελέγχεται εάν υπάρχει νίκη στη κύρια διαγώνιο
            for r in range(NUM_OF_ROWS-3):
                if board[r][c] == symbol and board[r+1][c+1] == symbol and board[r+2][c+2] == symbol and board[r+3][c+3] == symbol:
                    return True

        for c in range(NUM_OF_COL-3):  # ελέγχεται εάν υπάρχει νίκη στη δευτερεύουσα διαγώνιο
            for r in range(3, NUM_OF_ROWS):
                if board[r][c] == symbol and board[r-1][c+1] == symbol and board[r-2][c+2] == symbol and board[r-3][c+3] == symbol:
                    return True

    game_over = False  # Αρχικοποίηση των μεταβλητών του παιχνιδιού
    board = create_board()
    turn = 1

    print_board(board)  # Έναρξη παιχνιδιού
    while not game_over:
        if turn % 2 == 1:  # Στους μονούς γύρους παίζει ο παίκτης 1 και στους ζυγούς ο παίκτης 2

            col = int(input("Παίκτης 1 παίζει. Διαλέξτε στήλη (1-7): ")) - 1
            while(col < 0 or col > 6):
                col = int(
                    input("Παρακαλώ εισάγετε έγκυρο αριθμό στήλης(1-7): ")) - 1
            #Ελέγχεται εάν είναι έγκυρη η θέση που δίνει ο χρήστης
            if is_valid_row(board, col):
                row = get_next_open_row(board, col)
                put_symbol(board, row, col, 'X')
                #Ελέγχεται εάν έχει γίνει κίνηση που κερδίζει το παιχνίδι
                if winning_move(board, 'X'):
                    print_board(board)
                    print("Ο παίκτης 1 κερδίζει το παιχνίδι!")
                    #Τελειώνει το παιχνίδι
                    game_over = True
                    results4 = results4.append(
                        {'Νικητής': "Παίκτης 1"}, ignore_index=True)
                    results4.to_csv("Apotelesmata4.csv")
                    break

        else: #Αντίστοιχαγια παίκτη 2

            col = int(input("Παίκτης 2 παίζει. Διαλέξτε στήλη (1-7): ")) - 1
            while(col < 0 or col > 6):
                col = int(
                    input("Παρακαλώ εισάγετε έγκυρο αριθμό στήλης(1-7): ")) - 1

            if is_valid_row(board, col):
                row = get_next_open_row(board, col)
                put_symbol(board, row, col, 'O')

                if winning_move(board, 'O'):
                    print_board(board)
                    print("Ο παίκτης 2 κερδίζει το παιχνίδι!")
                    game_over = True
                    results4 = results4.append(
                        {'Νικητής': "Παίκτης 1"}, ignore_index=True)
                    results4.to_csv("Apotelesmata4.csv")
                    break

        turn += 1
        print_board(board)


def main():
    """Main Συνάρτηση που εκτυπώνει το Menu και ζητά τον χρήστη να επιλέξει ποιά άσκηση θέλει να τρέξει """
    while(True):
        print_menu()
        try:
            option = int(input("Επιλέξτε ποιά άσκηση θέλετε να τρέξετε:"))
        except:
            print('Wrong input. Please enter a number ...')
            #Ανάλογα με τις είσοδο (αριθμός) τρέχει την άσκηση που επιθυμεί
        if option == 1:
            askisi1()
            main()
        elif option == 2:
            askisi2()
            main()
        elif option == 3:
            askisi3()
            main()
        elif option == 4:
            askisi4()
            main()
        elif option == 5:
            break
        else:
            #Εάν δέν είναι έγκυρη η είσοδος του χρήστη
            print("Invalid Option. Please enter a number between 1 and 4")

    exit()


if __name__ == '__main__':
    main()
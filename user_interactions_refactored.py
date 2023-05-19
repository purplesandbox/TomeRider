from internal_api import InternalAPI, BookNotFound, BookAlreadyOnTable
from pprint import pp
class UserInteractions:
    def __init__(self):
        self.book_criteria = {
            'author': '',
            'categories': '',
            'book_type': '',
            'lexile_min': '',
            'lexile_max': '',
            'book_num': '',
            'random_choice': False,
            'filtered_choice': False
        }
        self.internal_api = InternalAPI()

    def welcome(self):
        while True:
            user_choice = input("""Welcome to {APP NAME}!\nWhat would you like to do?
            If you would like to search for a book, enter 'search'.
            If you would like to generate a random book, enter 'random'.
            If you would like to look at your to-read list, enter 'to-read'.
            If you would like to look at your read list, enter 'read'.
            To exit the program, enter 'exit'.\nPlease enter: """)
            lowercase_choice = user_choice.lower()
            if lowercase_choice == 'search':
                self.filtered_choice()
                break
            elif lowercase_choice == 'random':
                self.random_choice()
                break
            elif lowercase_choice == 'to-read':
                self.view_to_read_list()
                break
            elif lowercase_choice == 'read':
                self.view_read_list()
                break
            elif lowercase_choice == 'exit':
                print('Goodbye!')
                break
            else:
                print('Invalid choice. Please try again.')

    def filtered_choice(self):
        while True:
            try:
                number_of_books = int(
                    input('How many books would you like to search for? (Enter a number between 1 and 10) '))
                if number_of_books < 1 or number_of_books > 10:
                    raise ValueError('Invalid input. Please enter a number between 1 and 10.')
                break
            except ValueError as e:
                print(str(e))
                continue

        self.book_criteria['book_num'] = number_of_books
        self.book_criteria['filtered_choice'] = True

        print('What would you like to search by? (Press enter if you would like to leave blank):')
        author = input('Author: ')
        genre = input('Genre: ')
        fiction = input('Fiction or Non-Fiction: ')
        lexile_min = input('Lexile min: ')
        lexile_max = input('Lexile max: ')

        self.book_criteria['author'] = author
        self.book_criteria['categories'] = genre
        self.book_criteria['book_type'] = fiction
        self.book_criteria['lexile_min'] = lexile_min
        self.book_criteria['lexile_max'] = lexile_max

        pp(self.internal_api.search_book_suggestions(user_input = self.book_criteria))

    def random_choice(self):
        chosen_genre = input('What genre are you looking for? ')

        self.book_criteria['categories'] = chosen_genre
        self.book_criteria['random_choice'] = True

        pp(self.internal_api.random_book_suggestion(user_input = self.book_criteria))

    def add_book_to_list_or_not(self):
        while True:
            add_to_list_or_not = input('Would you like to add this book to a list? (y/n): ')
            if add_to_list_or_not.lower() == 'y':
                return True
            elif add_to_list_or_not.lower() == 'n':
                return False
            else:
                print('Invalid choice. Please try again.')

    def star_rating(self):
        user_rating = input('How many stars would you like to rate this book? (Enter a number between 1 and 5)')
        return int(user_rating)

    def view_to_read_list(self):
        return True

    def view_read_list(self):
        return True

    def regenerate_results(self):
        while True:
            happy_with_results = input('Would you like to generate different books? (y/n)')
            if happy_with_results.lower() == 'y':
                return True
            elif happy_with_results.lower() == 'n':
                return False
            else:
                    print('Invalid choice. Please try again.')


user1 = UserInteractions()
user1.welcome()
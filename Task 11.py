import json

class LibraryItem:
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id

    def display_info(self):
        pass


class Book(LibraryItem):
    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)
        self.author = author

    def display_info(self):
        print(f"Book Title: {self.title}")
        print(f"Item ID: {self.item_id}")
        print(f"Author: {self.author}\n")


class Magazine(LibraryItem):
    def __init__(self, title, item_id, publisher):
        super().__init__(title, item_id)
        self.publisher = publisher

    def display_info(self):
        print(f"Magazine Title: {self.title}")
        print(f"Item ID: {self.item_id}")
        print(f"Publisher: {self.publisher}\n")


class CD(LibraryItem):
    def __init__(self, title, item_id, artist):
        super().__init__(title, item_id)
        self.artist = artist

    def display_info(self):
        print(f"CD Title: {self.title}")
        print(f"Item ID: {self.item_id}")
        print(f"Artist: {self.artist}\n")


class User:
    def __init__(self, user_id, name, borrow_history=None):
        self.user_id = user_id
        self.name = name
        self.borrow_history = borrow_history if borrow_history is not None else []

    def borrow_item(self, item):
        self.borrow_history.append({'title': item.title, 'item_id': item.item_id})
        print(f"{self.name} has borrowed {item.title}.\n")

    def return_item(self, item_id):
        for item in self.borrow_history:
            if item['item_id'] == item_id:
                self.borrow_history.remove(item)
                print(f"{self.name} has returned {item['title']}.\n")
                return
        print(f"{self.name} has not borrowed this item.\n")

    def display_borrow_history(self):
        print(f"All items borrowed by {self.name}:")
        for item in self.borrow_history:
            print(f"Title: {item['title']}, Item ID: {item['item_id']}")


def load_from_json(filename):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        return None


def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


if __name__ == '__main__':
    while True:
        data = load_from_json('library_data.json')
        books_data = data['books']
        magazines_data = data['magazines']
        cds_data = data['cds']

        books = [Book(book['title'], book['id'], book['author']) for book in books_data]
        magazines = [Magazine(magazine['title'], magazine['id'], magazine['publisher']) for magazine in magazines_data]
        cds = [CD(cd['title'], cd['id'], cd['artist']) for cd in cds_data]

        try:
            users = load_from_json('user_data.json')
        except FileNotFoundError:
            users = []
        print("Welcome to the Library")
        user_id = input("Enter user ID: ")

        existing_user = next((user for user in users if user['user_id'] == user_id), None)

        if existing_user:
            user1 = User(existing_user['user_id'], existing_user['name'], existing_user['borrow_history'])
            print(f"Welcome back, {user1.name}!\n")

            action = input("Enter 'B' for borrowing or 'R' for returning: ").upper()

            if action == 'B':
                item_type = input("Enter '1' for a book, '2' for a magazine, or '3' for a CD: ")

                if item_type == '1':
                    print("Available books:")
                    for book in books:
                        book.display_info()
                    print("\n")
                    chosen_book_id = input("Enter the ID of the book you want to borrow: ")
                    chosen_book = next((book for book in books if book.item_id == chosen_book_id), None)
                    if chosen_book:
                        user1.borrow_item(chosen_book)
                    else:
                        print("Invalid book ID.\n")

                elif item_type == '2':
                    print("Available magazines:")
                    for magazine in magazines:
                        magazine.display_info()
                    chosen_magazine_id = input("Enter the ID of the magazine you want to borrow: ")
                    chosen_magazine = next((magazine for magazine in magazines if magazine.item_id == chosen_magazine_id), None)
                    if chosen_magazine:
                        user1.borrow_item(chosen_magazine)
                    else:
                        print("Invalid magazine ID.\n")

                elif item_type == '3':
                    print("Available CDs:")
                    for cd in cds:
                        cd.display_info()
                    chosen_cd_id = input("Enter the ID of the CD you want to borrow: ")
                    chosen_cd = next((cd for cd in cds if cd.item_id == chosen_cd_id), None)
                    if chosen_cd:
                        user1.borrow_item(chosen_cd)
                    else:
                        print("Invalid CD ID.\n")

                else:
                    print("Invalid choice.\n")

            elif action == 'R':
                if user1.borrow_history:
                    print(f"Borrowing history for {user1.name}:")
                    user1.display_borrow_history()
                    return_item_id = input("Enter the ID of the item you want to return: ")
                    user1.return_item(return_item_id)
                else:
                    print(f"{user1.name} has not borrowed anything.\n")

            else:
                print("Invalid choice.\n")

            if existing_user:
                user_data = {'user_id': user1.user_id, 'name': user1.name, 'borrow_history': user1.borrow_history}
                users = [user_data if user['user_id'] == user_id else user for user in users]
            else:
                user_data = {'user_id': user_id, 'name': user1.name, 'borrow_history': user1.borrow_history}
                users.append(user_data)

            save_to_json(users, 'user_data.json')

        else:
            print("User not found.\n")

            item_type = input("Enter '1' for a book, '2' for a magazine, or '3' for a CD: ")

            if item_type == '1':
                print("Available books:")
                for book in books:
                    book.display_info()
                chosen_book_id = input("Enter the ID of the book you want to borrow: ")
                chosen_book = next((book for book in books if book.item_id == chosen_book_id), None)
                if chosen_book:
                    user1 = User(user_id, "User")
                    user1.borrow_item(chosen_book)
                else:
                    print("Invalid book ID.\n")

            elif item_type == '2':
                print("Available magazines:")
                for magazine in magazines:
                    magazine.display_info()
                chosen_magazine_id = input("Enter the ID of the magazine you want to borrow: ")
                chosen_magazine = next((magazine for magazine in magazines if magazine.item_id == chosen_magazine_id), None)
                if chosen_magazine:
                    user1 = User(user_id, "New User")
                    user1.borrow_item(chosen_magazine)
                else:
                    print("Invalid magazine ID.\n")

            elif item_type == '3':
                print("Available CDs:")
                for cd in cds:
                    cd.display_info()
                chosen_cd_id = input("Enter the ID of the CD you want to borrow: ")
                chosen_cd = next((cd for cd in cds if cd.item_id == chosen_cd_id), None)
                if chosen_cd:
                    user1 = User(user_id, "New User")
                    user1.borrow_item(chosen_cd)
                else:
                    print("Invalid CD ID.\n")

            else:
                print("Invalid choice.")

            if user1:
                user_data = {'user_id': user1.user_id, 'name': user1.name, 'borrow_history': user1.borrow_history}
                users.append(user_data)

            save_to_json(users, 'user_data.json')

        choice = input("Do you want to continue? (y/n): ").lower()
        if choice != 'y':
            break

    save_to_json(users, 'user_data.json')

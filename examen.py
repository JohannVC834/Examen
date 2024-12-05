class User:
    def __init__(self, nombre, user_id, cuenta):
        # Encapsulamiento
        self.__nombre = nombre
        self.__id = user_id
        self.__cuenta = cuenta

 
    def get_nombre(self):
        return self.__nombre

    def get_id(self):
        return self.__id

    def search_author(self, author_name, catalogue):
        
        print(f"Buscando autor {author_name} en el catálogo...")
        return catalogue.check_available_books(author_name)


class Catalogue:
    def __init__(self):
        # Encapsulamiento
        self.__books = {
            "El Quijote": "Miguel de Cervantes",
            "Cien Años de Soledad": "Gabriel García Márquez",
            "1984": "George Orwell"
        }

    def check_available_books(self, author_name):
        # Polimorfismo
        try:  # Manejo de errores
            available_books = [book for book, author in self.__books.items() if author == author_name]
            if available_books:
                print(f"Libros disponibles de {author_name}: {available_books}")
                return available_books
            else:
                print(f"No hay libros disponibles de {author_name}")
                return []
        except Exception as e:  # Manejo de errores con try-catch
            print(f"Error al buscar libros: {e}")
            return []

    def print_receipt(self, user, book_name):
        print(f"Recibo: {user.get_nombre()} ha prestado el libro '{book_name}'.")

# Herencia
class Loan:
    def __init__(self):
        self.__loans = {}  

    def check_penalties(self, user_id):
        # Polimorfismo
        try:  # Manejo de errores
            print(f"Revisando penalizaciones para el usuario {user_id}...")
            
            return False
        except Exception as e:
            print(f"Error al revisar penalizaciones: {e}")
            return True

    def update_account(self, user_id, book_name):
        if user_id not in self.__loans:
            self.__loans[user_id] = []
        self.__loans[user_id].append(book_name)
        print(f"Cuenta del usuario {user_id} actualizada con el libro '{book_name}'.")


class Books:
    def __init__(self, nombre_libro, id_libro):
        # Encapsulamiento
        self.__nombre_libro = nombre_libro
        self.__id_libro = id_libro
        self.__is_checked_out = False

    def check_out(self, user, loan):
        # Manejo de errores
        try:
            if not self.__is_checked_out:
                self.__is_checked_out = True
                loan.update_account(user.get_id(), self.__nombre_libro)
                print(f"El libro '{self.__nombre_libro}' ha sido prestado a {user.get_nombre()}.")
            else:
                print(f"El libro '{self.__nombre_libro}' no está disponible.")
        except Exception as e:
            print(f"Error al realizar el préstamo: {e}")

    def update_account(self, user):
        print(f"Cuenta del usuario {user.get_nombre()} actualizada para el libro '{self.__nombre_libro}'.")


def main():
    try:  # Manejo de errores 
        
        user1 = User("Juan", 1, "juan123")
        
       
        catalogue = Catalogue()
        
        
        loan = Loan()
        
       
        author_name = "Miguel de Cervantes"
        available_books = user1.search_author(author_name, catalogue)
        
        if available_books:
            
            book_name = available_books[0]
            print(f"Libro seleccionado: {book_name}")
            
            
            book = Books(book_name, 101)
            
            
            if not loan.check_penalties(user1.get_id()):
                book.check_out(user1, loan)
                catalogue.print_receipt(user1, book_name)
            else:
                print("No puedes pedir prestado un libro debido a penalizaciones.")
        else:
            print(f"No hay libros disponibles del autor {author_name}.")
    except Exception as e:
        # Manejo de errores 
        print(f"Se produjo un error en el programa principal: {e}")

if __name__ == "__main__":
    main()

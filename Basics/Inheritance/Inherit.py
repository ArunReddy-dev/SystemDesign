from Dog import Dog
class Inherit:
    def main(self):
        my_dog = Dog()
        my_dog.eat()  # Inherited method
        my_dog.bark()  # Dog's own method

if __name__ == "__main__":
    inherit = Inherit()
    inherit.main()  
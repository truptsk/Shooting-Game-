import random

class ShootingGame:
    def __init__(self):
        self.guns = ['Pistol', 'Shotgun', 'Sniper']
        self.animals = {
            'Deer': {'points': 10},
            'Bear': {'points': 20},
            'Rabbit': {'points': 5}
        }
        self.points = 0

    def start_game(self):
        print("Welcome to the Shooting Game!")
        print("Choose your gun:")
        self.display_guns()

        selected_gun = input("Enter the number of the gun you want to use: ")
        if selected_gun.isdigit() and 1 <= int(selected_gun) <= len(self.guns):
            gun_choice = self.guns[int(selected_gun) - 1]
            print(f"You selected {gun_choice}!")

            self.shoot_animals(gun_choice)
            self.display_result()
        else:
            print("Invalid input. Please choose a valid gun.")

    def display_guns(self):
        for i, gun in enumerate(self.guns, start=1):
            print(f"{i}. {gun}")

    def shoot_animals(self, gun):
        print("\nGet ready to shoot!")

        for _ in range(5):  # Shooting 5 animals
            animal = random.choice(list(self.animals.keys()))
            print(f"A wild {animal} appears!")

            shot = input("Shoot? (yes/no): ").lower()
            if shot == 'yes':
                points_earned = self.animals[animal]['points']
                print(f"You shot and killed the {animal}! +{points_earned} points")
                self.points += points_earned
            else:
                print(f"You missed the {animal}. Try again!")

            print()

    def display_result(self):
        print("\nGame Over!")
        print(f"You earned {self.points} points.")

if __name__ == "__main__":
    game = ShootingGame()
    game.start_game()

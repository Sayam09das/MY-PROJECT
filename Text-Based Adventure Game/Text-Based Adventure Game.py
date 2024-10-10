import time
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.experience = 0

    def is_alive(self):
        return self.health > 0

    def heal(self):
        self.health = 100
        print(f"{self.name} rests and regains full health!")

class Game:
    def __init__(self):
        self.player = None
        self.locations = {}
        self.current_location = None
        self.enemies = ["Goblin", "Skeleton", "Troll", "Dragon"]
        self.items = ["Potion", "Gold", "Sword", "Shield", "Map"]
        self.create_locations()

    def create_locations(self):
        self.locations["village"] = Location(
            "You are in a small village. There are shops and people around.",
            {
                "explore": "Explore the village.",
                "rest": "Rest at the inn.",
                "dungeon": "Go to the dark dungeon."
            },
            {}
        )

        self.locations["dungeon"] = Location(
            "You enter a dark dungeon filled with monsters.",
            {
                "fight": "Fight a monster!",
                "explore": "Search for treasure.",
                "village": "Go back to the village."
            },
            {}
        )

        self.locations["forest"] = Location(
            "You are in a dense forest. It feels eerie here.",
            {
                "explore": "Search the forest.",
                "dungeon": "Go to the dungeon.",
                "village": "Return to the village."
            },
            {}
        )

        self.locations["castle"] = Location(
            "You stand before a grand castle. The gates are locked.",
            {
                "explore": "Look around the castle.",
                "forest": "Head back to the forest.",
                "village": "Return to the village."
            },
            {}
        )

        self.locations["treasure_room"] = Location(
            "You find yourself in a room filled with treasures!",
            {
                "take": "Take some treasure.",
                "dungeon": "Return to the dungeon."
            },
            {"gold": 100, "sword": 1}
        )

    def start_game(self):
        print("Welcome to the Adventure Game!")
        player_name = input("Enter your name: ")
        self.player = Player(player_name)
        self.current_location = self.locations["village"]
        print(f"Hello, {self.player.name}! Your adventure begins now.")
        self.main_loop()

    def main_loop(self):
        while self.player.is_alive():
            self.describe_location()
            action = input("What do you want to do? ").lower()
            self.perform_action(action)
        print("Game Over! You have been defeated.")

    def describe_location(self):
        print(self.current_location.description)
        print("Available actions: " + ", ".join(self.current_location.actions.keys()))

    def perform_action(self, action):
        if action in self.current_location.actions:
            if action == "explore":
                self.explore()
            elif action == "rest":
                self.player.heal()
            elif action == "dungeon":
                self.current_location = self.locations["dungeon"]
            elif action == "fight":
                self.fight()
            elif action == "forest":
                self.current_location = self.locations["forest"]
            elif action == "castle":
                self.current_location = self.locations["castle"]
            elif action == "take":
                self.take_treasure()
            else:
                print("Action not recognized.")
        else:
            print("Invalid action.")

    def explore(self):
        if self.current_location == self.locations["village"]:
            print("You find a mysterious map.")
            self.player.inventory.append("Map")
            print("You have obtained a Map.")
        elif self.current_location == self.locations["dungeon"]:
            treasure = random.choice(self.items)
            print(f"You found a treasure: {treasure}!")
            self.player.inventory.append(treasure)
        elif self.current_location == self.locations["forest"]:
            print("You find a hidden path leading to a castle.")
            self.current_location = self.locations["castle"]
        elif self.current_location == self.locations["castle"]:
            print("You discover a locked door. It seems to lead to a treasure room.")
            self.current_location.actions["treasure_room"] = "Go to the treasure room."
        elif self.current_location == self.locations["treasure_room"]:
            print("You have already been here.")
        else:
            print("You cannot explore here.")

    def take_treasure(self):
        if "gold" in self.current_location.items:
            print("You take some gold!")
            self.player.inventory.append("Gold")
            self.current_location.items.remove("gold")
        if "sword" in self.current_location.items:
            print("You take the sword!")
            self.player.inventory.append("Sword")
            self.current_location.items.remove("sword")

    def fight(self):
        if self.current_location == self.locations["dungeon"]:
            enemy = random.choice(self.enemies)
            print(f"A wild {enemy} appears!")
            while self.player.is_alive():
                action = input("Do you want to (attack) or (run)? ").lower()
                if action == "attack":
                    damage = random.randint(10, 30)
                    self.player.health -= damage
                    print(f"You attacked the {enemy} and took {damage} damage!")
                    if not self.player.is_alive():
                        print("You have been defeated!")
                        break
                    else:
                        print(f"You have {self.player.health} health left.")
                        self.player.experience += 20  
                        print(f"You gained 20 experience! Total experience: {self.player.experience}")
                elif action == "run":
                    print("You ran away safely!")
                    break
                else:
                    print("Invalid action.")
        else:
            print("You can't fight here!")

class Location:
    def __init__(self, description, actions, items):
        self.description = description
        self.actions = actions
        self.items = items

if __name__ == "__main__":
    game = Game()
    game.start_game()

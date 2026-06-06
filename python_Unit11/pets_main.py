import pets

def main():

    pet = pets.Pet("Retriever", "Happy", 45, "Gold", 3)
    print(pet.get_name())
    print(pet.get_weight())
    pet.feed(1800)
    print(pet.get_weight())
    pet.walk(1.5)
    print(pet.get_weight())


if __name__ == "__main__":
    main()

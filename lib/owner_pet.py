class Pet:
   
    pass

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
             return self._pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("The pet must be an instance of the Pet class.")
        pet.owner = self
        self._pets.append(pet)

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)
    
    pass
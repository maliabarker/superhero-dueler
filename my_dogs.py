from dog import Dog

bert = Dog("Bert", "Shepard")
my_dog = Dog("Rex", "SuperDog")
my_other_dog = Dog("Annie", "SuperDog")




print(my_other_dog.name)

print(my_dog)
print(my_dog.name)
print(my_dog.breed)
print(bert.breed)
my_dog.bark()
bert.bark()
my_other_dog.sit()
bert.roll_over()
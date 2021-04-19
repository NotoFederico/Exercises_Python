from exercise_48 import Person

federico = Person("Federico Noto")
print(federico)
for key in federico.__dict__:
    print(key,'=>',getattr(federico, key))

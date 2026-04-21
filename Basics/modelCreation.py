# Creating a basic model with Pydantic

from pydantic import BaseModel, ValidationError

class Person(BaseModel):
    first_name: str
    last_name: str
    age: int

    # Pydantic Models can hold its own methods
    @property
    def display_name(self):
        return f'{self.first_name} {self.last_name}'

if __name__ == "__main__": 
    p = Person(first_name='Theo', last_name='Cat', age=4)
    # String representation and Wrapper
    # print(str(p))
    print(repr(p))

    # Inspecting model fields with .model_fields
    # Used to be able to check via a model instance, however now you must pass in model
    # Utilizing the variable to check this is deprecated and will be removed in Pydantic V3.0
    print(Person.model_fields)

    # Demonstrating the validation error present in Pydantics model when creating new instances
    # Error shows all the fields that are missing, in this case first_name and age
    try:
        Person(last_name='Clark')
    except ValidationError as ex:
        print(ex)

    # Showing how to call the property / method
    print(p.display_name)

    # Can treat model like an OOP class
    print(p.first_name)
    print(p.age)
    p.age = 5
    print(str(p))

    # Type Creation fails due to four being a str
    try: 
        Person(first_name = 'Theo', last_name='Cat', age='four')
    except ValidationError as ex:
        print(ex)

    # However currently we can change it be invalid outside of instantiation
    # This will be fixed in further lectures
    # Validation happens when the data is loaded into the Pydantic Model
    p.age = 'five'
    print(str(p))
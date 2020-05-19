from faker import Faker

class BaseContact:
    def __init__(self,name:str,last_name:str,phone:int,email:str):
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.email = email
    def __str__(self):
        return f'Name: {self.name} Last Name: {self.last_name} Email: {self.email}'

    def contact(self):
        return f'I dial the number: {self.phone} and call {self.name} {self.last_name}'

    @property
    def label_lenght(self):
        return len(f"{self.name} {self.last_name}")


class BusinessCard(BaseContact):
    def __init__(self,occupation:str,company_name:str,business_phone:int,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.occupation = occupation
        self.company_name = company_name
        self.business_phone = business_phone

    def contact(self):
        return f'I dial the number: {self.business_phone} and call {self.name} {self.last_name}'


def create_contacts(card_type,quantity:int):
    faker = Faker()
    person_list = []
    for number in range(0,quantity):
        if card_type == BaseContact:
            person_list.append(BaseContact(faker.first_name(),faker.last_name(),faker.phone_number(),faker.email()))
        else:
            person_list.append(BusinessCard(faker.job(),faker.company(),faker.phone_number(),
                                faker.first_name(),faker.last_name(),faker.phone_number(),faker.email()))

    return person_list



def main():

    base_contacts = create_contacts(BaseContact,5)
    businnes_contacts = create_contacts(BusinessCard,3)

    print('PODSTAWOWE\n')
    for person in base_contacts:
        print(person)

    print('\nBIZNESOWE')

    for person in businnes_contacts:
        print(person)

    #sortowanie
    sorted_by_name = sorted(base_contacts, key=lambda human: human.name)
    sorted_by_lastname = sorted(businnes_contacts, key=lambda human: human.last_name)
    sorted_by_email = sorted(base_contacts, key=lambda human: human.email)

    print('\nSORTED PERSON BY NAME\n')
    for person_name in sorted_by_name:
        print(person_name)
    print('\nSORTED PERSON BY LAST NAME\n')
    for person_lastname in sorted_by_lastname:
        print(person_lastname)
    print('\nSORTED BY EMAIL\n')
    for person_email in sorted_by_email:
        print(person_email)

    #dlugosc pelnych imion w podstawowych
    for base in base_contacts:
        print(base.label_lenght)

    #dlugosc pelnych imion w biznesowych
    for businnes in businnes_contacts:
        print(businnes.label_lenght)

    #metoda contact
    print(base_contacts[2].contact())
    print(businnes_contacts[1].contact())




if __name__ == '__main__':
    main()




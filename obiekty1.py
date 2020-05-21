from faker import Faker


class BaseContact:
    def __init__(self, name: str, last_name: str, phone: int, email: str):
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f'Name: {self.name} Last Name: {self.last_name} Email: {self.email}'

    def contact(self):
        print(f'I dial the number: {self.phone} and call {self.name} {self.last_name}')

    @property
    def label_lenght(self):
        return len(f"{self.name} {self.last_name}")


class BusinessCard(BaseContact):
    def __init__(self, name: str, last_name: str, phone: int, email: str, occupation: str, company_name: str,
                 business_phone: int):
        super().__init__(name, last_name, phone, email)
        self.occupation = occupation
        self.company_name = company_name
        self.business_phone = business_phone

    def contact(self):
        return f'I dial the number: {self.business_phone} and call {self.name} {self.last_name}'


def create_contacts(card_type, quantity: int):
    faker = Faker()
    person_list = []
    for number in range(quantity):
        if card_type == BusinessCard:
            person_list.append(BusinessCard(name=faker.first_name(),
                                            last_name=faker.last_name(),
                                            phone=faker.phone_number(),
                                            email=faker.email(),
                                            occupation=faker.job(),
                                            company_name=faker.company(),
                                            business_phone=faker.phone_number(),
                                            ))
        elif card_type == BaseContact:
            person_list.append(BaseContact(name=faker.first_name(),
                                           last_name=faker.last_name(),
                                           phone=faker.phone_number(),
                                           email=faker.email()))
        else:
            raise TypeError

    return person_list


def main():
    base_contacts = create_contacts(BaseContact, 5)
    businnes_contacts = create_contacts(BusinessCard, 3)
    contacts_all = base_contacts + businnes_contacts

    print("ALL CONTACTS")

    for person in contacts_all:
        print(person)

    # SORT
    sorted_by_name = sorted(contacts_all, key=lambda human: human.name)
    sorted_by_lastname = sorted(contacts_all, key=lambda human: human.last_name)
    sorted_by_email = sorted(contacts_all, key=lambda human: human.email)

    print('SORTED PERSON BY NAME')
    for person_name in sorted_by_name:
        print(person_name)
    print('SORTED PERSON BY LAST NAME')
    for person_lastname in sorted_by_lastname:
        print(person_lastname)
    print('SORTED BY EMAIL')
    for person_email in sorted_by_email:
        print(person_email)

    # FULL NAMES LEN
    for person in contacts_all:
        print(person.label_lenght)

    # CONTACT
    print(contacts_all[2].contact())


if __name__ == '__main__':
    main()

from faker import Faker


AMOUNT = 200

Faker.seed(0)
fake = Faker()

placelists = []
for i in range(AMOUNT):
    placelists.append({
        'public_id': i,
        'name': fake.sentence(nb_words=4)[:-1],
        'user': f'@{fake.simple_profile()["username"]}'
    })

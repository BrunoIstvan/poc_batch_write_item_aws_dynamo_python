import boto3
from faker import Faker

fake = Faker('pt_BR')

resource = boto3.resource('dynamodb')

table = resource.Table('User')

with table.batch_writer() as batch:
    for i in range(500):

        item = {
                'cpf': fake.ssn(),
                'state': fake.estado_sigla(),
                'actived': False,
                'city': fake.city(),
                'email': fake.email(),
                'full_name': fake.name()
            }

        print(item)

        batch.put_item(Item=item)


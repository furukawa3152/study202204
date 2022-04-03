import pandas as pd
from faker import Faker
import random
fake = Faker("ja_JP")
#https://faker.readthedocs.io/en/master/locales/ja_JP.html

def make_fake_list(index_count):
    list = []
    for i in range(index_count):
        row = [fake.name(), fake.address(), fake.town(), fake.email()]
        list.append(row)
    df = pd.DataFrame(data=list, columns=["name", "address", "town", "email"])
    return (df)


if __name__ == '__main__':
    for i in range(1, 31):
        num = random.randint(1,1000)
        df = make_fake_list(num)
        name = fake.company()
        df.to_csv(f"fake_data\{name}.csv", encoding="shift_jis", index=False)

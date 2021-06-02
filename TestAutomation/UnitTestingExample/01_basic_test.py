user1 = {
    "id": 2,
    "first_name": "Alin",
    "last_name": "Popescu",
    "age": 29
}

user2 = {
    "id": 3,
    "first_name": "Roxana",
    "last_name": "Marin",
    "age": 29
}


def test_not_same_users():
    print("\nRunning test_not_same_users...")
    assert user1 != user2


def test_same_age():
    print("\nRunning test_same_age...")
    assert user1.get("age", -1) == user2.get("age", -1)


# will fail
def test_same_age2():
    print("\nRunning test_same_age...")
    assert user1.get("age", -1) != user2.get("age", -1)

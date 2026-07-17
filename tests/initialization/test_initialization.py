from utilities.api_client import post


def test_initialize():

    post("/add",{
        "a":10,
        "b":20
    })

    post("/subtract",{
        "a":50,
        "b":25
    })

    post("/multiply",{
        "a":10,
        "b":5
    })

    post("/divide",{
        "a":100,
        "b":20
    })
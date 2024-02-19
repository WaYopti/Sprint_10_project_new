body_create = {
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}

header_delete = {
    "Cookie": "token=abc123"
}

body_auth = {
    "username" : "admin",
    "password" : "password123"
}
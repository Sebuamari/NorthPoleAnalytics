def serialize_kids(kids):
    return {
        "kids": [
            {
                "name": kid.name,
                "gift": kid.gift.name,
                "niceness_coefficient": kid.niceness_coefficient,
                # "santas_list": {
                #     "name": kid.santas_list.name
                # } if kid.santas_list else None
            } for kid in kids
        ]
    }
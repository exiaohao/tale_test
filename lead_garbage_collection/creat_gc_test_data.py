phone_number_format = "13939{suffix}"
    for i in range(100000, 100020):
        phone_number = phone_number_format.format(suffix=i)
        taomi_tags = TaomiTag(phone_number=phone_number,
                              taomi_tag=TaomiStatus.I,
                              account_id=88001)
        taomi_tags.set_status()


garbage = {}
    garbage['garbage'] = {
        '1':{
            "follow_time": 12345678,
            "current_status_change_time": 12345999,
            "current_system_tag_id": 10,
        }
    }

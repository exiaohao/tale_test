from init import app, mysql_db as db
from models.lead_model import Lead, LeadSeaType
from models.customer_model import Customer


def main():
    max_id = Lead.query.filter_by(sea_type=LeadSeaType.TAOMI_PUBLIC).order_by(Lead.id.desc()).first().id
    do_clean(Lead, max_id)

    max_id = Customer.query.order_by(Customer.id.desc()).first().id
    do_clean(Customer, max_id)


def do_clean(model, max_id):
    print(max_id)

    count = 0
    i = max_id
    j = 1000
    while i >= 1:
        objs = model.query.filter(model.id.in_(range(i - j, i + 1)))
        for obj in objs:
            if obj.sea_type == LeadSeaType.TAOMI_PRIVATE:
                continue
            if obj.short_name and obj.full_name:
                continue

            obj.short_name, obj.full_name = get_clean_short_full_name(obj)

            db.session.add(obj)

            count += 1
            if count % 500 == 0:
                db.session.commit()

            if count % 2000 == 0:
                print('count: {}'.format(count))
                print('current object.id: {}'.format(obj.id))

        i -= j
        if i <= j:
            i = j + 1

    db.session.commit()

    print(count)
    print('Done.')


def get_clean_short_full_name(lead):  # 库中尚存在short_name为 '' 的线索
    short_name = lead.short_name
    full_name = lead.full_name
    if not short_name and full_name:
        short_name = full_name
    elif short_name and (not full_name or full_name == '未命名线索'):
        full_name = short_name
    return short_name, full_name


if __name__ == '__main__':
    with app.app_context():
        main()

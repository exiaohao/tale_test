from init import app, mysql_db as db
from models.customer_model import Customer, SeaType, CustomerAccount, SystemCustomerTag
from models.lead_model import Lead, LeadSeaType, LeadSource
from models.taomi_tag_model import TaomiStatus
from utils import get_current_timestamp


def copy_new_lead_from_customer(customer, customer_account):
    new_lead = Lead(customer_account.mobile)
    new_lead.full_name = customer.full_name
    new_lead.short_name = customer.short_name
    new_lead.sea_type = LeadSeaType.TAOMI_PRIVATE
    new_lead.relation_id = customer.relation_id
    new_lead.lead_source = LeadSource.TAOMI_DEPT
    new_lead.lead_status = TaomiStatus.L

    new_lead.city = customer_account.city
    new_lead.city_cn = customer_account.city_cn
    new_lead.main_category = customer_account.main_category
    new_lead.main_category_cn = customer_account.main_category_cn
    new_lead.top_category = customer_account.top_category
    new_lead.top_category_cn = customer_account.top_category_cn

    new_lead.copy_time = get_current_timestamp()
    new_lead.is_frozen = 1

    db.session.add(new_lead)
    db.session.commit()
    new_lead.build_search()

    return new_lead


with app.app_context():
    customers = Customer.query.filter_by(sea_type=SeaType.PRIVATE).filter(Customer.system_tag_id.in_([SystemCustomerTag.H, SystemCustomerTag.O]))

    for customer in customers:
        ca = CustomerAccount.query.filter_by(customer_id=customer.id, account_type=0).first()

        if ca:
            existed_lead = Lead.query.filter_by(mobile=ca.mobile, sea_type=LeadSeaType.TAOMI_PRIVATE, is_frozen=0).first()

            if not existed_lead:
                new_lead = copy_new_lead_from_customer(customer, ca)
                print(new_lead.id)

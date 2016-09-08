from init import app
from models.sale_maintainer_quota import SaleMaintainerQuota
from models.taomi_tag_model import TaomiTagMap
from libs.customer_maintainer_sea import MaintainerQuota
from libs.rpc import YaoguangRPC


with app.app_context():
    fields = [
        {
            'key': 'vip_expire_date',
            'name': 'VIP过期时间',
            'order': 0,
            'prefix': '',
            'scope': 'maintainer',
            'selections': [
                {
                    'id': [0, 4],
                    'name': '0-3',
                },
                {
                    'id': [4, 8],
                    'name': '4-7'
                },
                {
                    'id': [8, 16],
                    'name': '8-15',
                },
                {
                    'id': [16, 31],
                    'name': '16-30',
                },
                {
                    'id': [31, ],
                    'name': '30+',
                },
            ],
        },
        {
            'key': 'history_buy_ff',
            'name': '购买过FF产品',
            'order': 1,
            'prefix': '',
            'scope': 'maintainer',
            'selections': [
                {
                    'id': 'weiwoduzun',
                    'name': '唯我独尊',
                },
                {
                    'id': 'zhizunzhanwei',
                    'name': '至尊展位',
                },
                {
                    'id': 'shiwanhuoji',
                    'name': '十万火急',
                },
                {
                    'id': 'zhiding',
                    'name': '置顶',
                },
                {
                    'id': 'fengming',
                    'name': '凤鸣',
                },
                {
                    'id': 'tuijianzhanwei',
                    'name': '推荐展位',
                },
            ]
        },
        {
            'key': 'ff_expire_date',
            'name': 'FF到期时间',
            'order': 2,
            'prefix': '',
            'scope': 'maintainer',
            'selections': [
                {
                    'id': [0, 4],
                    'name': '0-3',
                },
                {
                    'id': [4, 8],
                    'name': '4-7'
                },
                {
                    'id': [8, 16],
                    'name': '8-15',
                },
                {
                    'id': [16, 31],
                    'name': '16-30',
                },
                {
                    'id': [31, ],
                    'name': '30+',
                },
            ]
        },
        {
            'key': 'vip_type',
            'name': 'VIP类型',
            'order': 3,
            'prefix': '',
            'scope': 'maintainer',
            'selections': [
                {
                    'id': '招聘',
                    'name': '招聘',
                },
                {
                    'id': '房产',
                    'name': '房产'
                },
                {
                    'id': '车辆',
                    'name': '车辆',
                },
                {
                    'id': '服务',
                    'name': '服务',
                },
                {
                    'id': '兼职',
                    'name': '兼职',
                },
                {
                    'id': '宠物',
                    'name': '宠物',
                },
            ]
        },
        {
            'key': 'channel_type',
            'name': '所属渠道',
            'order': 4,
            'prefix': '',
            'scope': 'maintainer',
            'selections': [
                {
                    'id': '1',
                    'name': '代理商',
                },
                {
                    'id': '2',
                    'name': '销售部'
                },
                {
                    'id': '3',
                    'name': '其他',
                },
            ]
        },
    ]

    _item_fields = ['key', 'name', 'order', 'prefix', 'scope', 'selections',]

    for _f in fields:
        taomi_tag_map = TaomiTagMap()
        for _if in _item_fields:
            setattr(taomi_tag_map, _if, _f[_if])

        taomi_tag_map.save()


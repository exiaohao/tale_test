if __name__ == '__main__':
    with app.app_context(), open('../test/test_phone_gc_data', 'r') as _f:
        dept_gc_rules = get_dept_gc_rules()
        for _line in _f.readlines():
            _line_data = _line.rstrip().split(',')

            garbage_taomi_phone_number(dept_gc_rules, _line_data[0])

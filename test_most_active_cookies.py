from most_active_cookie import MostActiveCookie

def test_sample_case_1():
    filename = "cookie_log.csv"
    request_date = "2018-12-09"

    try:
        with open(filename) as open_file:
            lines = open_file.readlines()[1:]
    except:
        print("\nFile not valid\n")
        exit()

    mac = MostActiveCookie()

    active_cookies_on_date = mac.filter_date(lines, request_date)

    output = mac.filter_most_counted(active_cookies_on_date)

    assert output == ["AtY0laUfhglK3lC7"]

def test_sample_case_2():
    filename = "cookie_log.csv"
    request_date = "2018-12-08"

    try:
        with open(filename) as open_file:
            lines = open_file.readlines()[1:]
    except:
        print("\nFile not valid\n")
        exit()

    mac = MostActiveCookie()

    active_cookies_on_date = mac.filter_date(lines, request_date)

    output = mac.filter_most_counted(active_cookies_on_date)

    assert output == ["SAZuXPGUrfbcn5UA", "4sMM2LxV07bPJzwf", "fbcn5UAVanZf6UtG"]

def test_empty_cookie_log_no_header():
    filename = "empty_cookie_log_no_header.csv"
    request_date = "2018-12-09"

    try:
        with open(filename) as open_file:
            lines = open_file.readlines()[1:]
    except:
        print("\nFile not valid\n")
        exit()

    mac = MostActiveCookie()

    active_cookies_on_date = mac.filter_date(lines, request_date)

    output = mac.filter_most_counted(active_cookies_on_date)

    assert output == []

def test_empty_cookie_log_with_header():
    filename = "empty_cookie_log_with_header.csv"
    request_date = "2018-12-09"

    try:
        with open(filename) as open_file:
            lines = open_file.readlines()[1:]
    except:
        print("\nFile not valid\n")
        exit()

    mac = MostActiveCookie()

    active_cookies_on_date = mac.filter_date(lines, request_date)

    output = mac.filter_most_counted(active_cookies_on_date)

    assert output == []

def test_custom_case_1():
    '''
    test case that tests multiple of same
    '''
    filename = "custom_cookie_log_1.csv"
    request_date = "2018-12-09"

    try:
        with open(filename) as open_file:
            lines = open_file.readlines()[1:]
    except:
        print("\nFile not valid\n")
        exit()

    mac = MostActiveCookie()

    active_cookies_on_date = mac.filter_date(lines, request_date)

    output = mac.filter_most_counted(active_cookies_on_date)

    assert output == ["AtY0laUfhglK3lC7"]


def test_custom_case_2():
    '''
    test case that tests multiple of same with mixed data
    '''
    filename = "custom_cookie_log_1.csv"
    request_date = "2018-12-08"

    try:
        with open(filename) as open_file:
            lines = open_file.readlines()[1:]
    except:
        print("\nFile not valid\n")
        exit()

    mac = MostActiveCookie()

    active_cookies_on_date = mac.filter_date(lines, request_date)

    output = mac.filter_most_counted(active_cookies_on_date)

    assert output == ["SAZuXPGUrfbcn5UA", "fbcn5UAVanZf6UtG"]

    
def test_custom_case_3():
    '''
    test case that tests when there is another day in which a cookie shows up the most
    '''
    filename = "custom_cookie_log_2.csv"
    request_date = "2018-12-08"

    try:
        with open(filename) as open_file:
            lines = open_file.readlines()[1:]
    except:
        print("\nFile not valid\n")
        exit()

    mac = MostActiveCookie()

    active_cookies_on_date = mac.filter_date(lines, request_date)

    output = mac.filter_most_counted(active_cookies_on_date)

    assert output == ["SAZuXPGUrfbcn5UA", "4sMM2LxV07bPJzwf", "fbcn5UAVanZf6UtG"]


if __name__ == "__main__":
    print("run using the command \"$ pytest test_most_active_cookies.py\"")
    pass
    


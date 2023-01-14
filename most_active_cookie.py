import sys

class MostActiveCookie:
        
    def filter_date(self, lines, queried_date):
        """
        filter_date takes a list of lines from a csv file of format "cookies,timestamp" and returns a list of only the cookies that were active on the requested date and a tuple of their count on that date with the most recent timestamp for that cookie

        returned list structure for clarification:
        [(cookie, (count, most recent timestamp))]
        str      int            str

        - parameter(s) -
        :lines: lines in the format of "cookies,timestamp"
        :queried_date: the date in question for most active cookies

        - returns - 
        :active_cookies_on_date (list): list of cookies with a tuple of count for the day and most recent timestamp for each
        """
        log_dictionary = {}
        for line in lines:

            try:
                cookie, datetime = line.split(",")
                date, time = datetime.split("T")
            except:
                print('\nCSV file not in correct format. \'cookie,timestamp\' and timestamp needs to be in format \'dateTtime\'\n') 
                exit()

            if date == queried_date:
                if cookie in log_dictionary:
                    # max ensures that the most recent timestamp is saved
                    log_dictionary[cookie] = (1 + log_dictionary[cookie][0], max(log_dictionary[cookie][1], time))
                else:
                    log_dictionary[cookie] = (1, time)

        # make dictionary iterable and sort primarily by most counts to least counts then by timestamp
        active_cookies_on_date = sorted(list(log_dictionary.items()), key = lambda x : (x[1][0], x[1][1]), reverse=True)

        return active_cookies_on_date



    def filter_most_counted(self, active_cookies_on_date):
        """
        filter_most_counted puts the cookies that were counted the most and their timestamp into a list and sorts them from most recent to furthest

        - parameter(s) -
        :active_cookies_on_date (list): list of cookies with a tuple of count for the day and most recent timestamp for each

        - returns - 
        :output (list = [str]): list of cookies that were the most active on the date

        """
        output = []
        if active_cookies_on_date:
            max_count = active_cookies_on_date[0][1][0]
            for cookie, (count, _) in active_cookies_on_date:
                if count != max_count:
                    break
                output.append(cookie)
        return output



if __name__ == "__main__":
    
    # Turn commandline arguments into the goat
    try:
        filename, request_date = sys.argv[1], sys.argv[3]
    except:
        print("\nIncorrect number of arguments\n")
        exit()
    
    # Open file and put each line as an element to a list/array
    try:
        with open(filename) as open_file:
            lines = open_file.readlines()[1:]
    except:
        print("\nFile not valid\n")
        exit()

    mac = MostActiveCookie()

    active_cookies_on_date = mac.filter_date(lines, request_date)

    output = mac.filter_most_counted(active_cookies_on_date)
    
    for cookie in output:
        print(cookie)
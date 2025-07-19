from problems.lib import cli, main_wrapper


YearMonth = tuple[int, int]


def next_month(year_month: YearMonth) -> tuple[YearMonth, int]:
    """Returns the first of the next month, and the number of days consumed."""
    year, month = year_month
    match month:
        # 30 days has Sept, April, June, Nov
        case 9 | 4 | 6 | 11:
            return (year, month + 1), 30
        case 2:
            if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
                return (year, month + 1), 29
            return (year, month + 1), 28
        case 12:
            return (year + 1, 1), 31
        case _:
            # all the rest have thirty-one
            return (year, month + 1), 31


@main_wrapper
def main():
    # How many Sundays fell on the first of the month during the
    # twentieth century (1 Jan 1901 -- 31 Dec 2000)
    # without datetime/calendar, otherwise boring
    # we simply advance one month at a time and count the number
    # of days. we only need to consider the 1st of each month.

    # let sunday be 0, monday 1 etc
    # as given, Jan 1 1900 is a Monday, this is our starting point
    year_month = (1900, 1)
    day_of_week = 1

    start_year_month = (1901, 1)
    end_year_month = (2000, 12)

    # advance to our start date, without counting sundays
    while year_month != start_year_month:
        year_month, days_advanced = next_month(year_month)
        day_of_week = (day_of_week + days_advanced) % 7

    # we are at the start date; count sundays until the end
    sundays_observed = 0
    while year_month != end_year_month:
        if day_of_week == 0:
            sundays_observed += 1
        year_month, days_advanced = next_month(year_month)
        day_of_week = (day_of_week + days_advanced) % 7

    return sundays_observed


if __name__ == "__main__":
    cli()

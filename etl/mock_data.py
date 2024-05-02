from datetime import datetime, timedelta


def generate_date_data(start_date, end_date, filename):
    current_date = start_date
    dates = []
    while current_date <= end_date:
        date_id = current_date.strftime('%Y%m%d')
        year = current_date.year
        month = current_date.month
        day = current_date.day
        quarter = (month - 1) // 3 + 1
        week = current_date.isocalendar()[1]
        dates.append(f"{date_id},{year},{month},{day},{quarter},{week}")
        current_date += timedelta(days=1)

    with open(filename, 'w') as file:
        for date in dates:
            file.write(date + '\n')


def main():
    start_date = datetime.now() - timedelta(days=5 * 365)  # 从今天起往回5年
    end_date = datetime.now()
    generate_date_data(start_date, end_date, 'dim_date.csv')


if __name__ == '__main__':
    main()

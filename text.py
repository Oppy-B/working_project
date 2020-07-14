from datetime import datetime


start_date = datetime.strptime('8/18/2008', "%m/%d/%Y")
end_date = datetime.strptime('9/26/2008', "%m/%d/%Y")

diff = (end_date-start_date).days
print(10 * diff)
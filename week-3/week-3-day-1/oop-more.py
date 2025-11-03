from datetime import date
class Book:
    def __init__(self, id, title, author, is_available = True):
        self.id = id
        self.title = title
        self.author = author
        self.is_available = is_available

    def mark_unavailable(self):
        if self.is_available == False:
            print("book is already taken")
        self.is_available = False 

    def mark_available(self):
        if self.is_available == True:
            print("book is available")
        self.is_available == True

class Member:
    def __init__(self, id, full_name, active_loans_count):
        self.id = id
        self.full_name = full_name
        self.active_loans_count = active_loans_count
        
    def loans_increment(self):
        active_loans_count += 1

    def loans_decrement(self):
        if active_loans_count > 0:
            active_loans_count -= 1
        else:
            print("can't ")

class Loan:
    def __init__(self, loan_id, book_id, member_id, open_date, return_date, status = 'Open'):
        self.loan_id = loan_id
        self.book_id = book_id
        self.member_id = member_id
        self.open_date = open_date
        self.return_date = return_date
        self.status =status

    def close(self):
        if self.status == 
        
        self.satus = 'Closed'
        self.return_date = date.today()


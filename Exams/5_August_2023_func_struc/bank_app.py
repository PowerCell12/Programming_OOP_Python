from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:

    def __init__(self, capacity):
        self.capacity = capacity
        self.loans = []
        self.clients = []



    def add_loan(self, loan_type: str):

        if loan_type != "StudentLoan" and loan_type != "MortgageLoan":
            raise Exception("Invalid loan type!")

        if loan_type == "StudentLoan":
            self.loans.append(StudentLoan())
        elif loan_type == "MortgageLoan":
            self.loans.append(MortgageLoan())

        return f"{loan_type} was successfully added."


    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):

        if client_type != "Student" and client_type != "Adult":
            raise Exception("Invalid client type!")

        if len(self.clients) + 1 > self.capacity: ## if error check
            return "Not enough bank capacity."


        if client_type == "Adult":
            self.clients.append(Adult(client_name, client_id, income))
        elif client_type == "Student":
            self.clients.append(Student(client_name, client_id, income))

        return f"{client_type} was successfully added."



    def grant_loan(self, loan_type: str, client_id: str):
        client = None
        loan = None

        for cl in self.clients:
            if cl.client_id == client_id:
                client = cl
                break

        for lo in self.loans:
            if lo.__class__.__name__ == loan_type:
                loan = lo
                break

        if client.__class__.__name__ == "Student" and loan.__class__.__name__ == "MortgageLoan":
            raise Exception("Inappropriate loan type!")

        if client.__class__.__name__ == "Adult" and loan.__class__.__name__ == "StudentLoan":
            raise Exception("Inappropriate loan type!")

        self.loans.remove(loan)
        client.loans.append(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."


    def remove_client(self, client_id: str):

        if client_id not in [h.client_id for h in self.clients]:
            raise Exception("No such client!")

        client = None
        for cl in self.clients:
            if cl.client_id == client_id:
                client = cl
                break

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."


    def increase_loan_interest(self, loan_type: str):

        count = 0
        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                loan.increase_interest_rate()
                count += 1

        return f"Successfully changed {count} loans."


    def increase_clients_interest(self, min_rate: float):
        count = 0

        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                count += 1

        return f"Number of clients affected: {count}."


    def get_statistics(self):
        return_list = []
        active = 0
        for cl in self.clients:
            if cl.loans:
                active += 1

        return_list.append(f"Active Clients: {len(self.clients)}")

        income_total = 0
        for cl in self.clients:
            income_total += cl.income

        return_list.append(f"Total Income: {income_total:.2f}") ## correct

        loans_count_granted_to_clients = 0
        granted_sum = 0

        for cl in self.clients:
            for loan in cl.loans:
                loans_count_granted_to_clients += 1
                granted_sum += loan.amount

        return_list.append(f"Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}")

        loans_count_not_granted = 0
        not_granted_sum = 0

        for loan in self.loans:
            loans_count_not_granted += 1
            not_granted_sum += loan.amount

        return_list.append(f"Available Loans: {loans_count_not_granted}, Total Sum: {not_granted_sum:.2f}")

        average = 0
        try:

            sum = 0
            for cl in self.clients:
                sum += cl.interest

            average = sum / len(self.clients)

        except ZeroDivisionError:
            average = 0


        return_list.append(f"Average Client Interest Rate: {average:.2f}")

        return "\n".join(return_list)
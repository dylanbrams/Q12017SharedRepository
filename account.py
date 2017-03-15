CONTINUE_PROCESSING_CHARACTERS = ['y', 'Y']

class Account(object):
    def __init__(self):
        self._interest = 0.001
        self._balance = 0


    def deposit(self, amount):
        """

        :return:
        """
        self._balance += amount
        return
    def calc_interest(self):
        """

        :return:
        """
        interest = self._interest*self._balance
        return(interest)

    def get_funds(self):
        """Returns account balance

        :return:
        >>> _balance = 104.45
        >>> get_funds()
        104.45
        """
        return self._balance

    def check_withdrawal(self, amount):
        if amount >= self._balance:
            return True
        else:
            return False

    def withdraw(self, amount):
        if not self.check_withdrawal(amount) == True:
            raise ValueError('Insufficient balance')
        else:
            self._balance -= amount
        return self._balance


#Main Definition
def main():
    checking = Account()
    savings = Account()
    run_again_flag = True
    while (run_again_flag == True):
        checking_or_savings = input('Operate on Checking (1, default) or Savings (2)?')
        if checking_or_savings == '2':
            current_account = savings
        else:
            current_account = checking
        print('Would you like to:')
        print('1: Check Account Balance')
        print('2: Deposit to your account')
        print('3: Withdraw from your account')
        print('4: Calculate interest on your account')
        action = input("? >>> ")
        if action == '2':
            deposit = input ('How much are you depositing?')
            current_account.deposit(float(deposit))
        elif action == '3':
            withdrawal = input ('How much are you withdrawing?')
            amount_withdrawn = current_account.withdraw(float(withdrawal))
            print ('Amount withdrawn: $' + str(amount_withdrawn))
        elif action == '4':
            interest = current_account.calc_interest()
            print ('Interest Gained: ' + str(interest))
        print ('Your Current Balance is : $' + str(current_account.get_funds()))
        run_again = input('Run Again.')
        if run_again.lower() not in CONTINUE_PROCESSING_CHARACTERS:
            run_again_flag = False
    return

#Main Call
if __name__ == '__main__':
    main()
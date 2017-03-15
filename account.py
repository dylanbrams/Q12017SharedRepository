class Account(object):
    def __init__(self):
        self._interest = 0.001
        self._balance = 0


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
    return

#Main Call
if __name__ == '__main__':
    main()
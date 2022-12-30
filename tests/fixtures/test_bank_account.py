import unittest
from my_project.fixtures.bank_account import BankAccount


def setUpModule():
    print('calling setUpModule')


def tearDownModule():
    print('calling tearDownModule')


class TestBankAccount(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('calling setUpClass')

    @classmethod
    def tearDownClass(cls) -> None:
        print('calling tearDownClass')

    def setUp(self) -> None:
        print('calling setUp')
        # Setup
        self.bank_account = BankAccount(10)

    def tearDown(self) -> None:
        print('calling tearDown')
        self.bank_account = None

    def test_deposit_success(self):
        # Setup
        # bank_account = BankAccount(0)

        # Action
        self.bank_account.deposit(10)

        # Assert
        self.assertEqual(20, self.bank_account.balance)

    def test_withdraw_success(self):
        # Setup
        # bank_account = BankAccount(10)

        # Action
        self.bank_account.withdraw(10)

        # Assert
        self.assertEqual(0, self.bank_account.balance)

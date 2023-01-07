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


    def tearDown(self) -> None:
        print('calling tearDown')


    def test_deposit_success(self):
        # Setup
        bank_account = BankAccount(10)

        # Action
        bank_account.deposit(10)

        # Assert
        self.assertEqual(20, bank_account.balance)

    def test_withdraw_success(self):
        # Setup
        bank_account = BankAccount(10)

        # Action
        bank_account.withdraw(10)

        # Assert
        self.assertEqual(0, bank_account.balance)

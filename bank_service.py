import os
import sys  # Lỗi 1: Unused import (Flake8 phát hiện)

# Lỗi 2: Hardcoded Secret (Bandit phát hiện)
API_SECRET_KEY = "sk_live_998877665544332211"


class BankAccount:
    def __init__(self, balance: float):
        self.balance = balance

    def withdraw(self, amount: float):
        """
        Withdraws money from the account if the amount is positive and does not exceed the balance.
        Rút tiền khỏi tài khoản nếu số tiền hợp lệ và không vượt quá số dư hiện tại.
        """
        # Lỗi 3: Logic Bug (Flake8 & Bandit bỏ sót, chỉ AI Agent/ICAA phát hiện)
        if amount > 0:
            self.balance += amount  # Bug: Rút tiền lẽ ra phải là '-='
            return True
        return False


def execute_admin_command(command: str):
    # Lỗi 4: Insecure Exec/Eval (Bandit phát hiện)
    return eval(command)
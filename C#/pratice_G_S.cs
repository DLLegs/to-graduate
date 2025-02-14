using System;

/*class 선언*/
class BankAccount
{
    public double Balance { get; private set; }

    /*생성자, initialBalance 값을 받아 초기값을 설정해줌*/
    public BankAccount(double initialBalance)
    {
        Balance = initialBalance;
    }

    /*해당 기능을 통해서만 금액 수정 가능*/
    public void Deposit(double amount)
    {
        Balance += amount;
    }
}
class Program
{
    public static void Main()
    {
        BankAccount account = new BankAccount(1000);

        Console.WriteLine($"잔액은: {account.Balance}");
        account.Deposit(500);
        Console.WriteLine($"잔액은: {account.Balance}");
        account.Deposit(400);
        Console.WriteLine($"{account.Balance}");
    }
}
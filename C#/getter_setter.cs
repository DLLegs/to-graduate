// See https://aka.ms/new-console-template for more information

using System;

class Person
{
    private string name;

    public string Name
    {
        get { return name; }
        set { name = value; }
    }
}

class Program
{
    static void Main()
    {
        Person p = new Person();
        /*set 블록 실행 value = "Alice"*/
        p.Name = "Alice";
        /*get 블록 실행 name값을 반환*/
        Console.WriteLine(p.Name);
    }
}
// See https://aka.ms/new-console-template for more information
using System;

class Person
{   
    // class의 property
    public string Name;
    public string Birthday;
    public string Gender;

    // class의 method
    public void Eat()
    {
        Console.WriteLine(Name + "이(가) 아침을 먹습니다");
    }
    public void Walk()
    {
        Console.WriteLine(Name + "이(가) 걷고 있습니다");
    }
    public void Run()
    {
        Console.WriteLine(Name + "이(가) 뛰고 있습니다");
    }
}

// 클래스 시작
class MainClass
{
    public static void Main(string[] args)
    {
        // 인스턴스만 만듬
        Person p1;
        // 메모리에 새 인스턴스 할당(초기화)
        p1 = new Person();
        p1.Name = "서준";
        p1.Eat();
    }
}
// 클래스 종료
// See https://aka.ms/new-console-template for more information

using System;

class Cat
{
    /* 고양이의 이름을 저장하는 맴버 변수 */
    public string Name;
    public int Weight;

    /* 생성자 */
    public Cat(string name)
    {
        Name = name;
        Console.WriteLine("생성자 호출");
        Console.WriteLine("고양이 이름" + Name);
    }
    
    /*오버로딩*/
    public Cat(string name, int weight)
    {
        Name = name;
        Weight = weight;
        Console.WriteLine("이름은" + Name + "몸무게는 " + Weight + "kg");
    }
}

class MainClass
{
    public static void Main(string[] args)
    {
        /* coco, moly 라는 객체 생성 */
        Cat coco = new Cat("코코");
        Cat moly = new Cat("몰리", 3);
    }
}

/* 소멸자는 필수가 아님
 * 외부 리소스(파일, 네트워크, DB연결) 등일때 직접 해제
 * Dispose를 이용하여 명시적 해제가 필요 */
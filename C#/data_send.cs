using System;

class Cat
{
    /*맴버 변수*/
    public string Name;

    public Cat(string name)
    {
        /*맴버변수 = 매개변수*/
        Name = name;
        Console.WriteLine("고양이 이름" +Name);

    }
}

class MainClass
{
    public static void Main(string[] args)
    {
        Cat coco = new Cat("코코");
        coco.Name = "몰리";
        Console.Write("고양이 이름은" + coco.Name);
    }
}
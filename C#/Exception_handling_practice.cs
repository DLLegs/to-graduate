using System;

class InvalidNameException : Exception
{
    public InvalidNameException(string massage):base(massage) { }
}
class Program
{
    static void ValidateNumber(int num)
    {
        if (num<1 || num > 100)
        {
            throw new InvalidNameException("숫자는 1에서 100 사이여야 합니다!");
        }
    }
    static void Main()
    {
        try
        {
            Console.WriteLine("숫자를 입력하세요: ");
            int num = int.Parse(Console.ReadLine());
            ValidateNumber(num);
            Console.WriteLine($"내가 입력한 숫자: {num}");
        }
        catch (InvalidNameException ex)
        {
            Console.WriteLine($"사용자 정의 예외 발생: {ex.Message}");
        }
        catch (Exception e)
        {
            Console.WriteLine($"예외 오류 발생: {e.Message}");
        }
    }
}
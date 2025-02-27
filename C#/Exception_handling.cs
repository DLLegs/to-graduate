using System;

class MainClass
{
    public static void Main(String[] args)
    {
        void CheckNumber(int number)
        {
            if (number <= 0)
            {
                /* throw를 사용하여 직접 예외를 발생 */
                throw new ArgumentException("숫자는 0보다 커야합니다!!!");
            }
            Console.WriteLine($"입력하신 숫자는 {number}");
        }
        
        /* if else문과 같은 예외처리에 사용하는 try catch */
        try
        {
            Console.WriteLine("나눌 숫자를 선택하세요: ");
            int divider = int.Parse(Console.ReadLine());
            CheckNumber(divider);
            Console.WriteLine($"결과: {10 / divider}");
        }
        /* 예외를 세분화 하여 더 정확한 오류 메세지 제공 */
        catch(DivideByZeroException)
        {
            Console.WriteLine("X  0으로는 나눌 수 없습니다!");
        }
        catch (FormatException)
        {
            Console.WriteLine("X  올바른 숫자를 입력하세요!");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"예기치 않은 오류: {ex.Message}");
        }
        /* 예외에 상관없이 실행, 프로그램&파일 입출력이 끝날 때 자주 이용 */
        finally
        {
            Console.WriteLine("프로그램이 종료됩니다.");
        }
    }
}
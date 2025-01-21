// See https://aka.ms/new-console-template for more information

using System;
using System.Numerics;
using System.Runtime.InteropServices;

namespace OperatorPractice
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("C# 연산자 연습");

            ArithmeticOperators.Run();
            ComparisonOperators.Run();
            LogicalOperators.Run();
            AssignmentOperators.Run();
            IncrementDecrementOperators.Run();
            TernaryOperator.Run();
        }
    }

    class ArithmeticOperators
    {
        public static void Run()
        {
            Console.WriteLine("--산술 연산자--");
            int a = 10, b = 3;
            Console.WriteLine($"a + b = {a + b}");
            Console.WriteLine($"a - b = {a - b}");
            Console.WriteLine($"a * b = {a * b}");
            Console.WriteLine($"a / b = {a / b}");
            Console.WriteLine($"a % b = {a % b}");
        }
        
    }

    class ComparisonOperators
    {
        public static void Run()
        {
            Console.WriteLine("--비교 연산자--");
            int a = 10, b = 20;

            Console.WriteLine($"a == b: {a == b}");
            Console.WriteLine($"a != b: {a != b}");
            Console.WriteLine($"a >= b: {a >= b}");
            Console.WriteLine($"a <= b: {a <= b}");
        }
    }

    class LogicalOperators
    {
        public static void Run() 
        {
            Console.WriteLine("--논리 연산자--");
            bool x = true, y = false;

            Console.WriteLine($"x && y: {x && y}");
            Console.WriteLine($"x || y: {x || y}");
            Console.WriteLine($"!x: {!x}");
        }    
    }

    class AssignmentOperators
    {
        public static void Run()
        {
            Console.WriteLine("--할당 연산자--");
            int a = 5;

            a += 3;
            Console.WriteLine($"a += 3: {a}");
            a -= 2;
            Console.WriteLine($"a -= 2: {a}");
            a *= 4;
            Console.WriteLine($"a *= 4: {a}");
            a /= 2;
            Console.WriteLine($"a /= 2: {a}");
            a %= 3;
            Console.WriteLine($"a %= 3: {a}");
        }
    }

    class IncrementDecrementOperators
    {
        public static void Run()
        {
            Console.WriteLine("--증감 연산자--");
            int a = 5;

            Console.WriteLine($"a: {a}");
            Console.WriteLine($"a++: {a++}");
            Console.WriteLine($"a: {a}");
            Console.WriteLine($"++a: {++a}");
            Console.WriteLine($"a--: {a--}");
            Console.WriteLine($"--a: {--a}");
        }
    }

    class TernaryOperator
    {
        public static void Run()
        {
            Console.WriteLine("--삼항 연산자--");
            int a = 10, b = 20;
            /* 삼항 연산자
                조건식 ? 참일 때 값: 거짓일 때 값;
                조건식 앞 true와 false 출력에 따라 string, int 등으로 포시
                if문 보다 간단한 조건문을 사용할 때 주로 사용*/
            string result = (a > b) ? "a가 b보다 큽니다." : "a가 b보다 작거나 같습니다.";
            Console.WriteLine(result);
        }    
    }
}
using System;
using System.Collections.Generic;
using System.IO;

namespace InfBez
{
    class Program
    {
        static void Main(string[] args)
        {
            int[,] Compression(int[,] input, int aperture)
            {
                int n = input.GetUpperBound(0) + 1;
                List<int> output_X = new List<int>();
                List<int> output_Y = new List<int>();
                output_X.Add(input[0, 0]);
                output_Y.Add(input[0, 1]);

                for (int i = 0; i <= n - 3; i++)
                {
                    for (int j = i + 1; j <= n - 2; j++)
                    {
                        double y = (input[j, 0] - input[i, 0]) * (input[j + 1, 1] - input[i, 1]) / (input[j + 1, 0] - input[i, 0]) + input[i, 1];
                        if (Math.Abs(input[j, 1] - y) >= aperture)
                        {
                            output_X.Add(input[j, 0]);
                            output_Y.Add(input[j, 1]);
                            i = j - 1;
                            break;
                        }
                    }
                }
                output_X.Add(input[n - 1, 0]);
                output_Y.Add(input[n - 1, 1]);
                int[,] output = new int[output_X.Count, 2];
                for (int i = 0; i < output_X.Count; i++)
                {
                    output[i, 0] = output_X[i];
                    output[i, 1] = output_Y[i];
                }
                return output;
            }

            double[,] Recover(int[,] input, int delta)
            {
                int n = input.GetUpperBound(0) + 1;
                List<int> output_X = new List<int>();
                List<double> output_Y = new List<double>();
                output_X.Add(input[0, 0]);
                output_Y.Add(input[0, 1]);
                for (int i = 0; i < n - 1; i++)
                {
                    int j = i + 1;
                    if (input[j, 0] - input[i, 0] > delta)
                    {
                        for (int k = delta; k < input[j, 0] - input[i, 0]; k=k+delta)
                        {
                            double y = (double)(input[i, 0] + k - input[i, 0]) * (double)(input[j, 1] - input[i, 1]) / (double)(input[j, 0] - input[i, 0]) + (double)input[i, 1];
                            output_X.Add(input[i, 0] + k);
                            output_Y.Add(Math.Round(y, 1));
                        }
                    }
                    output_X.Add(input[j, 0]);
                    output_Y.Add(input[j, 1]);
                }
                double[,] output = new double[output_X.Count, 2];
                for (int i = 0; i < output_X.Count; i++)
                {
                    output[i, 0] = output_X[i];
                    output[i, 1] = output_Y[i];
                }
                return output;
            }

            Console.WriteLine("Введите число точек:");
            int N = int.Parse(Console.ReadLine());
            int[,] input = new int[N, 2];
            Console.WriteLine("Через пробел введите индекс точки и значение функции (целый тип):");
            for (int i = 0; i < N; i++)
            {
                string[] line = Console.ReadLine().Split(' ');
                input[i, 0] = int.Parse(line[0]);
                input[i, 1] = int.Parse(line[1]);
            }
            Console.WriteLine("Введите значение апертуры (целое):");
            int e = int.Parse(Console.ReadLine());
            Console.WriteLine("Введите длину дискреционного шага:");
            int delta = int.Parse(Console.ReadLine());
            string path = "C:/Users/Xiaomi/Downloads/Compress.txt";

            Console.WriteLine("Исходный массив:");
            int n = input.GetUpperBound(0) + 1;
            string text = "";
            for (int i = 0; i < n; i++)
            {
                text += "[" + input[i, 0] + "; " + input[i, 1] + "] ";
                Console.Write("[" + input[i, 0] + "; " + input[i, 1] + "] ");
            }
            using (StreamWriter writer = new StreamWriter(path, true))
            {
                writer.WriteLineAsync("Исходный массив:");
                writer.WriteLineAsync(text);
            }
            Console.WriteLine();
            Console.WriteLine();

            Console.WriteLine("Сжатый массив:");
            int[,] compressed = Compression(input, e);
            n = compressed.GetUpperBound(0) + 1;
            string ctext = "";
            for (int i = 0; i < n; i++)
            {
                ctext += "[" + compressed[i, 0] + "; " + compressed[i, 1] + "] ";
                Console.Write("[" + compressed[i, 0] + "; " + compressed[i, 1] + "] ");
            }

            using (StreamWriter writer = new StreamWriter(path, true))
            {
                writer.WriteLineAsync("\nСжатый массив:");
                writer.WriteLineAsync(ctext);
            }
            Console.WriteLine();
            Console.WriteLine();

            Console.WriteLine("Восстановленный массив:");
            double[,] recovered = Recover(compressed, delta);
            n = recovered.GetUpperBound(0) + 1;
            string rtext = "";
            for (int i = 0; i < n; i++)
            {
                rtext += "[" + recovered[i, 0] + "; " + recovered[i, 1] + "] ";
                Console.Write("[" + recovered[i, 0] + "; " + recovered[i, 1] + "] ");
            }
            using (StreamWriter writer = new StreamWriter(path, true))
            {
                writer.WriteLineAsync("\nВосстановленный массив:");
                writer.WriteLineAsync(rtext);
            }
            Console.ReadKey();
        }
    }
}
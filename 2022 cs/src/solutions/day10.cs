public class Day10
{
  public void solveDay()
  {
    // a 15020 b
    Console.WriteLine("Day 10: " + "a sultion: " + a().ToString() + " b solution: " + b().ToString());
  }

  private int a()
  {
    string[] input = getInput();
    int cycle = 1;
    int X = 1;
    List<int> signalStrength = new List<int>();

    foreach (string line in input)
    {
      if (line == "noop") // noop
      {
        // next cycle
        cycle += increaseCycleA(cycle, X, signalStrength);
        Console.WriteLine("cycle: " + cycle + "  X: " + X);
        continue;
      }
      else // addx
      {
        int num = Convert.ToInt32(line.Split(" ")[1]);

        Console.WriteLine("num: " + num);

        for (int i = 1; i <= 2; i++)
        {
          // next cycle
          cycle += increaseCycleA(cycle, X, signalStrength);
          Console.WriteLine("cycle: " + cycle + "  X: " + X);
        }

        X += num;
      }
    }

    return signalStrength.Sum();
  }

  private int increaseCycleA(int cycle, int X, List<int> signalStrength)
  {
    if (cycle == 20)
    {
      // check signal strength
      signalStrength.Add(cycle * X);
    }
    else if ((cycle - 19) % 40 == 1)
    {
      // check signal strength
      signalStrength.Add(cycle * X);
      Console.WriteLine("Signal Strength: " + cycle);
    }

    return 1;
  }

  private int b()
  {
    string[] input = getInput();
    int cycle = 1;
    int X = 1;
    List<int> signalStrength = new List<int>();

    foreach (string line in input)
    {
      if (line == "noop") // noop
      {
        // next cycle
        cycle += increaseCycleB(cycle, X, signalStrength);
        Console.WriteLine("cycle: " + cycle + "  X: " + X);
        continue;
      }
      else // addx
      {
        int num = Convert.ToInt32(line.Split(" ")[1]);

        Console.WriteLine("num: " + num);

        for (int i = 1; i <= 2; i++)
        {
          // next cycle
          cycle += increaseCycleB(cycle, X, signalStrength);
          Console.WriteLine("cycle: " + cycle + "  X: " + X);
        }

        X += num;
      }
    }

    return signalStrength.Sum();
  }

  private int increaseCycleB(int cycle, int X, List<int> signalStrength)
  {
    if (cycle == 20)
    {
      // check signal strength
      signalStrength.Add(cycle * X);
    }
    else if ((cycle - 19) % 40 == 1)
    {
      // check signal strength
      signalStrength.Add(cycle * X);
      Console.WriteLine("Signal Strength: " + cycle);
    }

    return 1;
  }

  private string[] getInput()
  {
    return File.ReadAllLines("./src/2022/input/day10.txt");
  }
}
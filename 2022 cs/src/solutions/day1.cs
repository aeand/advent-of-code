public class Day1
{
  public void solveDay()
  {
    // 69206 197400
    Console.WriteLine("Day 1: " + "a solution: " + a().ToString() + " b solution: " + b().ToString());
  }

  public int a()
  {
    string[] input = getInput();
    List<int> inputChunk = new List<int> { };
    List<int> sums = new List<int> { };

    foreach (string row in input)
    {
      if (row == "")
      {
        int sum = 0;

        foreach (int num in inputChunk)
        {
          sum = sum + num;
        }
        sums.Add(sum);
        inputChunk.Clear();
      }
      else
      {
        inputChunk.Add(int.Parse(row));
      }
    }

    return sums.Max();
  }

  public int b()
  {
    string[] input = getInput();
    List<int> inputChunk = new List<int> { };
    List<int> sums = new List<int> { };

    foreach (string row in input)
    {
      if (row == "")
      {
        int sum = 0;

        foreach (int num in inputChunk)
        {
          sum = sum + num;
        }
        sums.Add(sum);
        inputChunk.Clear();
      }
      else
      {
        inputChunk.Add(int.Parse(row));
      }
    }

    int topThree = 0;

    for (int i = 0; i < 3; i++)
    {
      topThree = topThree + sums.Max();

      sums.Remove(sums.Max());
    }

    return topThree;
  }

  private string[] getInput()
  {
    return File.ReadAllLines("./src/2022/input/day1.txt");
  }
}
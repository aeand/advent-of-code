public class Day6
{
  public void solveDay()
  {
    Console.WriteLine("Day 6: " + "a solution: " + a().ToString() + " b solution: " + b().ToString());
  }

  public int a()
  {
    string[] lol = getInput();
    char[] input = lol[0].ToArray();
    List<char> lookedThroughChars = new List<char>();
    List<char> lastFourUniqueChars = new List<char>();
    int counter = 0;

    for (int i = 0; i < input.Length; i++)
    {
      counter++;
      if (counter < 4)
      {
        lastFourUniqueChars.Add(input[i]);
      }
      else
      {
        lastFourUniqueChars.Add(input[i]);
        char[] unique = lastFourUniqueChars.Distinct().ToArray();
        if(unique.Length == 4)
        {
          break;
        }

        lastFourUniqueChars.RemoveAt(0);
      }
    }

    return counter;
  }

  public int b()
  {
    string[] lol = getInput();
    char[] input = lol[0].ToArray();
    List<char> lookedThroughChars = new List<char>();
    List<char> lastFourUniqueChars = new List<char>();
    int counter = 0;

    for (int i = 0; i < input.Length; i++)
    {
      counter++;
      if (counter < 14)
      {
        lastFourUniqueChars.Add(input[i]);
      }
      else
      {
        lastFourUniqueChars.Add(input[i]);
        char[] unique = lastFourUniqueChars.Distinct().ToArray();
        if(unique.Length == 14)
        {
          break;
        }

        lastFourUniqueChars.RemoveAt(0);
      }
    }

    return counter;
  }

  private string[] getInput()
  {
    return File.ReadAllLines("./src/2022/input/day6.txt");
  }
}
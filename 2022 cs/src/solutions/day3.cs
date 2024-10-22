public enum scoreSheet
{
  a = 1,
  b = 2,
}

public class Day3
{
  public void solveDay()
  {
    // 7967 2716
    Console.WriteLine("Day 3: " + "a sultion: " + a().ToString() + " b solution: " + b().ToString());
  }

  private int a()
  {
    string[] input = getInput();
    List<char> sharedItemsInRow = new List<char>();
    List<char> noDuplicateItemsList = new List<char>();
    int score = 0;

    Dictionary<char, int> scoreboard = createScoreboard();

    foreach (string row in input)
    {
      char[] line = row.ToArray();
      char[] category1 = new char[line.Length / 2];
      char[] category2 = new char[line.Length / 2];

      for (int i = 0; i < line.Length / 2; i++)
      {
        category1[i] = line[i];
        category2[i] = line[line.Length / 2 + i];
      }

      for (int i = 0; i < category1.Length; i++)
      {
        for (int j = 0; j < category2.Length; j++)
        {
          if (category1[i] == category2[j])
          {
            sharedItemsInRow.Add(category1[i]);
            break;
          }
        }
      }

      List<char> soloBoiList = sharedItemsInRow.Distinct().ToList<char>();
      char soloBoi = soloBoiList[0];
      noDuplicateItemsList.Add(soloBoi);
      sharedItemsInRow.Clear();
    }

    foreach (char item in noDuplicateItemsList)
    {
      score = score + scoreboard[item];
    }

    return score;
  }

  private int b()
  {
    string[] input = getInput();
    List<char> sharedItemInGroup = new List<char>();
    int score = 0;

    Dictionary<char, int> scoreboard = createScoreboard();

    // look through the 3 rows
    for (int i = 0; i < input.Length; i = i + 3)
    {
      string row1 = input[i];
      string row2 = input[i + 1];
      string row3 = input[i + 2];

      // find the common char
      foreach (char j in row1)
      {
        foreach (char k in row2)
        {
          if (j == k)
          {
            foreach (char l in row3)
            {
              if (k == l)
              {
                sharedItemInGroup.Add(l);
                break;
              }
            }
          }
        }
      }

      sharedItemInGroup = sharedItemInGroup.Distinct().ToList<char>();

      // sum the badge number up
      foreach (char item in sharedItemInGroup)
      {
        score = score + scoreboard[item];
      }

      sharedItemInGroup.Clear();
    }

    return score;
  }

  private Dictionary<char, int> createScoreboard()
  {
    Dictionary<char, int> scoreboard = new Dictionary<char, int>();
    scoreboard.Add('a', 1);
    scoreboard.Add('b', 2);
    scoreboard.Add('c', 3);
    scoreboard.Add('d', 4);
    scoreboard.Add('e', 5);
    scoreboard.Add('f', 6);
    scoreboard.Add('g', 7);
    scoreboard.Add('h', 8);
    scoreboard.Add('i', 9);
    scoreboard.Add('j', 10);
    scoreboard.Add('k', 11);
    scoreboard.Add('l', 12);
    scoreboard.Add('m', 13);
    scoreboard.Add('n', 14);
    scoreboard.Add('o', 15);
    scoreboard.Add('p', 16);
    scoreboard.Add('q', 17);
    scoreboard.Add('r', 18);
    scoreboard.Add('s', 19);
    scoreboard.Add('t', 20);
    scoreboard.Add('u', 21);
    scoreboard.Add('v', 22);
    scoreboard.Add('w', 23);
    scoreboard.Add('x', 24);
    scoreboard.Add('y', 25);
    scoreboard.Add('z', 26);
    scoreboard.Add('A', 27);
    scoreboard.Add('B', 28);
    scoreboard.Add('C', 29);
    scoreboard.Add('D', 30);
    scoreboard.Add('E', 31);
    scoreboard.Add('F', 32);
    scoreboard.Add('G', 33);
    scoreboard.Add('H', 34);
    scoreboard.Add('I', 35);
    scoreboard.Add('J', 36);
    scoreboard.Add('K', 37);
    scoreboard.Add('L', 38);
    scoreboard.Add('M', 39);
    scoreboard.Add('N', 40);
    scoreboard.Add('O', 41);
    scoreboard.Add('P', 42);
    scoreboard.Add('Q', 43);
    scoreboard.Add('R', 44);
    scoreboard.Add('S', 45);
    scoreboard.Add('T', 46);
    scoreboard.Add('U', 47);
    scoreboard.Add('V', 48);
    scoreboard.Add('W', 49);
    scoreboard.Add('X', 50);
    scoreboard.Add('Y', 51);
    scoreboard.Add('Z', 52);

    return scoreboard;
  }

  private string[] getInput()
  {
    return File.ReadAllLines("./src/2022/input/day3.txt");
  }
}
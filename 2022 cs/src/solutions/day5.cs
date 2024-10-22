public class Day5
{
  public void solveDay()
  {
    Console.WriteLine("Day 5: " + "a sultion: " + a() + " b solution: " + b());
  }

  private string a()
  {
    // input parsing
    string[] input = getInput();
    List<string> table = new List<string>();

    foreach (string row in input)
    {
      if (row == "")
      {
        break;
      }

      table.Add(row);
    }

    List<string> coolTable = new List<string>();

    for (int i = 1; i < 35; i = i + 4)
    {
      foreach (string row in table)
      {
        coolTable.Add(row.Substring(i, 1));
      }
    }

    List<List<string>> stacks = new List<List<string>>();
    List<string> stack = new List<string>();

    foreach (string entry in coolTable)
    {
      if (entry == "1"
        || entry == "2"
        || entry == "3"
        || entry == "4"
        || entry == "5"
        || entry == "6"
        || entry == "7"
        || entry == "8"
        || entry == "9"
      )
      {
        stacks.Add(stack);
        stack = new List<string>();
      }
      else
      {
        stack.Add(entry);
      }
    }

    // Reverse
    for (int i = 0; i < stacks.Count; i++)
    {
      stacks[i].Reverse();
    }

    // Remove empty strings
    List<int> removeEntryIndex = new List<int>();
    for (int i = 0; i < stacks.Count; i++)
    {
      int countSomething = 0;

      for (int j = 0; j < stacks[i].Count; j++)
      {
        if (stacks[i][j] == " ")
        {
          removeEntryIndex.Add(stacks[i].Count - 1 - countSomething);
          countSomething++;
        }
      }

      countSomething = 0;

      for (int k = 0; k < removeEntryIndex.Count; k++)
      {
        stacks[i].RemoveAt(removeEntryIndex[k]);
      }
      removeEntryIndex.Clear();
    }

    // Instructions
    foreach (string row in input)
    {
      if (row == "" || row.Substring(0, 1) == "[" || row.Substring(0, 1) == " ")
      {

      }
      else
      {
        int offset = 0;
        if (row.Substring(16, 2).Trim() == "o")
        {
          offset = 1;
        }

        int move = int.Parse(row.Substring(5, 2).Trim());
        int from = int.Parse(row.Substring(12, 2).Trim()) - 1;
        int to = int.Parse(row.Substring(16 + offset, 2).Trim()) - 1;
        offset = 0;

        for (int i = 0; i < move; i++)
        {
          //take first entry in from
          string entry = stacks[from].Last();
          //remove from from list
          stacks[from].RemoveAt(stacks[from].Count - 1);
          //add to to list
          stacks[to].Add(entry);
        }
      }
    }

    string finalWord = "";
    for (int i = 0; i < stacks.Count; i++)
    {
      finalWord = finalWord + stacks[i].Last();
    }

    return finalWord;
  }

  private string b()
  {
    // input parsing
    string[] input = getInput();
    List<string> table = new List<string>();

    foreach (string row in input)
    {
      if (row == "")
      {
        break;
      }

      table.Add(row);
    }

    List<string> coolTable = new List<string>();

    for (int i = 1; i < 35; i = i + 4)
    {
      foreach (string row in table)
      {
        coolTable.Add(row.Substring(i, 1));
      }
    }

    List<List<string>> stacks = new List<List<string>>();
    List<string> stack = new List<string>();

    foreach (string entry in coolTable)
    {
      if (entry == "1"
        || entry == "2"
        || entry == "3"
        || entry == "4"
        || entry == "5"
        || entry == "6"
        || entry == "7"
        || entry == "8"
        || entry == "9"
      )
      {
        stacks.Add(stack);
        stack = new List<string>();
      }
      else
      {
        stack.Add(entry);
      }
    }

    // Reverse
    for (int i = 0; i < stacks.Count; i++)
    {
      stacks[i].Reverse();
    }

    // Remove empty strings
    List<int> removeEntryIndex = new List<int>();
    for (int i = 0; i < stacks.Count; i++)
    {
      int countSomething = 0;

      for (int j = 0; j < stacks[i].Count; j++)
      {
        if (stacks[i][j] == " ")
        {
          removeEntryIndex.Add(stacks[i].Count - 1 - countSomething);
          countSomething++;
        }
      }

      countSomething = 0;

      for (int k = 0; k < removeEntryIndex.Count; k++)
      {
        stacks[i].RemoveAt(removeEntryIndex[k]);
      }
      removeEntryIndex.Clear();
    }

    // Instructions
    foreach (string row in input)
    {
      if (row == "" || row.Substring(0, 1) == "[" || row.Substring(0, 1) == " ")
      {

      }
      else
      {
        int offset = 0;
        if (row.Substring(16, 2).Trim() == "o")
        {
          offset = 1;
        }

        int move = int.Parse(row.Substring(5, 2).Trim());
        int from = int.Parse(row.Substring(12, 2).Trim()) - 1;
        int to = int.Parse(row.Substring(16 + offset, 2).Trim()) - 1;
        offset = 0;

        List<string> stackToMove = new List<string>();

        for (int i = 0; i < move; i++)
        {
          //take first entry in from
          string entry = stacks[from].Last();
          //add entries to stack
          stackToMove.Add(entry);
          //remove from from list
          stacks[from].RemoveAt(stacks[from].Count - 1);
        }

        stackToMove.Reverse();

        for (int i = 0; i < stackToMove.Count; i++)
        {
          //add to to list
          stacks[to].Add(stackToMove[i]);
        }
        stackToMove = new List<string>();
      }
    }

    string finalWord = "";
    for (int i = 0; i < stacks.Count; i++)
    {
      finalWord = finalWord + stacks[i].Last();
    }

    return finalWord;
  }

  private string[] getInput()
  {
    return File.ReadAllLines("./src/2022/input/day5.txt");
  }
}

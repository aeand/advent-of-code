public class Day8
{
  public void solveDay()
  {
    // a 1843 b ?
    Console.WriteLine("Day 8: " + "a sultion: " + a().ToString() + " b solution: " + b().ToString());
  }

  private int a()
  {
    string[] input = getInput();
    List<List<int>> grid = new List<List<int>>();

    // prep column list
    foreach (string line in input)
    {
      List<int> row = new List<int>();

      foreach (char tree in line)
      {
        row.Add(int.Parse(tree.ToString()));
      }
      grid.Add(row);
    }

    int visibleTreeCounter = 0;

    // loop every tree
    for (int row = 0; row < grid[0].Count; row++)
    {
      for (int col = 0; col < grid.Count; col++)
      {
        // save tree
        int tree = grid[row][col];

        // reset visible tree check
        bool[] isTreeVisible = new bool[4];
        for (int i = 0; i < isTreeVisible.Length; i++)
        {
          isTreeVisible[i] = false;
        }

        // don't check outer tree ring
        if (row == 0 || col == 0 || row == grid[row].Count - 1 || col == grid.Count - 1)
        {
          visibleTreeCounter++;
        }
        else
        {
          // compare tree against left
          for (int l = col - 1; l >= 0; l--)
          {
            if (tree > grid[row][l])
            {
              // mark tree as visible
              isTreeVisible[0] = true;
            }
            else
            {
              isTreeVisible[0] = false;
              break;
            }
          }

          // compare tree against right
          for (int r = col + 1; r < grid[row].Count; r++)
          {
            if (tree > grid[row][r])
            {
              // mark tree as visible
              isTreeVisible[1] = true;
            }
            else
            {
              isTreeVisible[1] = false;
              break;
            }
          }

          // compare tree against up
          for (int u = row - 1; u >= 0; u--)
          {
            if (tree > grid[u][col])
            {
              // mark tree as visible
              isTreeVisible[2] = true;
            }
            else
            {
              isTreeVisible[2] = false;
              break;
            }
          }

          // compare tree against down
          for (int d = row + 1; d < grid.Count; d++)
          {
            if (tree > grid[d][col])
            {
              // mark tree as visible
              isTreeVisible[3] = true;
            }
            else
            {
              isTreeVisible[3] = false;
              break;
            }
          }

          // check tree visibility
          for (int i = 0; i < isTreeVisible.Length; i++)
          {
            if (isTreeVisible[i] == true)
            {
              visibleTreeCounter++;
              break;
            }
          }
        }
      }
    }

    return visibleTreeCounter;
  }

  private int b()
  {
    string[] input = getInput();
    List<List<int>> grid = new List<List<int>>();
    List<int> treeScores = new List<int>();

    // prep column list
    foreach (string line in input)
    {
      List<int> row = new List<int>();

      foreach (char tree in line)
      {
        row.Add(int.Parse(tree.ToString()));
      }
      grid.Add(row);
    }

    // loop every tree
    for (int row = 0; row < grid[0].Count; row++)
    {
      for (int col = 0; col < grid.Count; col++)
      {
        // save tree
        int tree = grid[row][col];

        // reset tree score
        int[] treeScore = new int[4];
        treeScore[0] = 0;
        treeScore[1] = 0;
        treeScore[2] = 0;
        treeScore[3] = 0;

        // don't check outer tree ring
        if (row == 0 || col == 0 || row == grid[row].Count - 1 || col == grid.Count - 1)
        {

        }
        else
        {
          // compare tree against left
          for (int l = col - 1; l >= 0; l--)
          {
            if (tree > grid[row][l])
            {
              // mark tree as visible
              treeScore[0]++;
            }
            else if (tree == grid[row][l])
            {
              treeScore[0]++;
              break;
            }
            else
            {
              break;
            }
          }

          // compare tree against right
          for (int r = col + 1; r < grid[row].Count; r++)
          {
            if (tree > grid[row][r])
            {
              // mark tree as visible
              treeScore[1]++;
            }
            else if (tree == grid[row][r])
            {
              treeScore[1]++;
              break;
            }
            else
            {
              break;
            }
          }

          // compare tree against up
          for (int u = row - 1; u >= 0; u--)
          {
            if (tree > grid[u][col])
            {
              // mark tree as visible
              treeScore[2]++;
            }
            else if (tree == grid[u][col])
            {
              treeScore[2]++;
              break;
            }
            else
            {
              break;
            }
          }

          // compare tree against down
          for (int d = row + 1; d < grid.Count; d++)
          {
            if (tree > grid[d][col])
            {
              // mark tree as visible
              treeScore[3]++;
            }
            else if (tree == grid[d][col])
            {
              treeScore[3]++;
              break;
            }
            else
            {
              break;
            }
          }

          // check tree score
          int sum = treeScore[0] * treeScore[1] * treeScore[2] * treeScore[3];
          treeScores.Add(sum);
        }
      }
    }

    return treeScores.Max();
  }

  private string[] getInput()
  {
    return File.ReadAllLines("./src/2022/input/day8.txt");
  }
}



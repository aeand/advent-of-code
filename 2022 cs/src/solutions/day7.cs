public class Day7
{
  public void solveDay()
  {
    Console.WriteLine();
  }

  private string a()
  {
    List<Dictionary<string, int>> dirs = new List<Dictionary<string, int>>();
    Dictionary<string, int> dirSize = new Dictionary<string, int>();

    List<string> dirTracker = new List<string>();
    int depthCounter = 0;

    string[] input = getInput();

    foreach (string row in input)
    {
      // count depth with an int, to determine what dir im in

      if (row.Substring(1, 1) == "$")
      {
        if (row.Substring(3, 4) == "cd")
        {
          // save dir name

          if (row.Substring(5, 7) == "..")
          {
            // go back in list to track dir
            depthCounter--;
          }
          else
          {
            depthCounter++;
            dirTracker.Add(row.Substring(5));
            dirSize.Add(row.Substring(5), 0);
          }
        }
        else if (row.Substring(3, 4) == "ls")
        {

        }
      }
      else if(int.Parse(row.Substring(1, 1)).GetType() == typeof(int))
      {
        // read int and add together to form dirsize

      }
    }

    return "";
  }

  private string b()
  {
    return "";
  }

  private string[] getInput()
  {
    return File.ReadAllLines("./src/2022/input/day7.txt");
  }
}
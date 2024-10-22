public class Day4
{
  public void solveDay()
  {
    // 462 835
    Console.WriteLine("Day 4: " + "a sultion: " + a().ToString() + " b solution: " + b().ToString());
  }

  private int a()
  {
    string[] input = getInput();
    int count = 0;

    foreach (string row in input)
    {
      string[] zones = row.Replace(',', '-').Split('-');
      int[] ids = new int[4];

      for (int i = 0; i < 4; i++)
      {
        ids[i] = int.Parse(zones[i]);
      }

      if ((ids[0] >= ids[2] && ids[1] <= ids[3])
        || (ids[0] <= ids[2] && ids[1] >= ids[3]))
      {
        count++;
      }
    }

    return count;
  }

  private int b()
  {
    string[] input = getInput();
    int count = 0;

    foreach (string row in input)
    {
      string[] zones = row.Replace(',', '-').Split('-');
      int[] ids = new int[4];

      for (int i = 0; i < 4; i++)
      {
        ids[i] = int.Parse(zones[i]);
      }

      if ((ids[0] >= ids[3] && ids[1] <= ids[2])
      || (ids[0] <= ids[3] && ids[1] >= ids[2]))
      {
        count++;
      }
    }

    return count;
  }

  private string[] getInput()
  {
    return File.ReadAllLines("./src/2022/input/day4.txt");
  }
}

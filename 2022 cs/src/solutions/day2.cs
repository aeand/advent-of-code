public class Day2
{
  public void solveDay()
  {
    /*
    * rock    A X 1
    * paper   B Y 2
    * scissor C Z 3
    */

    // 10310 14859
    Console.WriteLine("Day 2: " + "a sultion: " + a().ToString() + " b solution: " + b().ToString());
  }

  private int a()
  {
    Dictionary<string, string> cheat = new Dictionary<string, string>();
    cheat.Add("A", "Y");
    cheat.Add("B", "Z");
    cheat.Add("C", "X");

    Dictionary<string, string> same = new Dictionary<string, string>();
    same.Add("A", "X");
    same.Add("B", "Y");
    same.Add("C", "Z");

    Dictionary<string, int> scoreCalc = new Dictionary<string, int>();
    scoreCalc.Add("X", 1);
    scoreCalc.Add("Y", 2);
    scoreCalc.Add("Z", 3);

    string[] input = getInput();
    int score = 0;

    foreach (string line in input)
    {
      string[] values = line.Split(" ");
      string theirs = values[0];
      string mine = values[1];
      score = score + scoreCalc[mine];

      // win
      if (cheat[theirs] == mine)
      {
        score = score + 6;
      }
      // draw
      else if (same[theirs] == mine)
      {
        score = score + 3;
      }
      // lose
      else
      {
        score = score + 0;
      }
    }

    return score;
  }

  private int b()
  {
    Dictionary<string, string> cheat = new Dictionary<string, string>();
    cheat.Add("A", "Y");
    cheat.Add("B", "Z");
    cheat.Add("C", "X");

    Dictionary<string, string> same = new Dictionary<string, string>();
    same.Add("A", "X");
    same.Add("B", "Y");
    same.Add("C", "Z");

    Dictionary<string, int> scoreCalcWin = new Dictionary<string, int>();
    scoreCalcWin.Add("A", 2);
    scoreCalcWin.Add("B", 3);
    scoreCalcWin.Add("C", 1);

    Dictionary<string, int> scoreCalcDraw = new Dictionary<string, int>();
    scoreCalcDraw.Add("A", 1);
    scoreCalcDraw.Add("B", 2);
    scoreCalcDraw.Add("C", 3);

    Dictionary<string, int> scoreCalcLose = new Dictionary<string, int>();
    scoreCalcLose.Add("A", 3);
    scoreCalcLose.Add("B", 1);
    scoreCalcLose.Add("C", 2);

    Dictionary<string, string> match = new Dictionary<string, string>();
    match.Add("X", "lose");
    match.Add("Y", "draw");
    match.Add("Z", "win");

    string[] input = getInput();
    int score = 0;

    foreach (string line in input)
    {
      string[] values = line.Split(" ");
      string theirs = values[0];
      string matchOutcome = values[1];
      string gameDirection = match[matchOutcome];

      // win
      if (gameDirection == "win")
      {
        score = score + 6;
        score = score + scoreCalcWin[theirs];
      }
      // draw
      else if (gameDirection == "draw")
      {
        score = score + 3;
        score = score + scoreCalcDraw[theirs];
      }
      // lose
      else if (gameDirection == "lose")
      {
        score = score + 0;
        score = score + scoreCalcLose[theirs];
      }
    }

    return score;
  }

  private string[] getInput()
  {
    return File.ReadAllLines("./src/2022/input/day2.txt");
  }
}

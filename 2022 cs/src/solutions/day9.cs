public class Coord
{
  public int x;
  public int y;

  public Coord(int x, int y)
  {
    this.x = x;
    this.y = y;
  }

  public string coordString()
  {
    return this.x.ToString() + "," + this.y.ToString();
  }
}

public class Day9
{
    public void solveDay()
  {
    // a 6067 b 2471
    Console.WriteLine("Day 9: " + "a sultion: " + a().ToString() + " b solution: " + b().ToString());
  }

  public int a()
  {
    Dictionary<string, Coord> TailPos = new Dictionary<string, Coord>();
    TailPos.Add("-2,0", new Coord(-1, 0));
    TailPos.Add("0,-2", new Coord(0, -1));
    TailPos.Add("2,0", new Coord(1, 0));
    TailPos.Add("0,2", new Coord(0, 1));
    TailPos.Add("-2,-1", new Coord(-1, -1));
    TailPos.Add("-1,-2", new Coord(-1, -1));
    TailPos.Add("1,-2", new Coord(1, -1));
    TailPos.Add("2,-1", new Coord(1, -1));
    TailPos.Add("1,2", new Coord(1, 1));
    TailPos.Add("2,1", new Coord(1, 1));
    TailPos.Add("-1,2", new Coord(-1, 1));
    TailPos.Add("-2,1", new Coord(-1, 1));
    TailPos.Add("-2,-2", new Coord(-1, -1));
    TailPos.Add("-2,2", new Coord(-1, 1));
    TailPos.Add("2,-2", new Coord(1, -1));
    TailPos.Add("2,2", new Coord(1, 1));

    string[] input = File.ReadAllLines("./src/2022/input/day9.txt");

    HashSet<string> visited = new HashSet<string>();
    visited.Add("0,0");

    Coord[] snake = {
        new Coord(0, 0), //H
        new Coord(0, 0)  //T
    };

    foreach (string line in input)
    {
      string direction = line.Split(' ')[0];
      int steps = Convert.ToInt32(line.Split(' ')[1]);

      for (int i = 0; i < steps; i++)
      {
        switch (direction)
        {
          case "U":
            snake[0].y--;
            break;
          case "D":
            snake[0].y++;
            break;
          case "L":
            snake[0].x--;
            break;
          case "R":
            snake[0].x++;
            break;
        }

        for (int j = 1; j < snake.Length; j++)
        {
          Coord diff = new Coord(snake[j - 1].x - snake[j].x, snake[j - 1].y - snake[j].y);

          //Coord moveDir = TailPos[diff.coordString()];
          Coord moveDir = new Coord(0,0);
          if(TailPos.TryGetValue(diff.coordString(), out moveDir))
          {
            snake[j].x += moveDir.x;
            snake[j].y += moveDir.y;

            if (j == snake.Length - 1)
            {
              visited.Add(snake[j].coordString());
            }
          }
          else
          {
            continue;
          }
        }
      }
    }

    return visited.Count;
  }

   public int b()
  {
    Dictionary<string, Coord> TailPos = new Dictionary<string, Coord>();
    TailPos.Add("-2,0", new Coord(-1, 0));
    TailPos.Add("0,-2", new Coord(0, -1));
    TailPos.Add("2,0", new Coord(1, 0));
    TailPos.Add("0,2", new Coord(0, 1));
    TailPos.Add("-2,-1", new Coord(-1, -1));
    TailPos.Add("-1,-2", new Coord(-1, -1));
    TailPos.Add("1,-2", new Coord(1, -1));
    TailPos.Add("2,-1", new Coord(1, -1));
    TailPos.Add("1,2", new Coord(1, 1));
    TailPos.Add("2,1", new Coord(1, 1));
    TailPos.Add("-1,2", new Coord(-1, 1));
    TailPos.Add("-2,1", new Coord(-1, 1));
    TailPos.Add("-2,-2", new Coord(-1, -1));
    TailPos.Add("-2,2", new Coord(-1, 1));
    TailPos.Add("2,-2", new Coord(1, -1));
    TailPos.Add("2,2", new Coord(1, 1));

    string[] input = File.ReadAllLines("./src/2022/input/day9.txt");

    HashSet<string> visited = new HashSet<string>();
    visited.Add("0,0");

    Coord[] snake = {
        new Coord(0, 0), //H
        new Coord(0, 0),
        new Coord(0, 0),
        new Coord(0, 0),
        new Coord(0, 0),
        new Coord(0, 0),
        new Coord(0, 0),
        new Coord(0, 0),
        new Coord(0, 0),
        new Coord(0, 0)  //T
    };

    foreach (string line in input)
    {
      string direction = line.Split(' ')[0];
      int steps = Convert.ToInt32(line.Split(' ')[1]);

      for (int i = 0; i < steps; i++)
      {
        switch (direction)
        {
          case "U":
            snake[0].y--;
            break;
          case "D":
            snake[0].y++;
            break;
          case "L":
            snake[0].x--;
            break;
          case "R":
            snake[0].x++;
            break;
        }

        for (int j = 1; j < snake.Length; j++)
        {
          Coord diff = new Coord(snake[j - 1].x - snake[j].x, snake[j - 1].y - snake[j].y);

          //Coord moveDir = TailPos[diff.coordString()];
          Coord moveDir = new Coord(0,0);
          if(TailPos.TryGetValue(diff.coordString(), out moveDir))
          {
            snake[j].x += moveDir.x;
            snake[j].y += moveDir.y;

            if (j == snake.Length - 1)
            {
              visited.Add(snake[j].coordString());
            }
          }
          else
          {
            continue;
          }
        }
      }
    }

    return visited.Count;
  }
}

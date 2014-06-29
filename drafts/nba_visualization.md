Title: Visualizing NBA Playoffs (Part 1)
Date: 2014-06-04
Category: blog
Tags: visualization, R, python, ggplot
Slug: visualizing-nba-playoffs
Author: Nick Jones
Summary: Coming up with ways to visualize the trajectory of a basketball game

(Note that I originally wrote the scraper/initial visualization code for 
the NCAA tournament. Some of the article below repeats concepts described 
in the NCAA post. Read about it 
[here](http://blog.nrjones8.com/visualizing-march-madness.html)

I've missed out on watching a lot of the NBA playoffs -- one of the goals of this 
visualization is to see what games were good (i.e. not blowouts), and how the 
trajectories of games changed over the course of a best-of-7 series. 

The goals:

1. Visualize the trajectory of a game
2. Compare the trajectories of one game to another
3. Cluster games?

# Scraping Play by Play Data

In order to see plot a game, we need to create a time series of the game -- 
for any given time in the game, what was the score? ESPN provides play-by-play 
data for every game (for example, http://espn.go.com/nba/playbyplay?gameId=400556334) 
which we can use to parse out the score at any given time. Using Python's `requests` 
and `BeautifulSoup` libraries make this a whole lot easier. Check out 
[this gist](https://gist.github.com/nrjones8/9821474) to see the full scraper's code 
(or view it in my [repo](https://github.com/nrjones8/game-visualizer/blob/master/scraper.py)).

The scraper outputs a .csv file containing events from all the playoff games played so far. 
Each event stores the teams involved, metadata about the teams (their rank), 
the round number, the time, and scores. Note that we'll be interested in looking 
at the _difference_ in scores at a given time; since we expect a higher ranked 
team to be winning, the `diff_score` variable used throughout is with respect to
the higher ranked team, i.e. `score of higher ranked team - score of lower ranked team.`
An example (with header included) of a few events from the Nets vs. Raptors series 
is shown below:
```
away,away_rank,away_score,diff_score,game_id,home,home_rank,home_score,rank_diff,round_num,series_id,time
BKN, 6, 3, -3, TOR-BKN-1, TOR, 3, 0, 3, 1, TOR-BKN, 0.0
BKN, 6, 3, -3, TOR-BKN-1, TOR, 3, 0, 3, 1, TOR-BKN, 0.25
BKN, 6, 5, -5, TOR-BKN-1, TOR, 3, 0, 3, 1, TOR-BKN, 0.5
BKN, 6, 5, -5, TOR-BKN-1, TOR, 3, 0, 3, 1, TOR-BKN, 0.75
BKN, 6, 5, -5, TOR-BKN-1, TOR, 3, 0, 3, 1, TOR-BKN, 1.0
BKN, 6, 5, -5, TOR-BKN-1, TOR, 3, 0, 3, 1, TOR-BKN, 1.25
...
```

# Analyzing the Data

Note that the scraper's output gives uniform time intervals. In other words,  
we define each event to happen every 15 seconds to allow us to compare games more easily. 

As with the NCAA data, R (with [RStudio](https://www.rstudio.com/) and [ggplot2]
(http://ggplot2.org/) are perfect to start messing with the data

* Individual games -- what teams are involved? The above plot doesn't show this well. 
* "Fairness" of game -- how different are teams' ranks?
* Trajectory of game -- was it close, a blowout, or had sections of each?

# Heatmap

Which brings us to the heatmap, which is a great way to visualize many variables at once.
The below heatmap ([larger version](https://raw.githubusercontent.com/nrjones8/game-visualizer/master/figures/heatmap_3_31.png)) 
does a much better job of capturing all the above aspects, though it requires a little more explanation. 

<a href="https://raw.githubusercontent.com/nrjones8/game-visualizer/master/figures/heatmap_3_31.png">
  <img src="images/heatmap_3_31.png" style="width: 800px;"/>
</a>

* X-axis is time
* Each row corresponds to a game (with the teams/game number shown on the far left)
* The color of each cell is based on the score differential of the given game at the 
given time -- blue means the favorite is winning by a lot, red means the underdog 
is winning by a lot, and closer to white means the game is close. (Note that any lead of 
over 15 is rounded down, since we'd like the colors to be distinguishable at lower differentials).
* The rows are ordered! As shown on the right side of the map, rows are grouped by the rank differential of the game -- games between teams with a rank differential of 3 are plotted together etc. Thus, in the bottom rows we would expect to see lots of blue (since the higher ranked team is _much higher_ ranked). Any place we see red means an upset -- the lower the red is on the map, the more of an upset it was. 

Thing to note:
* "Home field advantage" looks to be (anecdotally) present. In a lot of series, we see
team A blow out team B in one game, and team B blow out team A in the next. For example,
consider the SA-OKC series. SA won game 1 by 17 points and game 2 by 35, but then
then then lost game 3 by 9 and game 4 by 13. 
* On the other hand, some series were much closer throughout. Despite being a
1 seed vs. an 8 seed, the SA-DAL series had much closer games in general.



For example, the Duke vs. Mercer game was an upset, since Duke was 11 seeds higher than Mercer. By looking at the MER-DUKE row, we can see that it was a good game -- each team had the lead for some time, but it switched often (as shown by the shift back and forth from red and blue). Similarly, Virginia had a tough time with Coastal Carolina for a while, as shown by the red cells in the first 2/3 of the CCAR-UVA game. On the other hand, Pitt-Colorado game wasn't particularly interesting -- Pitt was winning big the whole game, as shown by the constant red in their row. 

The code for making the above plots isn't too tough -- here's the heatmap:

```S

  head(df)

    away away_rank away_score diff_score game_id home home_rank home_score rank_diff round_num time
  1  DAY        11          0          2 DAY-OSU  OSU         6          2         5         2 0.00
  2  DAY        11          0          2 DAY-OSU  OSU         6          2         5         2 0.25
  3  DAY        11          0          2 DAY-OSU  OSU         6          2         5         2 0.50
  4  DAY        11          0          5 DAY-OSU  OSU         6          5         5         2 0.75
  5  DAY        11          0          5 DAY-OSU  OSU         6          5         5         2 1.00
  6  DAY        11          3          2 DAY-OSU  OSU         6          5         5         2 1.25
   # Column for rounded scores -- anything over <max_score> will be the same color
  df$rounded_diff_score <- sapply(df$diff_score, function(score) {
    ifelse(score > 0, min(score, max_score), max(score, -max_score))
  })

  # Thanks to tutorial here: http://learnr.wordpress.com/2010/01/26/ggplot2-quick-heatmap-plotting/
  # Also good: http://quantcorner.wordpress.com/2013/11/02/creating-a-heatmap-to-visualize-returns-with-r-ggplot2/

  heat <- ggplot(df, aes(time, game_id)) +
    geom_tile(aes(fill = rounded_diff_score), color = 'white') +
    scale_fill_gradient2("Score Differential", low = 'red', high = 'blue') +
    facet_grid(rank_diff ~ ., scales = 'free', space = 'free', labeller=rank_diff_label) +
    theme_bw() +
    # Horizontal text on the facet
    theme(strip.text.y = element_text(size = 9, angle = 0)) +
    scale_x_continuous('Time') +
    scale_y_discrete('Teams') +
    ggtitle('NCAA 2014: Rounds 2 and 3')

  print(heat)

```

* overtime


All the plotting code is available [here](https://github.com/nrjones8/game-visualizer/blob/master/visualize.R) if you're curious! Feel free to follow me on Twitter @nrjones8 for more posts in the future. 
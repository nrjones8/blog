Title: About Me
Category: about
Tags: about, meta
Slug: about
Author: Nick Jones
Summary: Information about this blog
url: index.html
save_as: index.html

Hello humans! I'm a Software Engineer interested in government, media, data visualization, and how to use data responsibly in decision-making and writing. In the past, I've worked on improving government services at [Nava](https://navapbc.com), and built tools to help local professionals grow their businesses at [Thumbtack](https://www.thumbtack.com).

## Projects
<link href="static/about-styles.css" rel="stylesheet"></link>

<div class="projects-grid-container">
  <!-- Robots.txt -->
  <div class="project-grid-item">
    <h4 class="project-title">
      <a href="https://robots-dot-txt-db.com/" target="_blank">Robots.txt Database <i class="fa fa-external-link"></i></a>
    </h4>
    <p class="project-description">
    A project that collects robots.txt files from websites across the internet, making them searchable and available for researchers to query or download in bulk. Starting with a focus on 9000+ state, local, and federal government websites. Access the raw data <a href="https://github.com/nrjones8/robots-dot-txt-archive-bot" target="_blank">on Github</a>, or search across all 9000+ robots.txt files <a href="http://robots-dot-txt-db.com/" target="_blank">here</a>.
    </p>
    <img class="project-img" src="https://github.com/nrjones8/blog/blob/master/content/images/robots_dot_txt_db_screenshot.png?raw=true">
  </div>
  <!-- News archive explorer -->
  <div class="project-grid-item">
    <h4 class="project-title">
      <a href="https://nrjones8.github.io/news-archive-explorer/" target="_blank">Hourly News Homepage Archive <i class="fa fa-external-link"></i></a>
    </h4>
    <p class="project-description">
    An archive that captures what the front page of various news websites show. Screenshots are taken <b>every hour</b> starting January 1, 2019 and continually updated. To access the raw screenshots directly, see <a href="https://github.com/nrjones8/website-screenshotter" target="_blank">Github</a>, or browse the screenshots <a href="https://nrjones8.github.io/news-archive-explorer/" target="_blank">here</a>.
    </p>
    <img class="project-img" src="https://github.com/nrjones8/blog/blob/master/content/images/news_homepage_archive_screenshot.png?raw=true" >
  </div>
  <!-- EEOC violations on job boards -->
  <div class="project-grid-item">
    <h4 class="project-title">
      <a href="https://github.com/nrjones8/eeoc-job-violations" target="_blank">Discriminatory Postings on Online Job Boards <i class="fa fa-external-link"></i></a>
    </h4>
    <p class="project-description">
    Online job boards are an increasingly common way for people to find jobs. How do platforms like ZipRecruiter handle potentially discriminatory job postings? I wrote code to collect job postings that have potential EEOC (Equal Employment Opportunity Commission) violations against people with criminal records, where companies include blanket exclusionary statements like "No Criminal Background" in their job descriptions. Data and writeup available <a href="https://github.com/nrjones8/eeoc-job-violations" target="_blank">on Github</a>.
    </p>
    <img class="project-img" src="https://github.com/nrjones8/blog/blob/master/content/images/ziprecruiter_no_felony_screenshot.png?raw=true">
  </div>
  <!-- SF Ballot Props -->
  <div class="project-grid-item">
    <h4 class="project-title">
      <a href="https://sfprops.shinyapps.io/historical/" target="_blank">Historical SF Ballot Props Explorer <i class="fa fa-external-link"></i></a>
    </h4>
    <p class="project-description">
    Most years, San Franciscans vote on ballot measures determining whether or not police should carry tasers, to allocate $50 million a year for homeless services, or to impose a fee on ride-hailing apps to support public transit. In some years, voters make decisions on over 30 propositions at the local, regional or state level. I built an interactive tool to help people explore 40+ years of ballot propositions and their outcomes, available <a href="https://sfprops.shinyapps.io/historical/" target="_blank">here</a>, and wrote about the process of building the interactive for <a href="https://www.storybench.org/how-i-visualized-hundreds-of-ballot-proposition-outcomes-with-r-shiny/" target="_blank">Storybench</a>.
    </p>
    <img class="project-img" src="https://github.com/nrjones8/blog/blob/master/content/images/ballot_props_screenshot.png?raw=true">
  </div>
  <!-- CA prison overcrowding -->
  <div class="project-grid-item">
    <h4 class="project-title">
      <a href="https://nrjones8.me/measuring-prison-overcrowding.html" target="_blank">Misleading Prison Overcrowding Statistics in California <i class="fa fa-external-link"></i></a>
    </h4>
    <p class="project-description">
      Since <a href="https://en.wikipedia.org/wiki/Brown_v._Plata" target="_blank">2011</a>, California has been under a court-mandated reduction of its prison population to 137.5% of its designed capacity. In order to track progress of <b>individual</b> prisons over time, I built a tool to parse <a href="https://sites.cdcr.ca.gov/research/population-reports/monthly-total-population-report-archive/" target="_blank">PDFs published monthly by the CDCR</a> and aggregate monthly population data into one easily-analyzable CSV.
    </p>
    <p class="project-description">
      The data and code are <a href="https://github.com/nrjones8/cdcr-population-data" target="_blank">on Github</a>; I also <a href="https://nrjones8.me/measuring-prison-overcrowding.html" target="_blank">wrote about</a> why the court's definition of "overcrowding" as an average across 35 prisons is extremely problematic, as many individual prisons have continued to house upwards of 160% of their designed capacities.
    </p>
    <img class="project-img" src="https://github.com/nrjones8/blog/blob/master/content/images/ca_prison_overcrowding_screenshot.png?raw=true" >
  </div>
  <!-- MUNI Citations -->
  <div class="project-grid-item">
    <h4 class="project-title">
      <a href="https://www.storybench.org/using-r-to-explore-the-relationship-between-san-francisco-muni-citations-and-the-weather/" target="_blank">MUNI's increased ticketing on rainy days <i class="fa fa-external-link"></i></a>
    </h4>
    <p class="project-description">
    Published on Storybench, an investigation into the relationship between bad weather and the number of citations handed out by MUNI. Using data obtained via records request from MUNI, I found an increased rate of citations on days that it rained vs. those when it didn't.
    </p>
    <img class="project-img" src="https://github.com/nrjones8/blog/blob/master/content/images/boxplot_by_weather_day.png?raw=true" >
  </div>
  <!-- BART viz -->
  <div class="project-grid-item">
    <h4 class="project-title">
      <a href="http://bl.ocks.org/nrjones8/20ed209849bc61104c4574a4543439ad" target="_blank">BART Ridership Visualizations <i class="fa fa-external-link"></i></a>
    </h4>
    <p class="project-description">
    A treemap visualization of weekday BART ridership. Data came from combining .xlsx data published by BART, see <a href="https://github.com/nrjones8/bart-ridership" target="_blank">Github</a> for raw data.
    </p>
    <img class="project-img" src="https://github.com/nrjones8/blog/blob/master/content/images/bart_weekly_ridership_screenshot.png?raw=true" >
  </div>
</div>

## Contacting me

If you'd like to follow along with new posts, provide feedback on any of my projects, or otherwise contact me, you can find me elsewhere - I would love to hear from you!

* [Twitter](https://twitter.com/nrjones8)
* [Github](https://github.com/nrjones8)
* nrjones8@gmail.com

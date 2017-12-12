Title: The odds stacked against defendants (err...)
Date: 2017-12-10
Category: blog
Tags: visualization, R, ggplot, criminal justice
Slug: california-public-defenders-understaffed
Author: Nick Jones
Summary: foo fooo foooooo


> The fundamental right to a lawyer that Americans assume apply to everyone accused of criminal conduct effectively does not exist in practice for countless people across the United States.

> [Gideon's Broken Promise: America's Continuing Quest for Equal Justice](https://www.americanbar.org/content/dam/aba/administrative/legal_aid_indigent_defendants/ls_sclaid_def_bp_execsummary.authcheckdam.pdf), American Bar Association, December 2004


People are generally aware of the landmark case "Gideon v. Wainwright" from 1963 which granted the right to an attorney - if the accused couldn't afford an attorney, one would be appointed. But people are generally less aware of what that actually means, or the fact that roughly 80% of those accused of felonies cannot afford an attorney [cite this]. I hope to write a longer post some time about how Gideon is actually implemented the short version is:

* Implementation varies widely by state - some public defender offices are run by the state, some by each county
* There are no formal rules for determining who "can't afford" an attorney
* Many states still require defendants to pay an application fee and / or a "recoupment" fee
* Public Defenders offices are always overloaded, forcing some to even downright turn away clients for lack of resources (reword).

The "adversarial" system that the American legal system relies upon is not really all that fair - district attorneys have better resources, more people, and complete discretion of what cases they take on, leaving Public Defenders (and their clients) at a <drastic?> disadvantage. [could cite Pfaff on discretion piece]

In this post, we'll take a look at a simple comparison of resources in California, one of X states that administers indigent defense at the county level.

 the California DOJ has a number of interesting datasets available, including county-level data on number of employees in the District Attorney's Office and in the Public Defender's Office. Given that roughly 80% of defendants need a public defender, a "fair" (albeit oversimplified) system would staff the Public Defender's Office with 80% of the employees of the District Attorney's Office <further explanation needed?>. Unsurprisingly, this is not the case.

## A look at the data
While it's great that the DOJ provides this type of data, it is not the cleanest dataset. Tracking 58 counties from 2004 until 2016, there were only 32 counties that actually reported data on their Public Defender's office - it's unclear why the remaining 26 counties don't have this data, though the README for this dataset included a vague explanation:
>  Zero's may indicate that a department or office does not have personnel in that classification, that a department may have closed or merged with another, that a county may not have a police department or a public defender's office, or that data were not reported.

Of those that did report data, let's compare the size of the public defender's office with the size of the district attorney's office. The plot below shows that relationship; each point represents one particular county in one particular year (looking at all years and counties we have data for between 2004 and 2016). I've included two other lines: one showing "equal" sizes for the two offices (i.e. if the same number of people were employed by the DA as the PD), and one showing 80% (i.e. if the PD office had 80% the number of employees that the DA office had).



<scatterplot here>



As is clear from the plot above, public defender's offices are consistently understaffed relative to the staffing of a district attorney's office. In 2016, the median public defender's office had 43% the staff that a district attorney's office had [footnote and explain what "median" means here]. If we take the "80% rule" above as fact, then public defender's offices are handling at least 2X as many cases / employee as the district attorney's office. It should be noted that these are rather rough estimates - comparing total employees is a very simplistic way of comparing "resources." In fact, prosecutors' offices and budgets underestimate their "advantage" over public defenders, since prosecutors also have law enforcement agencies on their "side":

"Moreover, prosecutor budgets understate prosecutors' competitive advantage, since unlike defense attorneys, prosecutors do not have to pay for their investigative services, which are provided directly by the police, sheriffs, and other law enforcement agencies. A study in North Carolina found that accounting for these sorts of services effectively tripled the amount spent on prosecution in that state."

Pfaff, John. Locked In: The True Causes of Mass Incarceration�and How to Achieve Real Reform (Kindle Locations 2226-2232). Basic Books. Kindle Edition.


## Is this a fair comparison?
* What additional roles do both offices play?
* E.g. prosecutors have law enforcement to help with investigations
* E.g. public defenders are often the ones trying to help people clear their records
> Alameda County Deputy Public Defender Sue Ra said her office hasn’t received any additional funding for post-conviction relief services, which could help attorneys reach more people and process their petitions faster.“Somebody needs to do this work, and the public defenders are on the ground actually doing it,” Ra said. “It would be nice to get the support to allow us the resources to complete work quickly so that our clients don’t miss out on employment and other opportunities.”

https://www.themarshallproject.org/2017/11/27/how-do-you-clear-a-pot-conviction-from-your-record

## But isn't budget the real question? Maybe they're funded similarly, but the PD is spending differently?
Lol no.

## Some particularly bad counties

### News articles on Fresno
foo

### San Luis Obispo County (SLO)
SLO was missing data on public defenders for 2016 - according to the [SLO county website](http://www.slocounty.ca.gov/Departments/Administrative-Office/Services/Public-Defender-Services-(for-individuals).aspx)

> The County contracts with private attorneys to provide Public Defender services. The County’s primary Public Defender firm is San Luis Obispo Defenders.

The [San Luis Obispo Defenders website](http://www.slodefend.com/about-us/) reports having 37 total staff:
> Today we have 23 attorneys, 5 investigators, 4 paralegals, one social worker, and a support staff of 4 who handle in excess of over 7,000 cases a year.

In 2016, SLO's had 93 total prosecutors according to DOJ data, leaving the public defender with just 40% of the staff of the district attorney.

### San Mateo
I think there's is supposed to be particularly good?
http://www.smcgov.org/private-defender-program
https://www.smcba.org/wp-content/uploads/2017/12/Annual-Report-FY-2016-2017_FINAL_Digital.pdf


## Why does this matter?
"Prosecutors have a huge carrot to use with defendants who can't make bail: plead guilty now, and the sentence recommendation will be for time already served in jail. A defendant faced with such an offer has to decide if staying in prison and fighting for an acquittal is worth more than just walking home that afternoon. It's a very powerful card for the prosecutor to hold."

Pfaff, John. Locked In: The True Causes of Mass Incarceration�and How to Achieve Real Reform (Kindle Locations 4805-4808). Basic Books. Kindle Edition.

No representation? Client has no idea what to do. Only a tiny bit of time? Well, the quickest way to "handle" a case is to get a quick plea.



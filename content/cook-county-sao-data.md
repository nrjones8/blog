Title: Cook County SAO Dispositions - Direct Filing and Narcotics Cases
Date: 2017-11-30
Category: blog
Tags: R, ggplot
Slug: cook-county-sao-dispositions
Author: Nick Jones
Summary: The Cook County State's Attorney's Office released an interesting dataset on how their prosecutors have handled thousands of cases since 2011. It turns out that narcotics cases are initiated differently from all other types of cases - this article explores how "direct filing" leads to a significant number of narcotics cases being dismissed. What would happen if those defendants weren't charged to begin with?

> We have extensive data on crimes, arrests, and prison populations, but when it comes to prosecutors we have next to nothing...We have no comprehensive data on such basic issues as the number of cases resolved by plea bargaining, the number of cases dismissed by prosecutors or judges, or the demographics of line prosecutors—and how those might interact with the demographics of defendants or defense counsel.

> &mdash; John Pfaff, author of Locked In: The True Causes of Mass Incarceration, Kindle Locations 2582-2587

As John Pfaff notes in his [recent book _Locked In_](https://www.goodreads.com/book/show/29502356-locked-in), it's hard to come across data on prosecutors. When Cook County State's Attorney Kim Foxx released a dataset and report on how the State's Attorney's Office (SAO) had handled felony cases over the past six years, I was excited to take a look at some of the data. The [report itself](https://www.cookcountystatesattorney.org/sites/default/files/files/documents/ccsao-data-report-oct-2017.pdf) looks just at data from 2016, while there are a number of datasets released for data starting in 2011.

The report is pretty detailed, and provides a lot of helpful context on what the data mean and don't mean. It also provides some great visual explanations of how a case moves through the SAO - from arrest to initiation to pre-trail to a disposition to sentencing. I was particularly curious about dispositions, but noticed that the "Disposition" section excluded an analysis / breakdown of narcotics cases. This post looks into how narcotics cases are treated differently, and why the report may have left those cases out of their disposition analysis.

All data used below came from the [State's Attorney Felony Cases - Disposition Outcomes By Offense Type and Defendant Race](https://datacatalog.cookcountyil.gov/Courts/State-s-Attorney-Felony-Cases-Disposition-Outcomes/cqdb-r84f) dataset, and the code used to calculate numbers and generate graphics can be found [here](https://github.com/nrjones8/cook-county-states-attorney/blob/master/analysis.R). For a more detailed explanation of the code, please see [a second post I wrote on the topic](http://nrjones8.me/dplyr-intro-sao-data.html).

## How Narcotics Cases are Initiated
The report notes that narcotics cases are initiated differently from all other cases. Non-narcotics cases go through either (1) Felony review (where attorneys at the SAO decide whether or not to prosecute) or (2) a grand jury. There's a brief explanation (and helpful flowchart) of these differences on page 4 of the report, part of which is reproduced below.

![Case initiation process](images/initiation_process.png "Case initiation process")

Narcotics cases, however, are filed directly by law enforcement - they do not go through felony review or a grand jury. On page 6, the "Initiations" section explains:

> Law enforcement may directly file charges in narcotics cases without FRU approval. The first time the SAO has any involvement in those cases is at preliminary hearing. In the data these are referred to as "bond set" cases.

As a result, comparing the dispositions of narcotics cases (vs. other types of cases, such as retail theft, DUIs, etc.) would not be a fair comparison.

For example, looking at all dispositions in the provided data (2011 - 2016), cases labeled as "Narcotics” led to a guilty plea just 43% of the time, compared to 75% of the time for all other types of cases. That is quite different from what I'd expect to see, since plea bargains are generally quoted to happen in the vast majority of cases. See, e.g. [this report from the Human Rights Watch](https://www.hrw.org/report/2013/12/05/offer-you-cant-refuse/how-us-federal-prosecutors-force-drug-defendants-plead) - it focuses on federal drug cases, but the general trend of pleas holds at the state level as well.

That suggests that we need to take a closer look at the data - there are likely more narcotics cases making to the "disposition” stage than other types of cases.
## Narcotics Dispositions
Looking at all narcotics data (years 2011 - 2016), the data start to make sense. The table below shows the most common narcotics dispositions, along with the most common dispositions for _non_-narcotics cases.

<table border=1 frame=void rules=rows>
    <thead>
        <tr>
        <th>Disposition</th>
        <th align="center">Number of narcotics cases</th>
        <th align="center">% of all narcotics cases</th>
        <th align="center">Number of non-narcotics cases</th>
        <th align="center">% of all non-narcotics cases</th>
        </tr>
    </thead>
    <tbody>
    <tr>
        <td>Plea Of Guilty</td>
        <td align="center">43,782</td>
        <td align="center">43%</td>
        <td align="center">95,049</td>
        <td align="center">75%</td>
    </tr>
    <tr>
        <td>FNPC</td>
        <td align="center">26,911</td>
        <td align="center">26%</td>
        <td align="center">3,363</td>
        <td align="center">3%</td>
    </tr>
    <tr>
        <td>Nolle prosequi</td>
        <td align="center">26,365</td>
        <td align="center">26%</td>
        <td align="center">12,565</td>
        <td align="center">10%</td>
    </tr>
    <tr>
        <td>Finding guilty</td>
        <td align="center">2,045</td>
        <td align="center">2%</td>
        <td align="center">6,567</td>
        <td align="center">5%</td>
    </tr>
    <tr>
        <td>Finding not guilty</td>
        <td align="center">1,735</td>
        <td align="center">2%</td>
        <td align="center">4,646</td>
        <td align="center">4%</td>
    </tr>
    </tbody>
</table>

<br />

As we would expect, "Plea of Guilty” is most common. But the more interesting classifications are the next two most common - FNPC ("Finding of no probable cause”) and Nolle prosequi (the SAO chose not to proceed). This seems to explain why we thought that narcotics cases had such a lower rate of guilty pleas. A narcotics charge does not get initiated through felony review or a grand jury, resulting in a significant number of cases being initiated that end up being dismissed (either by a finding of no probable cause, or the prosecution simply choosing not to proceed). In non-narcotics cases, more of these cases wouldn't even reach initiation - they wouldn't make it past a grand jury or felony review by the SAO.

If we remove the "FNPC" and "Nolle prosequi" cases, we end up seeing pretty similar plea rates in narcotics vs. non-narcotics cases. In 2016, 85% of narcotics cases ended in a guilty plea, while 82% of non-narcotics cases ended in a guilty plea.

## Why don't narcotics cases go through felony review or a grand jury?
I researched this a bit - there is a [2012 research report on "Policies and Procedures of the Illinois Criminal Justice System](http://www.icjia.state.il.us/assets/pdf/ResearchReports/Policies_and_Procedures_of_the_Illinois_Criminal_Justice_System_Aug2012.pdf) but that lacked any reference to direct filings. Cook County's ["Guide to the Criminal Justice System"](https://www.cookcountyil.gov/service/guide-criminal-justice-system) also doesn't mention direct filings.

What I could find simply suggested that direct filing by law enforcement was a choice that a state attorney's office could make. I found a reference from 2010 in the _CHRI User's Manual_ (full manual available [here](http://www.isp.state.il.us/docs/5-336e.pdf)), which reads:

> State's attorney's offices may allow local agencies to direct file criminal charges with the circuit court clerk. The state's attorney must submit a letter describing the circumstances where local agencies may direct file criminal charges. State's attorneys do not need to submit paper copies of filing decisions for charges that have been determined to be direct filed, however paper submissions are required for other filing decisions. These filing decisions will automatically appear on the subject's criminal history record.

I spoke briefly with the SAO on the phone, and they provided some helpful context. The direct filing of narcotics cases in Cook County has existed for some time for a few reasons:

1. Narcotics cases are somewhat simpler than many other types of cases. A police officer arrests someone for possession of a controlled substance, and that person either has that substance or doesn't - an initial Felony Review in such cases wouldn't provide much extra benefit. I do not mean to suggest that narcotics cases as a whole are simple; just that an initial review of a case by the SAO may not provide much added value. An attorney from the SAO can provide more value at a preliminary hearing, with access to more information and context on the case.

2. There are a _lot_ of narcotics cases. 8,777 out of a total of the 30,505 total cases considered in 2016 were narcotics cases. Adding an additional 8,777 cases to Felony Review would take a lot of time from SAO attorneys.

It should be noted that defendants in narcotics cases _do_ go through a bond hearing. For lower level offenses, most defendants aren't detained pre-trial or forced to post bail - but some are. While the report provided a lot of detail already, it did not provide data at this granularity. If such cases instead went through the Felony Review process, then presumably fewer cases would be initiated - more importantly, those defendants wouldn't have gone through a bond hearing or preliminary hearing.

## Conclusion

I was pleasantly surprised to have the opportunity to talk directly with the SAO to get a better understanding of the direct filing process. Their responsiveness, release of this report, and release of accompanying data is an encouraging sign of transparency, especially from a part of the criminal justice system that generally lacks much detailed data.

If you have questions, comments, or otherwise want to talk, please [reach out via Twitter or email](http://nrjones8.me/about.html). Thanks for reading!

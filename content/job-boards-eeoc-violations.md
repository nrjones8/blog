Title: Criminal Record Discrimination on Online Job Boards
Date: 2018-04-22
Category: blog
Tags: eeoc, ziprecruiter
Slug: job-boards-eeoc-violations
Author: Nick Jones
Summary: Online job boards are an increasingly common way for people to find jobs. How do platforms like ZipRecruiter and Indeed handle potentially discriminatory job postings? This post looks specifically at EEOC (Equal Employment Opportunity Commission) violations against people with criminal records, where companies include blanket exclusionary statements like "No Criminal Background" in their job descriptions - and describes a dataset of potential violations on ZipRecruiter.

## Discrimination in Hiring - EEOC Guidelines

While criminal justice reforms often focus on ending mass incarceration, the problems of American criminal justice policy extend beyond the almost [2.3 million incarcerated people](https://www.prisonpolicy.org/reports/pie2018.html) in the United States today. [A 2015 report](https://www.sentencingproject.org/wp-content/uploads/2015/11/Americans-with-Criminal-Records-Poverty-and-Opportunity-Profile.pdf) from The Sentencing Project estimates that as many as **100 million Americans have criminal records** - and over 60% of formerly incarcerated individuals are unemployed one year after being released.

Not surprisingly, it’s more difficult for people with a criminal record to get a job - but there are laws that in theory protect people with a criminal record from being discriminated against. The Equal Employment Opportunity Commission (EEOC) issued guidance dating back to 1987 that employers are not allowed to bar people from employment based _solely_ on their criminal records - because the criminal justice system disproportionately impacts people of color, a policy of barring anybody with a criminal record from employment would disproportionately bar people of color from getting jobs.

The National Employment Law Project (NELP) gives a much more detailed analysis of EEOC’s guidance in [their 2015 report](http://www.nelp.org/content/uploads/2015/03/65_Million_Need_Not_Apply.pdf) _65 Million "Need Not Apply": The Case for Reforming Background Checks for Employment_. Instead, an employer must consider an _individual’s_ criminal history, how that individual has changed, and how such a history relates to the job the person is applying for.

Many companies, however, completely ignore the EEOC’s guidance - the NELP report mentioned above found that even huge companies like Bank of America, Aramark, Lowe’s, and more impose overbroad background checks. And it still happens today - earlier this month, the Prison Policy Initiative reported that [Target had agreed to a settlement](https://www.prisonpolicy.org/blog/2018/04/11/target_settlement/) in a discriminatory hiring lawsuit in which Target denied employment to over 41,000 Black and Latinx job applicants between 2008 and 2016, simply because they had a criminal record.

## EEOC Violations Online
Job search sites ("job boards") are one common way for job-seekers to find work; sites like [Indeed](https://www.indeed.com/) report having over 200 million visitors per month, while [ZipRecruiter](https://www.ziprecruiter.com/) has over 200 million active job seekers, according to [Proven](https://blog.proven.com/100-best-job-boards-to-find-niche-talent/). These job boards include hundreds, if not thousands, of job descriptions that violate EEOC guidelines - companies that refuse to even _consider_ candidates with criminal records. Here are a few examples from ZipRecruiter:

* [Tekk Force LLC](https://www.ziprecruiter.com/jobs/tekk-force-llc-36d08c8f/cable-puller-no-experience-required-no-criminal-background-19ab48e3?mid=3167&source=cpc-jobs2careers-uncapped): "No Experience Required/No Criminal Background"
* [Carpet Cleaning, Repair and Restoration Technician](https://www.ziprecruiter.com/jobs/authority-services-inc-2af3b51b/carpet-cleaning-repair-and-restoration-technician-39339c8c): "Have a clean criminal background (No felony convictions)"
* [Customer Service Agent](https://www.ziprecruiter.com/jobs/bmjb-llc-wfh-solutions-1eb2f3fe/customer-service-agent-18cbcd18): "Individuals who have been convicted of or pled guilty to certain felony or misdemeanor charges, including but not limited to theft, fraud, identity theft, or other similar violations, are prohibited"
* [Airline Maintenance Manager](https://www.ziprecruiter.com/jobs/republic-airline-44ff5892/airline-maintenance-manager-7a2f3e19): "No previous felony convictions and a stable employment history."
* [Shipper / Packer](https://www.ziprecruiter.com/ojob/789649506b59cf88078f6ecbd55dcc75?mid=278&source=directemployersassociation_cpc): "Be able to meet production/accuracy standards required by the facility. NO felony convictions."

These examples were taken from a dataset I assembled of ~1000 total job postings that included keywords like "felony", from 30 different cities across the United States. The entire dataset is available on [Google Sheets](http://bit.ly/zr-eeoc-data). There are a few things to note about the dataset (and how the dataset was assembled):

* The job postings came from simply searching for phrases like "felony" or "felony -driver" - so there are some job descriptions that include positive phrases like "Liberty Fleet is a FELONY FRIENDLY company." Those have not been filtered out of this dataset.
* A large portion of them (roughly 70%) are for various driver's jobs, which have a [number of (rather complicated) rules](https://helpforfelons.org/become-truck-driver-with-felony/) around past criminal histories - e.g. certain convictions disqualify you from being able to get a Commercial Driver's License.

With that said, this dataset demonstrates that there are quite a few postings that _do_ violate EEOC guidelines, such as the specific examples cited above. Estimating the impact or proportion of jobs that violate EEOC guidelines is a more complex question - this dataset is not suitable for such an analysis.

## Role of the platform
This raises a number of questions for both employers and job search platforms - while employers surely should not be violating EEOC guidance, what role does ZipRecruiter (and other job search sites) play? Should they be moderating content for such violations? It would be difficult to detect _all_ such violations, but it would not be technically difficult to flag suspicious job descriptions for human review. While there is certainly nuance to potential EEOC violations, the examples given above illustrate that such listings do exist - and a human moderator could likely be trained to remove blatantly discriminatory postings.


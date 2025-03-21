# Employer-Employee Database (1998-2013)

### `PNR`

Unique identification of person is used as key to `PERSON_ID`.

People's anonimized CPR. All CPR PNRs are converted to a unidentified PERSON_ID.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/folketal/pnr)

### `LBNR`

Unique serial number per workplace that is constant over time for preserved (not definitively closed) workplaces.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/ida-databasen/ida-ansaettelser/lbnr)


### `ARBGNR`

Workplace 12-digits Unique Code.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/arbgnr)


### `ANSAAR`

Year of employment at workplace.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-ansaettelser/ansaar)

### `ANSDAGE`

Number of days employed.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-ansaettelser/ansdage)

### `ANSXFREM`

Change of employment from the previous year to the current year for each employee. The variable thus looks forward in time to November the following year.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-ansaettelser/ansxfrem)

### `ANSXTILB`

Change in employment at the current workplace compared to the previous year for the individual employee. The variable thus looks back in time to November the year before.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-ansaettelser/ansxtilb)

### `ARBLED`

Unemployment rate in that working year (excluding holidays). Total unemployed weeks in a year divided by the total number of working weeks in a year.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ledighed---beskaeftigelsesoplysninger-der-vedroerer-ida-ansaettelser-/arbled)

### `ARBSTK`

Workplace 4-digits Code.

The code itself is not unique. Only in combination with the employer number (see `ARBGNR` under workplaces) can the individual workplace be identified. The identification is only valid for the current year and has no lasting impact on the separation of individual workplaces. For this purpose, workplace number is used (`ARDNR`)

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/arbstk)

### `JOBKAT`

Type of job.

- '1' = Full time (30 hours or more per week)
- '2' = Part time (15-29 hours)
- '3' = Bijob (under 15 hours)
- '5' = Full time (Over 8 weeks with partial unemployment during the year)
- '6' = Part-time (Over 8 weeks of partial unemployment during the year)
- '7' = Bijob (Over 8 weeks with partial unemployment during the year)
- '9' = Undisclosed

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-ansaettelser/jobkat)

### `JOBLON`

Salary linked to particular employment.

Wages in the individual employment relationship for both main and secondary employees.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/loenforhold-der-vedroerer-ida-ansaettelser-/joblon)

### `LONMFREM`

Whether an employee is an employee the following year or not.

- '0' = Not employed the following year
- '1' = Employee the following year

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-ansaettelser/lonmfrem)

### `LONMTILB`

Whether an employee is an employee the year before or not.

- '0' = Not employed the year before
- '1' = Employee the year before

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-ansaettelser/lonmtilb)

### `PERSBRC`

Personal industry code received from the Register-based Workforce Statistics (RAS). The variable is defined for principal employees, employers, self-employed and assisting spouses.

- '1XXXXX' = Agriculture, fisheries and raw material extraction
- '2XXXXX' = Manufacturing
- '3XXXXX' = Energy and water supply
- '4XXXXX' = Construction
- '5XXXXX' = Trade, hotel and restaurant business. etc.
- '6XXXXX' = Transport, Post and Telecommunications
- '8XXXXX' = Public and personal services

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-ansaettelser/persbrc)

### `STILL`

Socio-economic Job Position variable code that indicates the type of employee at the end of November (November main Job).

- '31' = Director / Top Managers
- '32' = Senior official / Employee at the highest level
- '33' = Leading functionary
- '34' = Functional in general / Medium-level employees
- '35' = Skilled worker / Basic level employees
- '36' = Non-skilled worker / Other employees
- '37' = Employed employees without further details

There are more codes in the data but the documentation do not say what they mean (e.g. 11).

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-ansaettelser/still)

### `TILKNYT`

Association with the primary place of work of the employee during working hours. Codes 10, 20 and 30 must be disregarded.

- '01' = Full time, continuous, longer than one year
- '02' = Part-time (>= 30 hours), continuous, longer than one year
- '03' = Part time (>= 20-29 hours), continuous, longer than one year
- '04' = Part time (>= 10-19 hours), continuous, longer than one year
- '05' = Part time (< 10 hours), continuous, longer than one year
- '11' = Full time, serial, longer than a year
- '12' = Part time (>= 30 hours), serial, longer than one year
- '13' = Part time (>= 20-29 hours), serial, longer than one year
- '14' = Part time (>= 10-19 hours), serial, longer than one year
- '15' = Part time (< 10 hours), serial, longer than one year
- '21' = Full time, continuous, shorter than one year
- '22' = Part-time (>= 30 hours), continuous, shorter than one year
- '23' = Part time (>= 20-29 hours), continuous, shorter than one year
- '24' = Part time (>= 10-19 hours), continuous, shorter than one year
- '25' = Part-time (< 10 hours), continuous, shorter than one year
- '31' = Full time, serial, shorter than a year
- '32' = Part time (>= 30 hours), serial, shorter than one year
- '33' = Part time (>= 20-29 hours), serial, shorter than one year
- '34' = Part time (>= 10-19 hours), serial, shorter than one year
- '35' = Part time (< 10 hours), serial, shorter than one year

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-ansaettelser/tilknyt)

### `TIMELON`

Hourly salary.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/loenforhold-der-vedroerer-ida-ansaettelser-/timelon)

### `TLONKVAL`

Quality of `TIMELON` variable. It captures the relative uncertainty of the quality of the data from `TIMELON` from 0 (no hours) to +100 (useless hourly salary).

- '0' = Number of hours employed equals 0
- '1-49' = Useful quality
- '50-99' = Doubtful quality
- '100' = Pension (ATP - Arbejdsmarkedets Tillægspension)
- '>100' = Useless quality

The relevant populations for TLONKVAL can be defined using the variable `TYPE`

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/loenforhold-der-vedroerer-ida-ansaettelser-/tlonkval)

### `TYPE`

Type of employment.

- 'A' = Employer
- 'B' = November bi job (bi-employment)
- 'E' = Not November job
- 'H' = November primary job (mainly employed)
- 'M' = Assisting spouse
- 'N' = November job
- 'S' = Self employed
- '3' = Most important not November jobs

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-ansaettelser/type)

# CBS DST Data Catalog

## Databases

TBD

https://dbdiagram.io/d

## Variable List

Variable Searching tool: https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable

List of Registry:
https://www.dst.dk/extranet/forskningvariabellister/Oversigt%20over%20registre.html

### `pnr`

Unique identification of person is used as key to `PERSON_ID`.

People's anonimized CPR. All CPR PNRs are converted to a unidentified PERSON_ID.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/folketal/pnr

### `alder`

Age.

https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/alder

### `familie_id`

Basic legal family unit. All individuals have a FAMILIE_ID.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/familier/familie-id

### `c_familie_id`

Focuses on the family links. C_FAMILIE_ID is only for coupled families, in which C_FAMILIE_ID = PERSON_ID for the mother.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/familier/c-familie-id

### `mor_id`

`PERSON_ID` of the person's mother.

https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/mor-id

### `far_id`

`PERSON_ID` of the person's father.

https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/far-id

### `efalle`

EFALLE_ID is the social security number of the person with whom a given person lives and forms a couple in the form of marriage, registered partnership, cohabiting couples or cohabiting couples.

https://www.dst.dk/da/Statistik/dokumentation/Times/forskningsservice/efalle

### `aegte_id`

Specifies the social security number ID of spouse or registered partner. There is the following connection between the person's marital status and information about the spouse:

- Married = spouse number
- Divorced = social security number of former spouse
- Widow / widower = social security number of deceased spouse
- Partnership = partner number
- Oph. partnership = social security number of former partner
- Long-term Partner = social security number of deceased partner
- Death = spouse / partner social security number

https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/aegte-id

### `bopikom`

The address in the municipality (road no., house number, house letter, floor, side / door)

https://www.dst.dk/da/Statistik/dokumentation/Times/forskningsservice/bopikom

### `kom`

Municipal code from the National Register Address.

https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/kom

### `bop_vfra`

Date of immigration.

https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/bop-vfra

### `van_vtil`

Date when immigration applies from.

A person who immigrates several times during a period is included the corresponding number of times and appears with several immigration dates.

https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/van-vtil

### `cvist`

Person's marital status (marital status). Unmarried is not included in the marital status table.

The marital code thus became from d. Oct 1 1989 expanded from 4 to 7 marital states.

- 'U' =Unmarried (not included in the marital status table)
- 'G' = Gift 'F' = Divorced
- 'E' = Widow stand The new marital status was as a result of the Registered Partnership Act
- 'P' = Registered Partnership
- 'O' = Repealed registered partnership
- 'L' = Longitudinal living of 2 partners.
- 'D' = Dead

https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/civst

### `civ_fra`

Date of the most recently recorded change of marital status (married, divorced, dead) of the person. Back to 2004, if `cvist` (marital status) is equal to U (unmarried), `civ_fra` is set equal to the date of birth.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/folketal/civ-vfra

### `familie_type`

Type of family (people of a family live at the same address).

- '1' = married couple
- '2' = Registered partnership
- '3' = Cohabiting couples
- '4' = Cohabiting couple
- '5' = Single (including non-resident children)
- '7' = Married couples different genders
- '8' = Same-sex married couples
- '9' = single
- '10' = Non-resident children

https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/familie-type

### `fm_mark`

Person cohabitation type.

- '1' = Lives with both parents
- '2' = For children: Lives with mother who is in new couple. For adults: Living with mom.
- '3' = For children: Living with single mother. For adultsThe value does not exist.
- '4' = For children: Lives with dad who is in new couple. For adults: Living with dad.
- '5' = For children: Living with single father. For adults: The value does not exist.
- '6' = Do not live with parents

https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/fm-mark

### `foedreg_kode`

Place of birth.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/folketal/foedreg-kode

### `foed_dag`

Birthday.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/folketal/foed-dag

### `ie_type`

Definitions of immigrants, descendants, and people of Danish origin, which collectively comprise entire populations, are as follows:

- '1' = Danish. People, regardless of birthplace, who have at least one parent who is both a Danish citizen and born in Denmark.
- '2' = Immigrant. People born abroad. None of the parents are both Danish citizens and born in Denmark.
- '3' = Descendant. People born in Denmark. None of the parents are both Danish citizens and born in Denmark.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/udlaendinge/ie-type

### `generation`

Whether the father and/or mother were born in Denmark or abroad.

- '0' = Danish (`ie_type` = 1)
- '1' = Parents both born abroad
- '2' = Parents both born in Denmark
- '3' = One parent born in Denmark and another abroad.
- '4' = Parental information not available.

https://www.dst.dk/da/Statistik/dokumentation/Times/cpr-oplysninger/generation

### `hustype`

Household composition.

- '1' = A single man
- '2' = A single woman
- '3' = A married couple
- '4' = A few more
- '5' = A non-resident child under 18 years
- '6' = Household of several families

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/husstande/hustype

### `koen`

Gender (CPR based).

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/folketal/koen

### `opr_land`

Code (DST based) of the country of origin.

Encoding: https://www.dst.dk/da/Statistik/dokumentation/nomenklaturer/lande-psd?

https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/opr-land

### `plads`

A person's "place" within the couple.

- '1' = Protagonist (woman)
- '2' = Partner (man)
- '3' = Resident child

In a couple, 1 is the woman (or oldest if not man/women couple), 2 the man (or youngest if not man/women couple), 3 is a person under the age of 25 who lives at the same address as at least one of his parents who has never been married or registered partner (marital status = unmarried) and who is not a father or mother of anyone who lives or has lived in Denmark.

https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/plads

### `reg`

Region of Denmark.

- '0' = Undisclosed
- '81' = North Jutland
- '82' = Central Jutland
- '83' = Southern Denmark
- '84' = Capital Region
- '85' = Zealand

https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/reg

### `statsb`

Citisenzhip of the person.

Codes available in the documentation (link below).

https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/statsb

### `hovedperson`

Personal id (`pnr`) of the family Protagonist (see `plads` variable).

https://www.dst.dk/da/Statistik/dokumentation/Times/forebyggelsesregistret/plads

### `papnr`

Personal id (`pnr`) of the family Partner (see `plads` variable).

https://www.dst.dk/da/Statistik/dokumentation/Times/forebyggelsesregistret/plads

### `aldaeldst`

Oldest child age in `e_familie` (see `e_familie`)

custom variable?

### `aldyngst`

Oldest child age in `e_familie` (see `e_familie`)

custom variable?

### `antboernf`

Number of children in the family.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/familier/antboernf

### `antpersf`

Number of people in the family

https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/antpersf

### `cvrnr`

CVR number. The CVR number is the unique id of a legal entity.

https://www.dst.dk/da/Statistik/dokumentation/Times/forskningsservice/cvrnr

### `arbnr`

10-digit identification number for a workplace. The value is `0` for self-employed and employed spouses who are not in the business register.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-fra-det-centrale-oplysningsseddelregister/arbnr

### `antboernh`

Number of children in the household.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/husstande/antboernh

### `antpersh`

Number of people in the household.

https://www.dst.dk/da/Statistik/dokumentation/Times/cpr-oplysninger/antperh

### `bopikom_gl`

Previous address in the municipality (road no., house number, house letter, floor, side / door)

https://www.dst.dk/extranet/ForskningVariabellister/NBPT%20-%20N%C3%B8gle%20bop%C3%A6lsadresse%20tilbage%20i%20Tid%20(ny%20til%20gl).html

### `kom_gl`

Previous municipal code from the National Register Address.

https://www.dst.dk/extranet/ForskningVariabellister/NBPT%20-%20N%C3%B8gle%20bop%C3%A6lsadresse%20tilbage%20i%20Tid%20(ny%20til%20gl).html

### `opgikom`

The address in the municipality (road no., House no., House letter). See `BOPIKOM` for further description.

https://www.dst.dk/da/Statistik/dokumentation/Times/forskningsservice/opgikom

### `opgikom_gl`

Previous address in the municipality (road no., House no., House letter). See `BOPIKOM` for further description.

https://www.dst.dk/extranet/ForskningVariabellister/NOGT%20-%20N%C3%B8gle%20opgangsadresse%20tilbage%20i%20tid%20(ny%20til%20gl).html

### `afslutn`

Course end. Specifies the way the course is completed for each student, ie. whether the student has, for example, completed or interrupted the course.

- '0' = Continues beyond the period
- '1' = The course is completed and the test passed
- '2' = The course is completed and the test has not passed
- '3' = The course is completed and the student does not attend the exam
- '4' = The course is complete and there is no test attached to the course
- '5' = The student has interrupted the course or has not attended the exam
- '6' = Self-students
- '7' = Uninformed termination
- '8' = No sample associated with the course

https://www.dst.dk/da/Statistik/dokumentation/Times/Uddannelsesdata/Kursistregistret/AFSLUTN

### `akomfang`

The proportion of a full academic year to which the course corresponds. Decimal fraction of 1 year of 5 digits where the comma is implied. The proposed 0 must not be suppressed. A full-time course is thus indicated by the value `10000`, while a half-time course is indicated by the value `05000`.

https://www.dst.dk/da/Statistik/dokumentation/Times/Uddannelsesdata/Kursistregistret/AKOMFANG

### `cprtjek`

CPR check. Control value calculated on a social security number from a given date.

- '0' = The social security number is valid
- '1' = The social security number does not consist of 10 digits
- '2' = Not used replacement number
- '3' = Not valid date of birth in a replacement number
- '4' = Not valid date of birth in a social security number with control digit
- '5' = Not valid date of birth in a social security number without a control digit
- '6' = Social security number without control digit, but not in valid series
- '7' = Date of birth is after the date the age is calculated from

https://www.dst.dk/da/Statistik/dokumentation/Times/forskningsservice/cprtjek

### `cprtype`

CPR type.

- '1' = Traditional pnumber
- '2' = Replacement pnumber
- '3' = Pnumber without control digit, series 1
- '4' = Pnumber without control digit, series 2
- '5' = Pnumber without control digit, series 3

https://www.dst.dk/da/Statistik/dokumentation/Times/forskningsservice/cprtype

### `kursist_vfra`

Start date of the course.

https://www.dst.dk/da/Statistik/dokumentation/Times/Uddannelsesdata/Kursistregistret/KURSIST-VFRA

### `kursist_vtil`

End date of the course.

https://www.dst.dk/da/Statistik/dokumentation/Times/Uddannelsesdata/Kursistregistret/KURSIST-VTIL

### `udd`

Code for an education understood as the educational program or activity. All educational programs have a UDD code (eg: Nurse = 5166, Engineer = 5189)

https://www.dst.dk/da/statistik/dokumentation/times/uddannelseregister/udd

### `version`

Time reference. The first time data is loaded is `version = 01` for a given REFERENCE TIME, the second time `version = 02`, etc.

https://www.dst.dk/da/statistik/dokumentation/times/moduldata-faelles-variable/version

### `ansaar`

Year of employment at work.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-ansaettelser/ansaar

### `ansdage`

Number of days employed.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-ansaettelser/ansdage

### `ansxfrem`

Change of employment from the previous year to the current year for each employee. The variable thus looks forward in time to November the following year.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-ansaettelser/ansxfrem

### `ansxtilb`

Change in employment at the current workplace compared to the previous year for the individual employee. The variable thus looks back in time to November the year before.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-ansaettelser/ansxtilb

### `arbled`

Unemployment rate in working years (excluding holidays). Total unemployed weeks in a year divided by the total number of working weeks in a year.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ledighed---beskaeftigelsesoplysninger-der-vedroerer-ida-ansaettelser-/arbled

### `jobkat`

Type of job.

- '1' = Full time (30 hours or more per week)
- '2' = Part time (15-29 hours)
- '3' = Bijob (under 15 hours)
- '5' = Full time (Over 8 weeks with partial unemployment during the year)
- '6' = Part-time (Over 8 weeks of partial unemployment during the year)
- '7' = Bijob (Over 8 weeks with partial unemployment during the year)
- '9' = Undisclosed

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-ansaettelser/jobkat

### `joblon`

Salary. Wages in the individual employment relationship for both main and secondary employees.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/loenforhold-der-vedroerer-ida-ansaettelser-/joblon

### `lonmfrem`

Whether an employee is an employee the following year or not.

- '0' = Not employed the following year
- '1' = Employee the following year

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-ansaettelser/lonmfrem

### `lonmtilb`

Whether an employee is an employee the year before or not.

- '0' = Not employed the year before
- '1' = Employee the year before

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-ansaettelser/lonmtilb

### `persbrc`

Personal industry code received from the Register-based Workforce Statistics (RAS). The variable is defined for principal employees, employers, self-employed and assisting spouses.

- '1XXXXX' = Agriculture, fisheries and raw material extraction
- '2XXXXX' = Manufacturing
- '3XXXXX' = Energy and water supply
- '4XXXXX' = Construction
- '5XXXXX' = Trade, hotel and restaurant business. etc.
- '6XXXXX' = Transport, Post and Telecommunications
- '8XXXXX' = Public and personal services

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-ansaettelser/persbrc

### `still`

Socio-economic variable code that indicates the type of employee at the end of November.

- '31' = Director / Top Managers
- '32' = Senior official / Employee at the highest level
- '33' = Leading functionary
- '34' = Functional in general / Medium-level employees
- '35' = Skilled worker / Basic level employees
- '36' = Non-skilled worker / Other employees
- '37' = Employed employees without further details

There are more codes but the documentation do not say what they mean (e.g. 11).

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-ansaettelser/still

### `tilknyt`

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

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-ansaettelser/tilknyt

### `timelon`

Hourly salary.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/loenforhold-der-vedroerer-ida-ansaettelser-/timelon

### `tlonkval`

Quality of `timelon` variable. It captures the relative uncertainty of the quality of the data from `timelon` from 0 (no hours) to +100 (useless hourly salary).

- '0' = Number of hours employed equals 0
- '1-49' = Useful quality
- '50-99' = Doubtful quality
- '100' = Pension (ATP - Arbejdsmarkedets Tillægspension)
- '>100' = Useless quality

The relevant populations for TLONKVAL can be defined using the variable `type`

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/loenforhold-der-vedroerer-ida-ansaettelser-/tlonkval

### `type`

Type of employment.

- 'A' = Employer
- 'B' = November bi job (bi-employment)
- 'E' = Not November job
- 'H' = November primary job (mainly employed)
- 'M' = Assisting spouse
- 'N' = November job
- 'S' = Self employed
- '3' = Most important not November jobs

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-ansaettelser/type

### `ielandf`

Father's country of origin.

custom variable?

-`ielandm`

Mother's country of origin.

custom variable?

### `ietypef`

Father inmigration type (see `ie_type`)

custom variable?

### `ietypem`

Mother inmigration type (see `ie_type`)

custom variable?

### `antalarb`

Number of workplaces in the company.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-firmaer/antalarb

### `antarbb`

Previous number of retained workplaces in the company between the current year and the year before.

https://www.dst.dk/da/Statistik/dokumentation/Times/IDA-databasen/IDA-firmaer/ANTARBB

### `fansb`

Total number of employees in the company.

https://www.dst.dk/da/Statistik/dokumentation/Times/IDA-databasen/IDA-firmaer/FANSB

### `fansh`

Number of _main_ employees in the company. Number of employees with main occupation in the company.

https://www.dst.dk/da/Statistik/dokumentation/Times/IDA-databasen/IDA-firmaer/FANSH

### `sarbgnrx`

1 if company largest workplace in company changed headcount, 0 otherwise.

- '0' = Unchanged employer number
- '1' = Changed employer number

https://www.dst.dk/da/Statistik/dokumentation/Times/IDA-databasen/IDA-firmaer/SARBGNRX

### `sidtilb`

Identity of largest workplace in the company between the current year and the year before. Categorical varaible that tracks the movement of workers from the largest workplace (e.g. HQ).

- 'B1' = Preserved, identical
- 'B2' = Preserved, not identical
- 'O1' = newly created
- 'O2' = Created via separation from a workplace (min. 30% of employees and min. 2 people (v. Address change))
- 'O3' = Created via "takeover" of premises / buildings from a closed workplace in the same industry
- 'O4' = Created through transition from self-employed without employees per November (in the same industry)
- 'O5' = Created via transition from workplace without employees per November (in the same industry)
- 'SM' = Unchanged, with no employees per November also in the year before (preserved).
- 'T1' = New access (no connection to a workplace the year before)
- 'T2' = Access from work with November employees in the previous year (in the same industry)
- 'T3' = Access of a "fictional" entity in connection with a formal change of ownership

### `slbnr`

Serial number for largest workplace in company.

https://www.dst.dk/da/Statistik/dokumentation/Times/IDA-databasen/IDA-firmaer/SLBNR

### `stordbxx`

6-digit industry code for largest workplace in the company. The varaible name change depending of the year of the Danish Industry Code they are using for the encoding (93', 03', 07').

- From idfi1980 to idfi2002, the variable/column is called `STORDB93`
- From idfi2003 to idfi2006, the variable/column is called `STORDB03`
- From idfi2007 onwards, the variable/column is called `STORDB07`

Check the documentation for the specific categorical encodings:

https://www.dst.dk/da/Statistik/dokumentation/Times/IDA-databasen/IDA-firmaer/STORDB03

### `uoplansb`

Secondary employees in company with undisclosed workplace.

The variable must be seen in the context of the variable `FANSB` (Number of employees in the company). In this, the number of secondary employees in each company is calculated on the basis of the workplace data set (IDAS) for the given year. This includes only valid workplaces, ie. fictitious and undisclosed workplaces are not included. However, there are also secondary employees who are associated with an undisclosed workplace and who therefore do not appear in that dataset.

https://www.dst.dk/da/Statistik/dokumentation/Times/IDA-databasen/IDA-firmaer/UOPLANSB

### `almaudd`

Code for highest completed _general_ education.

Check the documentation for the specific categorical encodings:

https://www.dst.dk/da/Statistik/dokumentation/Times/Uddannelsesdata/Hoejest-fuldfoerte-uddannelse---status/ALMAUDD

### `alm_vfra`

Time of highest completed general education.

https://www.dst.dk/da/Statistik/dokumentation/Times/Uddannelsesdata/Hoejest-fuldfoerte-uddannelse---status/ALM-VFRA

### `erhaudd`

Highest completed _vocational_ qualifying education.

Check the documentation for the specific categorical encodings:

https://www.dst.dk/da/Statistik/dokumentation/Times/Uddannelsesdata/Hoejest-fuldfoerte-uddannelse---status/ERHAUDD

### `erhinstnr`

Institutional number of the institution where the highest completed vocational qualifying education has been completed.

Check the documentation for the specific categorical encodings:

https://www.dst.dk/da/Statistik/dokumentation/Times/Uddannelsesdata/Hoejest-fuldfoerte-uddannelse---status/ERHINSTNR

### `erh_vfra`

Time of obtaining vocational competency-providing education

https://www.dst.dk/da/Statistik/dokumentation/Times/Uddannelsesdata/Hoejest-fuldfoerte-uddannelse---status/ERH-VFRA

### `hfaudd`

Code for a person's highest completed education at any given time.

Check the documentation for the specific categorical encodings:

https://www.dst.dk/da/Statistik/dokumentation/Times/Uddannelsesdata/Hoejest-fuldfoerte-uddannelse---status/HFAUDD

### `hfinstnr`

Code for the name of the institution where the highest completed education is completed.

Check the documentation for the specific categorical encodings:

https://www.dst.dk/da/Statistik/dokumentation/Times/Uddannelsesdata/Hoejest-fuldfoerte-uddannelse---status/HFAUDD

### `hf_vfra`

Time of highest completed education.

https://www.dst.dk/da/Statistik/dokumentation/Times/Uddannelsesdata/Hoejest-fuldfoerte-uddannelse---status/HF-VFRA

### `ig_vfra`

Starting time of ongoing education.

https://www.dst.dk/da/Statistik/dokumentation/Times/Uddannelsesdata/Hoejest-fuldfoerte-uddannelse---status/IG-VFRA

### `forklar`

Code for residence permit type from the Immigration Service.

Check the documentation for the specific categorical encodings:

https://www.dst.dk/da/Statistik/dokumentation/Times/Uddannelsesdata/Hoejest-fuldfoerte-uddannelse---status/HFAUDD

### `grundlag`

Code of the subdivision of residence permit type from the Immigration Service.

Check the documentation for the specific categorical encodings:

https://www.dst.dk/da/Statistik/dokumentation/Times/Uddannelsesdata/Hoejest-fuldfoerte-uddannelse---status/grundlag

### `imputeret`

Code for imputation status of the person's residence permit. After a process, residence permit are `imputed` (e.g 1, 20, 99) for immigrant persons who do not have Danish / Nordic citizenship and who are born abroad.

- '0' From 1997, Immigration Service
- '1' From 1997, Imputed
- '9' From 1997, Nordic citizen, should not be imputed
- '11' Before 1997, Immigration Service 1993-1996
- '12' Before 1997, Survey Response
- '20' Before 1997, Imputed
- '29' Before 1997, a Nordic citizen, should not be imputed
- '99' Imputed in connection with inventory sheet (statusopgørelse)

https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/imputeret

### `referenceid`

Date [TO BE DOCUMENTED]

Custom variable?

### `kategori`

Code for residence permit type from the Immigration Service.

- '1' = Asylum, etc.
- '2' = The other area of residence
- '3' = Business
- '4' = EU / EEA
- '5' = family reunification
- '51' = Brexit
- '52' = Ukraine special law
- '53' = Other basis
- '54' = refugee Status
- '55' = Study etc.
- '6' = Study
- '9997' = Nordic citizen
- '9999' = Immigrated before 1997

https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/kategori

### `tilladelsesdato`

Date of residence permit.

https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/tilladelsesdato

### `akasaf`

Last year as a member of A-kassa.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ledighed-og-beskaeftigelsesoplysninger-der-vedroerer-ida-personer/akasaf

### `akasst`

Most recent start year as a member of the A-kassa.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ledighed-og-beskaeftigelsesoplysninger-der-vedroerer-ida-personer/akasst

### `aldernov`

Age calculated at the end of November (reference period).

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-personer/aldernov

### `arledgr`

Unemployment rate.

The unemployment rate is calculated as the number of hours available in relation to the number of (possible) working hours for a given year.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ledighed-og-beskaeftigelsesoplysninger-der-vedroerer-ida-personer/arledgr

### `atpar`

Number of years as an employee.

A person who has been abroad and has therefore not been included in the population for one or more years will have his ATPAR reset.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-personer/atpar

### `ejnov`

Number of supplementary non-November employment appointments.

Employment with the largest ATP contribution is defined as being the most important non-November employment. Thus, when the most important non-November employment is selected, any additional non-November employment per year is counted.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-personer/ejnov

### `ejnovsum`

The variable sums up wages in supplementary non-November-related employment in addition to the most important employment.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/loenoplysninger-der-vedroerer-ida-personer/ejnovsum

### `erhver`

Work experience (1000 "points" per fulltime employed year).

The maximum work experience for part-time insured persons can be assumed 750 per person. per year and for the rest 1,000 per year.

For people who have been abroad and therefore have not been included in the population for one or more years, `erhver` will be reset.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-personer/erhver

### `erhver79`

Work experience from 1964 to the end of 1979 calculated on the basis of ATP contributions. It counts the number of years as an employee before 1980 for people born in 1921 - 1971.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-personer/erhver79

### `lonind`

Salary based on SKAT employee reporting.

All employers issue an information sheet to SKAT and their employees annually (during January). The information sheet is an overview of paid salary and contributions. nr. 13 specifies the net salary for each employment to which the information form relates.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/loenoplysninger-der-vedroerer-ida-personer/lonind

### `nsup`

Number of supplementary November-employment in addition to main and secondary employment per year.

The employment that relates to November but not to the main or secondary employment is counted for the individual. The supplementary employment is only included if the amount is above the salary limit.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-personer/nsup

### `pstill`

[TO BE DONE]

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-personer/pstill

### `sstill`

[TO BE DONE]

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-personer/sstill

### `senafar`

Latest completion of the labor market.

Most recent termination of the labor market as employed or unemployed for 2 consecutive years.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-personer/senafar

### `senstar`

Latest start in the labor market.

Latest start in the labor market as employed or unemployed is formed from the primary job positio for 2 consecutive years.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-personer/senstar

### `startar`

Year for the first time in the labor market.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-personer/startar

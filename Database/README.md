# SI DST Data Catalog

## Database Catalogue

[TO BE DONE]

## Variable Catalogue

### Tools

- Variable Searching tool: https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable
- Registry list: https://www.dst.dk/extranet/forskningvariabellister/Oversigt%20over%20registre.html


### `PNR` / DB: [`bef`, `poppers`,`fida`,`idan` ,`frpe`, `idan` ,`idap`, `iepe`, `ivpe`, `ind`, `indh`]

Unique identification of person is used as key to `PERSON_ID`.

People's anonimized CPR. All CPR PNRs are converted to a unidentified PERSON_ID.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/folketal/pnr

### `ALDER` / DB: [`bef`, `poppers`, `iepe`]

Age.

https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/alder

### `FAMILIE_ID` / DB: [`bef`, `poppers_famid`]

Basic legal family unit. All individuals have a FAMILIE_ID.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/familier/familie-id

### `C_FAMILIE_ID` / DB: [`fam`, `poppers_cfamid`]

Focuses on the family links. C_FAMILIE_ID is only for coupled families, in which C_FAMILIE_ID = PERSON_ID for the mother.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/familier/c-familie-id

### `MOR_ID` / DB: [`bef`, `iepe`]

`PERSON_ID` of the person's mother.

https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/mor-id

### `FAR_ID` / DB: [`bef`, `iepe`]

`PERSON_ID` of the person's father.

https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/far-id

### `EFALLE` / DB: [`bef`]

EFALLE_ID is the social security number of the person with whom a given person lives and forms a couple in the form of marriage, registered partnership, cohabiting couples or cohabiting couples.

https://www.dst.dk/da/Statistik/dokumentation/Times/forskningsservice/efalle

### `AEGTE_ID` / DB: [`bef`]

Specifies the social security number ID of spouse or registered partner. There is the following connection between the person's marital status and information about the spouse:

- Married = spouse number
- Divorced = social security number of former spouse
- Widow / widower = social security number of deceased spouse
- Partnership = partner number
- Oph. partnership = social security number of former partner
- Long-term Partner = social security number of deceased partner
- Death = spouse / partner social security number

https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/aegte-id

### `BOPIKOM` / DB: [`bef`, `hust`, `fam`]

The address in the municipality (road no., house number, house letter, floor, side / door)

https://www.dst.dk/da/Statistik/dokumentation/Times/forskningsservice/bopikom

### `KOM` / DB: [`bef`, `hust`, `fam`, `iepe`, `nbpt`, `nogt`]

Municipal code from the National Register Address.

https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/kom

### `BOP_VFRA` / DB: [`bef`]

Date of immigration.

https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/bop-vfra

### `VAN_VTIL` / DB: [`bef`]

Date when immigration applies from.

A person who immigrates several times during a period is included the corresponding number of times and appears with several immigration dates.

https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/van-vtil

### `CIVST` / DB: [`bef`, `iepe`]

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

### `CIV_FRA` / DB: [`bef`]

Date of the most recently recorded change of marital status (married, divorced, dead) of the person. Back to 2004, if `CVIST` (marital status) is equal to U (unmarried), `CIV_FRA` is set equal to the date of birth.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/folketal/civ-vfra

### `FAMILIE_TYPE` / DB: [`bef`, `fam`]

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

### `FM_MARK` / DB: [`bef`]

Person cohabitation type.

- '1' = Lives with both parents
- '2' = For children: Lives with mother who is in new couple. For adults: Living with mom.
- '3' = For children: Living with single mother. For adultsThe value does not exist.
- '4' = For children: Lives with dad who is in new couple. For adults: Living with dad.
- '5' = For children: Living with single father. For adults: The value does not exist.
- '6' = Do not live with parents

https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/fm-mark

### `FOEDREG_KODE` / DB: [`bef`, `iepe`]

Place of birth.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/folketal/foedreg-kode

### `FOED_DAG` / DB: [`bef`]

Birthday.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/folketal/foed-dag

### `IE_TYPE` / DB: [`bef`, `iepe`]

Definitions of immigrants, descendants, and people of Danish origin, which collectively comprise entire populations, are as follows:

- '1' = Danish. People, regardless of birthplace, who have at least one parent who is both a Danish citizen and born in Denmark.
- '2' = Immigrant. People born abroad. None of the parents are both Danish citizens and born in Denmark.
- '3' = Descendant. People born in Denmark. None of the parents are both Danish citizens and born in Denmark.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/udlaendinge/ie-type

### `GENERATION` / DB: [`bef`, `iepe`]

Whether the father and/or mother were born in Denmark or abroad.

- '0' = Danish (`IE_TYPE` = 1)
- '1' = Parents both born abroad
- '2' = Parents both born in Denmark
- '3' = One parent born in Denmark and another abroad.
- '4' = Parental information not available.

https://www.dst.dk/da/Statistik/dokumentation/Times/cpr-oplysninger/generation

### `HUSTYPE` / DB: [`bef`, `hust`]

Household composition.

- '1' = A single man
- '2' = A single woman
- '3' = A married couple
- '4' = A few more
- '5' = A non-resident child under 18 years
- '6' = Household of several families

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/husstande/hustype

### `KOEN` / DB: [`bef`, `frpe`, `idap`, `iepe`]

Gender (CPR based).

- '1' = Male
- '2' = Female
- '9' = Unknown / Company

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/folketal/koen

### `OPR_LAND` / DB: [`bef`, `iepe`]

Citizenship / Country of origin of the person.

Encoding: https://www.dst.dk/da/Statistik/dokumentation/nomenklaturer/lande-psd?

https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/opr-land

### `PLADS` / DB: [`bef`]

A person's "place" within the couple.

- '1' = Protagonist (woman)
- '2' = Partner (man)
- '3' = Resident child

In a couple, 1 is the woman (or oldest if not man/women couple), 2 the man (or youngest if not man/women couple), 3 is a person under the age of 25 who lives at the same address as at least one of his parents who has never been married or registered partner (marital status = unmarried) and who is not a father or mother of anyone who lives or has lived in Denmark.

https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/plads

### `REG` / DB: [`bef`]

Region of Denmark.

- '0' = Undisclosed
- '81' = North Jutland
- '82' = Central Jutland
- '83' = Southern Denmark
- '84' = Capital Region
- '85' = Zealand

https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/reg

### `STATSB` / DB: [`bef`, `iepe`]

Citizenship / Country of origin of the person.

Codes available in the documentation (link below).

https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/statsb

### `STATFODF` / DB: [`iepe`]

Continent of origin of the father.

Codes available in the documentation (link below).

https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/statsb

### `STATFODM` / DB: [`iepe`]

Continent of origin of the mother.

Codes available in the documentation (link below).

https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/statsb

### `STATFOED` / DB: [`iepe`]

Continent of origin of the person.

Codes available in the documentation (link below).

https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/statsb

### `HOVEDPERSON` / DB: [`fam`]

Personal id (`pnr`) of the family Protagonist (see `PLADS` variable).

https://www.dst.dk/da/Statistik/dokumentation/Times/forebyggelsesregistret/plads

### `PAPNR` / DB: [`fam`]

Personal id (`PNR`) of the family Partner (see `PLADS` variable).

https://www.dst.dk/da/Statistik/dokumentation/Times/forebyggelsesregistret/plads

### `ALDAELDST` / DB: [`fam`]

Oldest child age in `E_FAMILIE` (see `E_FAMILIE`)

No documentation available.

### `ALDYNGST` / DB: [`fam`]

Youngest child age in `E_FAMILIE` (see `E_FAMILIE`)

No documentation available.

### `ANTBOERNF` / DB: [`fam`]

Number of children in the family.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/familier/antboernf

### `ANTPERSF` / DB: [`fam`]

Number of people in the family

https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/antpersf

### `CVRNR` / DB: [`firm`, `fida`, `frpe`, `ivnv`, `ivpe`]

Central Business Register (CVR) number. The CVR number is the unique id of a legal entity.

https://www.dst.dk/da/Statistik/dokumentation/Times/forskningsservice/cvrnr

### `ARBNR` / DB: [`fida`]

10-digit identification number for a workplace. The value is `0` for self-employed and employed spouses who are not in the business register.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-fra-det-centrale-oplysningsseddelregister/arbnr

### `LBNR` / DB: [`fida`, `idan`, `idas`]

Unique serial number per workplace that is constant over time for preserved (not definitively closed) workplaces.

https://www.dst.dk/da/Statistik/dokumentation/Times/ida-databasen/ida-ansaettelser/lbnr

### `ANTBOERNH` / DB: [`hust`]

Number of children in the household.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/husstande/antboernh

### `ANTPERSH` / DB: [`hust`]

Number of people in the household.

https://www.dst.dk/da/Statistik/dokumentation/Times/cpr-oplysninger/antperh

### `BOPIKOM_GL` / DB: [`nbpt`]

Previous address in the municipality (road no., house number, house letter, floor, side / door)

https://www.dst.dk/extranet/ForskningVariabellister/NBPT%20-%20N%C3%B8gle%20bop%C3%A6lsadresse%20tilbage%20i%20Tid%20(ny%20til%20gl).html

### `KOM_GL` / DB: [`nbpt`, `nogt`]

Previous municipal code from the National Register Address.

https://www.dst.dk/extranet/ForskningVariabellister/NBPT%20-%20N%C3%B8gle%20bop%C3%A6lsadresse%20tilbage%20i%20Tid%20(ny%20til%20gl).html

### `OPGIKOM` / DB: [`nogt`]

Opgang housing project. The address in the municipality (road no., House no., House letter). See `BOPIKOM` for further description.

https://www.dst.dk/da/Statistik/dokumentation/Times/forskningsservice/opgikom

### `OPGIKOM_GL` / DB: [`nogt`]

Opgang housing project. Previous address in the municipality (road no., House no., House letter). See `BOPIKOM` for further description.

https://www.dst.dk/extranet/ForskningVariabellister/NOGT%20-%20N%C3%B8gle%20opgangsadresse%20tilbage%20i%20tid%20(ny%20til%20gl).html

### `AFSLUTN`

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

### `AKOMFANG`

The proportion of a full academic year to which the course corresponds. Decimal fraction of 1 year of 5 digits where the comma is implied. The proposed 0 must not be suppressed. A full-time course is thus indicated by the value `10000`, while a half-time course is indicated by the value `05000`.

https://www.dst.dk/da/Statistik/dokumentation/Times/Uddannelsesdata/Kursistregistret/AKOMFANG

### `CPRTJEK`

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

### `CPRTYPE`

CPR type.

- '1' = Traditional pnumber
- '2' = Replacement pnumber
- '3' = Pnumber without control digit, series 1
- '4' = Pnumber without control digit, series 2
- '5' = Pnumber without control digit, series 3

https://www.dst.dk/da/Statistik/dokumentation/Times/forskningsservice/cprtype

### `KURSIST_VFRA`

Start date of the course.

https://www.dst.dk/da/Statistik/dokumentation/Times/Uddannelsesdata/Kursistregistret/KURSIST-VFRA

### `KURSIST_VTIL`

End date of the course.

https://www.dst.dk/da/Statistik/dokumentation/Times/Uddannelsesdata/Kursistregistret/KURSIST-VTIL

### `UDD`

Code for an education understood as the educational program or activity. All educational programs have a UDD code (eg: Nurse = 5166, Engineer = 5189)

https://www.dst.dk/da/statistik/dokumentation/times/uddannelseregister/udd

### `VERSION` / DB: [`firm`, `frpe`]

Time reference. The first time data is loaded is `VERSION = 01` for a given REFERENCE TIME, the second time `VERSION = 02`, etc.

https://www.dst.dk/da/statistik/dokumentation/times/moduldata-faelles-variable/version

### `ARBGNR` / DB: [`idan`, `idas`, `idfi`]

Workplace 12-digits Unique Code.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/arbgnr

### `ANSAAR` / DB: [`idan`]

Year of employment at workplace.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-ansaettelser/ansaar

### `ANSDAGE` / DB: [`idan`]

Number of days employed.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-ansaettelser/ansdage

### `ANSXFREM` / DB: [`idan`]

Change of employment from the previous year to the current year for each employee. The variable thus looks forward in time to November the following year.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-ansaettelser/ansxfrem

### `ANSXTILB` / DB: [`idan`]

Change in employment at the current workplace compared to the previous year for the individual employee. The variable thus looks back in time to November the year before.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-ansaettelser/ansxtilb

### `ARBLED` / DB: [`idan`]

Unemployment rate in that working year (excluding holidays). Total unemployed weeks in a year divided by the total number of working weeks in a year.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ledighed---beskaeftigelsesoplysninger-der-vedroerer-ida-ansaettelser-/arbled

### `ARBSTK` / DB: [`idan`]

Workplace 4-digits Code.

The code itself is not unique. Only in combination with the employer number (see `ARBGNR` under workplaces) can the individual workplace be identified. The identification is only valid for the current year and has no lasting impact on the separation of individual workplaces. For this purpose, workplace number is used (`ARDNR`)

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/arbstk

### `JOBKAT` / DB: [`idan`]

Type of job.

- '1' = Full time (30 hours or more per week)
- '2' = Part time (15-29 hours)
- '3' = Bijob (under 15 hours)
- '5' = Full time (Over 8 weeks with partial unemployment during the year)
- '6' = Part-time (Over 8 weeks of partial unemployment during the year)
- '7' = Bijob (Over 8 weeks with partial unemployment during the year)
- '9' = Undisclosed

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-ansaettelser/jobkat

### `JOBLON` / DB: [`idan`]

Salary linked to particular employment. Wages in the individual employment relationship for both main and secondary employees.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/loenforhold-der-vedroerer-ida-ansaettelser-/joblon

### `LONMFREM` / DB: [`idan`]

Whether an employee is an employee the following year or not.

- '0' = Not employed the following year
- '1' = Employee the following year

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-ansaettelser/lonmfrem

### `LONMTILB` / DB: [`idan`]

Whether an employee is an employee the year before or not.

- '0' = Not employed the year before
- '1' = Employee the year before

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-ansaettelser/lonmtilb

### `PERSBRC` / DB: [`idan`]

Personal industry code received from the Register-based Workforce Statistics (RAS). The variable is defined for principal employees, employers, self-employed and assisting spouses.

- '1XXXXX' = Agriculture, fisheries and raw material extraction
- '2XXXXX' = Manufacturing
- '3XXXXX' = Energy and water supply
- '4XXXXX' = Construction
- '5XXXXX' = Trade, hotel and restaurant business. etc.
- '6XXXXX' = Transport, Post and Telecommunications
- '8XXXXX' = Public and personal services

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-ansaettelser/persbrc

### `STILL` / DB: [`idan`]

Socio-economic Job Position variable code that indicates the type of employee at the end of November (November main Job).

- '31' = Director / Top Managers
- '32' = Senior official / Employee at the highest level
- '33' = Leading functionary
- '34' = Functional in general / Medium-level employees
- '35' = Skilled worker / Basic level employees
- '36' = Non-skilled worker / Other employees
- '37' = Employed employees without further details

There are more codes in the data but the documentation do not say what they mean (e.g. 11).

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-ansaettelser/still

### `TILKNYT` / DB: [`idan`]

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

### `TIMELON` / DB: [`idan`]

Hourly salary.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/loenforhold-der-vedroerer-ida-ansaettelser-/timelon

### `TLONKVAL` / DB: [`idan`]

Quality of `TIMELON` variable. It captures the relative uncertainty of the quality of the data from `TIMELON` from 0 (no hours) to +100 (useless hourly salary).

- '0' = Number of hours employed equals 0
- '1-49' = Useful quality
- '50-99' = Doubtful quality
- '100' = Pension (ATP - Arbejdsmarkedets Tillægspension)
- '>100' = Useless quality

The relevant populations for TLONKVAL can be defined using the variable `TYPE`

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/loenforhold-der-vedroerer-ida-ansaettelser-/tlonkval

### `TYPE` / DB: [`idan`]

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

### `IELANDF`

Citizenship / Country of origin of the father.

[NO DOCUMENTATION AVAILABLE]

-`IELANDM`

Citizenship / Country of origin of the mother.

[NO DOCUMENTATION AVAILABLE]

### `IETYPEF`

Father inmigration type (see `IE_TYPE`)

[NO DOCUMENTATION AVAILABLE]

### `IETYPEM`

Mother inmigration type (see `IE_TYPE`)

[NO DOCUMENTATION AVAILABLE]

### `ANTALARB` / DB: [`idfi`]

Number of workplaces in the company.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-firmaer/antalarb

### `ANTARBB` / DB: [`idfi`]

Previous number of retained workplaces in the company between the current year and the year before.

https://www.dst.dk/da/Statistik/dokumentation/Times/IDA-databasen/IDA-firmaer/ANTARBB

### `FANSB` / DB: [`idfi`]

Total number of employees in the company.

https://www.dst.dk/da/Statistik/dokumentation/Times/IDA-databasen/IDA-firmaer/FANSB

### `FANSH` / DB: [`idfi`]

Number of _main_ employees in the company. Number of employees with main occupation in the company.

https://www.dst.dk/da/Statistik/dokumentation/Times/IDA-databasen/IDA-firmaer/FANSH

### `SARBGNRX` / DB: [`idfi`]

1 if company largest workplace in company changed headcount, 0 otherwise.

- '0' = Unchanged employer number
- '1' = Changed employer number

https://www.dst.dk/da/Statistik/dokumentation/Times/IDA-databasen/IDA-firmaer/SARBGNRX

### `SIDTILB` / DB: [`idfi`]

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

### `SLBNR` / DB: [`idfi`]

Serial number for largest workplace in company.

https://www.dst.dk/da/Statistik/dokumentation/Times/IDA-databasen/IDA-firmaer/SLBNR

### `STORDBXX` / DB: [`idfi`]

6-digit industry code for largest workplace in the company. The varaible name change depending of the year of the Danish Industry Code they are using for the encoding (93', 03', 07').

- From idfi1993 to idfi2002, the variable/column is called `STORDB93`
- From idfi2003 to idfi2006, the variable/column is called `STORDB03`
- From idfi2007 onwards, the variable/column is called `STORDB07`

Check the documentation for the specific categorical encodings:

https://www.dst.dk/da/Statistik/dokumentation/Times/IDA-databasen/IDA-firmaer/STORDB03

### `UOPLANSB` / DB: [`idfi`]

Secondary employees in company with undisclosed workplace.

The variable must be seen in the context of the variable `FANSB` (Number of employees in the company). In this, the number of secondary employees in each company is calculated on the basis of the workplace data set (IDAS) for the given year. This includes only valid workplaces, ie. fictitious and undisclosed workplaces are not included. However, there are also secondary employees who are associated with an undisclosed workplace and who therefore do not appear in that dataset.

https://www.dst.dk/da/Statistik/dokumentation/Times/IDA-databasen/IDA-firmaer/UOPLANSB

### `ALMAUDD`

Code for highest completed _general_ education.

Check the documentation for the specific categorical encodings:

https://www.dst.dk/da/Statistik/dokumentation/Times/Uddannelsesdata/Hoejest-fuldfoerte-uddannelse---status/ALMAUDD

### `ALM_VFRA`

Time of highest completed general education.

https://www.dst.dk/da/Statistik/dokumentation/Times/Uddannelsesdata/Hoejest-fuldfoerte-uddannelse---status/ALM-VFRA

### `ERHAUDD`

Highest completed _vocational_ qualifying education.

Check the documentation for the specific categorical encodings:

https://www.dst.dk/da/Statistik/dokumentation/Times/Uddannelsesdata/Hoejest-fuldfoerte-uddannelse---status/ERHAUDD

### `ERHINSTNR`

Institutional number of the institution where the highest completed vocational qualifying education has been completed.

Check the documentation for the specific categorical encodings:

https://www.dst.dk/da/Statistik/dokumentation/Times/Uddannelsesdata/Hoejest-fuldfoerte-uddannelse---status/ERHINSTNR

### `ERH_VFRA`

Time of obtaining vocational competency-providing education

https://www.dst.dk/da/Statistik/dokumentation/Times/Uddannelsesdata/Hoejest-fuldfoerte-uddannelse---status/ERH-VFRA

### `HFAUDD`

Code for a person's highest completed education at any given time.

Check the documentation for the specific categorical encodings:

https://www.dst.dk/da/Statistik/dokumentation/Times/Uddannelsesdata/Hoejest-fuldfoerte-uddannelse---status/HFAUDD

### `HFINSTNR`

Code for the name of the institution where the highest completed education is completed.

Check the documentation for the specific categorical encodings:

https://www.dst.dk/da/Statistik/dokumentation/Times/Uddannelsesdata/Hoejest-fuldfoerte-uddannelse---status/HFAUDD

### `HF_VFRA`

Time of highest completed education.

https://www.dst.dk/da/Statistik/dokumentation/Times/Uddannelsesdata/Hoejest-fuldfoerte-uddannelse---status/HF-VFRA

### `IG_VFRA`

Starting time of ongoing education.

https://www.dst.dk/da/Statistik/dokumentation/Times/Uddannelsesdata/Hoejest-fuldfoerte-uddannelse---status/IG-VFRA

### `FORKLAR`

Code for residence permit type from the Immigration Service.

Check the documentation for the specific categorical encodings:

https://www.dst.dk/da/Statistik/dokumentation/Times/Uddannelsesdata/Hoejest-fuldfoerte-uddannelse---status/HFAUDD

### `GRUNDLAG`

Code of the subdivision of residence permit type from the Immigration Service.

Check the documentation for the specific categorical encodings:

https://www.dst.dk/da/Statistik/dokumentation/Times/Uddannelsesdata/Hoejest-fuldfoerte-uddannelse---status/grundlag

### `IMPUTERET`

Code for imputation status of the person's residence permit. After a process, residence permit are `IMPUTED` (e.g 1, 20, 99) for immigrant persons who do not have Danish / Nordic citizenship and who are born abroad.

- '0' From 1997, Immigration Service
- '1' From 1997, Imputed
- '9' From 1997, Nordic citizen, should not be imputed
- '11' Before 1997, Immigration Service 1993-1996
- '12' Before 1997, Survey Response
- '20' Before 1997, Imputed
- '29' Before 1997, a Nordic citizen, should not be imputed
- '99' Imputed in connection with inventory sheet (statusopgørelse)

https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/imputeret

### `REFERENCEID`

Date

[TO BE DONE]

[NO DOCUMENTATION AVAILABLE]

### `KATEGORI`

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

### `TILLADELSESDATO`

Date of residence permit.

https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/tilladelsesdato

### `AKASAF` / DB: [`idap`]

Most Recent year as a member of an Unemployment fund (A-kassa).

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ledighed-og-beskaeftigelsesoplysninger-der-vedroerer-ida-personer/akasaf

### `AKASST` / DB: [`idap`]

Most recent start year as a member of A-kassa.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ledighed-og-beskaeftigelsesoplysninger-der-vedroerer-ida-personer/akasst

### `ALDERNOV` / DB: [`idap`]

Age calculated at the end of November (reference period).

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-personer/aldernov

### `ARLEDGR` / DB: [`idap`]

Unemployment rate.

The unemployment rate is calculated as the number of hours available in relation to the number of (possible) working hours for a given year.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ledighed-og-beskaeftigelsesoplysninger-der-vedroerer-ida-personer/arledgr

### `ATPAR` / DB: [`idap`]

Number of years as an employee.

A person who has been abroad and has therefore not been included in the population for one or more years will have his ATPAR reset.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-personer/atpar

### `EJNOV` / DB: [`idap`]

Number of supplementary Non-November employment appointments.

Employment with the largest ATP contribution is defined as being the most important non-November employment. Thus, when the most important non-November employment is selected, any additional non-November employment per year is counted.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-personer/ejnov

### `EJNOVSUM` / DB: [`idap`]

Non-November Employment Salary Sum.

The variable sums up wages in supplementary and main employment for non-November jobs.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/loenoplysninger-der-vedroerer-ida-personer/ejnovsum

### `ERHVER` / DB: [`idap`]

Work experience measured in points (1000 "points" per fulltime employed year).

The maximum work experience for part-time insured persons can be assumed 750 per person. per year and for the rest 1,000 per year.

For people who have been abroad and therefore have not been included in the population for one or more years, `ERHVER` will be reset.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-personer/erhver

### `ERHVER79` / DB: [`idap`]

Work experience from 1964 to the end of 1979 calculated on the basis of ATP contributions. It counts the number of employeed years for people born in 1921 - 1971 until 1980.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-personer/erhver79

### `LONIND` / DB: [`idap`]

Total summed salary linked to the person.

All employers issue an information sheet to SKAT and their employees annually (during January). The information sheet is an overview of paid salary and contributions. nr. 13 specifies the net salary for each employment to which the information form relates.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/loenoplysninger-der-vedroerer-ida-personer/lonind

### `NSUP` / DB: [`idap`]

Number of supplementary November-employments in addition to main and secondary employment per year.

The employment that relates to November but not to the main or secondary employment is counted for the individual. The supplementary employment is only included if the amount is above the salary limit.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-personer/nsup

### `NSUPSUM` / DB: [`idap`]

Summed salary for Supplementary November Employments.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/loenoplysninger-der-vedroerer-ida-personer/nsupsum

### `PSTILL` / DB: [`idap`]

Primary Job Position Code.

[TO BE DONE]

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-personer/pstill

### `SSTILL` / DB: [`idap`]

Secondary Job Position Code.

[TO BE DONE]

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-personer/sstill

### `SENAFAR` / DB: [`idap`]

Latest exit of the labor market.

Most recent termination of the labor market as employed or unemployed for 2 consecutive years.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-personer/senafar

### `SENSTAR` / DB: [`idap`]

Latest start in the labor market.

Latest start in the labor market as employed or unemployed is formed from the primary job positio for 2 consecutive years.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-personer/senstar

### `STARTAR` / DB: [`idap`]

First Year in the Labor Market.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/beskaeftigelsesoplysninger-der-vedroerer-ida-personer/startar

### `GF_AARE` / DB: [`firm`]

Company profits (kr.).

Profit for the year after taxes measured in kroner. The total result (surplus / loss) of the activity for the financial year after deduction of the corporation tax (SSAR) that caused the activity of the year. In personally owned companies, this year's result must also cover work remuneration to the company's owner / owners.

https://www.dst.dk/da/statistik/dokumentation/times/generel-firmastatistik/gf-aare

### `GF_AARSV` / DB: [`firm`]

Company number of fulltime employees.

- Until 2007: The sum of ATP contributions for all employees. This is basically a count of "FTEs" (Full Time Equivalent) for the company. For example, 3 workers working partially 9-17 hours/week counts as 1 worker fulltime (1/3 + 1/3 + 1/3 = 1 ATP contribution or FTE)

- From the year 2008: The calculation is made from this on the basis of companies' reporting to E-income. The companies report monthly all hours and wages for all their employees, and therefore this is just a count of how many are reported working +27 hours per week.

https://www.dst.dk/da/statistik/dokumentation/times/generel-firmastatistik/gf-aarsv

### `GF_AAT` / DB: [`firm`]

Fixed assets (kr.)

Permanent ownership or use of the company, eg buildings, machinery, furniture, patents, licenses and long-term investments of a financial nature, eg shares and bonds.

https://www.dst.dk/da/statistik/dokumentation/times/generel-firmastatistik/gf-aat

### `GF_AINV` / DB: [`firm`]

Net Investment (kr.)

Investments (ATIT) minus investment departure (AFAT).

https://www.dst.dk/da/statistik/dokumentation/times/generel-firmastatistik/gf-ainv

### `GF_ANSATTE` / DB: [`firm`]

Indicates the number of people employed by the company at the end of November.

https://www.dst.dk/da/Statistik/dokumentation/Times/generel-firmastatistik/gf-ansatte

### `GF_AT` / DB: [`firm`]

Total Assets (kr.) at the end of the year.

https://www.dst.dk/da/statistik/dokumentation/times/generel-firmastatistik/gf-at

### `GF_BAGATEL` / DB: [`firm`]

Code indicating whether the company is above or below the threshold of accounting class for reporting (bagatelgrænse).

- '0' = Above
- '1' = Below
- '3' = Forced below

https://www.dst.dk/da/Statistik/dokumentation/Times/generel-firmastatistik/generel-firmastatistik--esdvh-/gf-bagatel

### `GF_BAV` / DB: [`firm`]

Gross profit (kr.)

Gross profit is calculated as revenue minus consumption of goods minus the purchase of wages and subcontracting.

https://www.dst.dk/da/statistik/dokumentation/times/generel-firmastatistik/gf-bav

### `GF_BD_LS` / DB: [`firm`]

[TO BE DONE]

No documentation available. Markering for branchedækning for lønsumsindbetaling.

### `GF_BD_MO` / DB: [`firm`]

[TO BE DONE]

No documentation available. Markering for branchedækning vedr. momsbetaling .

### `GF_BD_RE` / DB: [`firm`]

[TO BE DONE]

No documentation available. Markering for branchedækning i Generel Regnskabsstatistik

### `GF_BG_METODE` / DB: [`firm`]

Code for the method for determining the variable `GF_bagatel`.

Categorical variable but without documentation of what they mean (e.g. 15, 19, 12)

https://www.dst.dk/da/Statistik/dokumentation/Times/generel-firmastatistik/generel-firmastatistik--esdvh-/gf-bg-metode

### `GF_EGUL` / DB: [`firm`]

Equity (kr.)

Total assets (AT) at the end of the year minus the sum of provisions and other debt obligations.

https://www.dst.dk/da/statistik/dokumentation/times/generel-firmastatistik/gf-egul

### `GF_EKSP` / DB: [`firm`]

Exports (kr.)

Total exports of goods and services without VAT.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/firmastatistik/gf-eksp

### `GF_GR009_DB93` / DB: [`firm`]

Company's main industry expressed by NACE Standard Industry Classification of 9 groups for Danish Industrial Classification of All Economic Activities (Dansk Branchekode) 1993.

Please check the following link for the NACE encodings:
https://www.dst.dk/Site/Dst/Udgivelser/GetPubFile.aspx?id=16684&sid=nace

### `GF_GR027_DB93` / DB: [`firm`]

Company's main industry expressed by NACE Standard Industry Classification of 27 groups for Danish Industrial Classification of All Economic Activities (Dansk Branchekode) 1993.

Please check the following link for the NACE encodings:
https://www.dst.dk/Site/Dst/Udgivelser/GetPubFile.aspx?id=16684&sid=nace

### `GF_GR053_DB93` / DB: [`firm`]

Company's main industry expressed by NACE Standard Industry Classification of 53 groups for Danish Industrial Classification of All Economic Activities (Dansk Branchekode) 1993.

Please check the following link for the NACE encodings:
https://www.dst.dk/Site/Dst/Udgivelser/GetPubFile.aspx?id=16684&sid=nace

### `GF_GR111_DB93` / DB: [`firm`]

Company's main industry expressed by NACE Standard Industry Classification of 111 groups for Danish Industrial Classification of All Economic Activities (Dansk Branchekode) 1993.

Please check the following link for the NACE encodings:
https://www.dst.dk/Site/Dst/Udgivelser/GetPubFile.aspx?id=16684&sid=nace

### `GF_GR010_DB07` / DB: [`firm`]

Company's main industry expressed by NACE Standard Industry Classification of 10 groups for Danish Industrial Classification of All Economic Activities (Dansk Branchekode) 2007.

Please check the following link for the NACE encodings:
https://www.dst.dk/da/Statistik/dokumentation/nomenklaturer/db07

### `GF_GR019_DB07` / DB: [`firm`]

Company's main industry expressed by NACE Standard Industry Classification of 19 groups for Danish Industrial Classification of All Economic Activities (Dansk Branchekode) 2007.

Please check the following link for the NACE encodings:
https://www.dst.dk/da/Statistik/dokumentation/nomenklaturer/db07

### `GF_GR036_DB07` / DB: [`firm`]

Company's main industry expressed by NACE Standard Industry Classification of 36 groups for Danish Industrial Classification of All Economic Activities (Dansk Branchekode) 2007.

Please check the following link for the NACE encodings:
https://www.dst.dk/da/Statistik/dokumentation/nomenklaturer/db07

### `GF_GR127_DB07` / DB: [`firm`]

Company's main industry expressed by NACE Standard Industry Classification of 127 groups for Danish Industrial Classification of All Economic Activities (Dansk Branchekode) 2007.

Please check the following link for the NACE encodings:
https://www.dst.dk/da/Statistik/dokumentation/nomenklaturer/db07

### `GF_NACE2_DB93` / DB: [`firm`]

NACE Company division following Dansk Branchekode 1993.

NACE's first two-digit numerical code. NACE is the acronym used to designate the various statistical classifications of economic activities developed since 1970 in the European Union (EU).

https://www.dst.dk/da/Statistik/dokumentation/Times/generel-firmastatistik/generel-firmastatistik--esdvh-/gf-nace2-db07
https://ec.europa.eu/eurostat/statistics-explained/index.php?title=NACE_background

Please check the following link for the NACE encodings:
https://www.dst.dk/Site/Dst/Udgivelser/GetPubFile.aspx?id=16684&sid=nace

### `GF_NACE3_DB93` / DB: [`firm`]

NACE Company group following Dansk Branchekode 1993.

NACE's first three-digit numerical code. NACE is the acronym used to designate the various statistical classifications of economic activities developed since 1970 in the European Union (EU).

https://www.dst.dk/da/Statistik/dokumentation/Times/generel-firmastatistik/generel-firmastatistik--esdvh-/gf-nace2-db07
https://ec.europa.eu/eurostat/statistics-explained/index.php?title=NACE_background

Please check the following link for the NACE encodings:
https://www.dst.dk/Site/Dst/Udgivelser/GetPubFile.aspx?id=16684&sid=nace

### `GF_NACE_DB93` / DB: [`firm`]

NACE Company class following Dansk Branchekode 1993.

NACE's four-digit numerical code. NACE is the acronym used to designate the various statistical classifications of economic activities developed since 1970 in the European Union (EU).

https://www.dst.dk/da/Statistik/dokumentation/Times/generel-firmastatistik/generel-firmastatistik--esdvh-/gf-nace2-db07
https://ec.europa.eu/eurostat/statistics-explained/index.php?title=NACE_background

Please check the following link for the NACE encodings:
https://www.dst.dk/Site/Dst/Udgivelser/GetPubFile.aspx?id=16684&sid=nace

### `GF_NACE2_DB07` / DB: [`firm`]

NACE Company division following Dansk Branchekode 2007.

NACE's first two-digit numerical code. NACE is the acronym used to designate the various statistical classifications of economic activities developed since 1970 in the European Union (EU).

https://www.dst.dk/da/Statistik/dokumentation/Times/generel-firmastatistik/generel-firmastatistik--esdvh-/gf-nace2-db07
https://ec.europa.eu/eurostat/statistics-explained/index.php?title=NACE_background

Please check the following link for the NACE encodings:
https://www.dst.dk/da/Statistik/dokumentation/nomenklaturer/db07

### `GF_NACE3_DB07` / DB: [`firm`]

NACE Company group following Dansk Branchekode 2007.

NACE's first three-digit numerical code. NACE is the acronym used to designate the various statistical classifications of economic activities developed since 1970 in the European Union (EU).

https://www.dst.dk/da/Statistik/dokumentation/Times/generel-firmastatistik/generel-firmastatistik--esdvh-/gf-nace2-db07
https://ec.europa.eu/eurostat/statistics-explained/index.php?title=NACE_background

Please check the following link for the NACE encodings:
https://www.dst.dk/da/Statistik/dokumentation/nomenklaturer/db07

### `GF_NACE_DB07` / DB: [`firm`]

NACE Company class following Dansk Branchekode 2007.

NACE's four-digit numerical code. NACE is the acronym used to designate the various statistical classifications of economic activities developed since 1970 in the European Union (EU).

https://www.dst.dk/da/Statistik/dokumentation/Times/generel-firmastatistik/generel-firmastatistik--esdvh-/gf-nace2-db07
https://ec.europa.eu/eurostat/statistics-explained/index.php?title=NACE_background

Please check the following link for the NACE encodings:
https://www.dst.dk/da/Statistik/dokumentation/nomenklaturer/db07

### `JUR_HOVED_BRA_DB93` / DB: [`firm`]

Complete six-digit NACE classification code following Dansk Branchekode 1993.

The first four digits of the code are the same in all European countries (`GF_NACE_DB93`). The fifth digit might vary from country to country and further digits are sometimes placed by suppliers of databases.

Encodings available in the documentation:
https://www.dst.dk/da/Statistik/dokumentation/Times/groenne-varer-og-tjenester/jur-hoved-bra-db07

### `JUR_HOVED_BRA_DB07` / DB: [`firm`]

Complete six-digit NACE classification code following Dansk Branchekode 2007.

The first four digits of the code are the same in all European countries (`GF_NACE_DB07`). The fifth digit might vary from country to country and further digits are sometimes placed by suppliers of databases.

Encodings available in the documentation:
https://www.dst.dk/da/Statistik/dokumentation/Times/groenne-varer-og-tjenester/jur-hoved-bra-db07

### `GF_IMPORT` / DB: [`firm`]

Imports (kr.)

Company's total imports. All amounts in kroner without VAT.

https://www.dst.dk/da/statistik/dokumentation/times/generel-firmastatistik/gf-import

### `GF_INKLEJER` / DB: [`firm`]

Number of employees (including the owner).

https://www.dst.dk/da/statistik/dokumentation/times/generel-firmastatistik/gf-inklejer

### `GF_KOB` / DB: [`firm`]

Domestic purchases plus imports (kr.)

Domestic purchases of goods and services as well as imports of goods (but not imports of services).All amounts are in kroner without VAT.

https://www.dst.dk/da/statistik/dokumentation/times/generel-firmastatistik/gf-kob

### `GF_LGAGMV` / DB: [`firm`]

Total Payroll (kr.)

Includes salaries and salaries, pension expenses and other social security costs. Measured in kroner.

https://www.dst.dk/da/statistik/dokumentation/times/generel-firmastatistik/gf-lgagmv

### `GF_MK_RE` / DB: [`firm`]

"1" if company match with General Accounting statistics (Regnskabsstatistik) registry for private urban enterprises.

- '0' = Not match
- '1' = Match
- '2' = Non GF unit.

https://www.dst.dk/da/Statistik/dokumentation/Times/generel-firmastatistik/generel-firmastatistik--esdvh-/gf-mk-re

### `GF_OMS` / DB: [`firm`]

Revenue (kr.)

Company revenue from the sale of products and services that come from the company's primary operations. Measured in kroner.

https://www.dst.dk/da/statistik/dokumentation/times/generel-firmastatistik/gf-oms

### `GF_OPR_OMS` / DB: [`firm`]

Method for calculating Revenue. Variable only containing 1999 data.

No doumentation available.

### `GF_RESDEL1_DB07` / DB: [`firm`]

[TO BE DONE]

No doumentation available.

### `GF_RESDEL1_DB93` / DB: [`firm`]

[TO BE DONE]

No doumentation available.

### `GF_RESDEL2_DB93` / DB: [`firm`]

[TO BE DONE]

No doumentation available.

### `GF_RESHOV1_DB07` / DB: [`firm`]

[TO BE DONE]

No doumentation available.

### `GF_RESHOV1_DB93` / DB: [`firm`]

[TO BE DONE]

No doumentation available.

### `GF_RESHOV2_DB93` / DB: [`firm`]

[TO BE DONE]

No doumentation available.

### `GF_RFEP` / DB: [`firm`]

EBIT / Operational Profit (kr.)

Revenue from primary operations (revenue) and secondary operations (other operating income) less the following costs: consumption of goods and services for ordinary operations, wages and salaries, pension costs and other social security costs, depreciation and write-downs of tangible and intangible fixed assets, and write-downs of current assets to the extent that they exceed normal write-downs.

https://www.dst.dk/da/statistik/dokumentation/times/generel-firmastatistik/gf-rfep

### `GF_VTV` / DB: [`firm`]

Value Added (kr.)

The difference between the value of production and consumption. Essentially the economic value that a business adds to its inputs before passing the product on to the next stage in the production process or to the final consumer.

https://www.dst.dk/da/statistik/dokumentation/times/generel-firmastatistik/gf-vtv

### `JKOD` / DB: [`firm`]

Journal code. Internal code indicating the source from which the company's accounting information originates and the current state of the process.

- 'E' = The company has completed an accounting form electronically through the Danish Commerce and Companies Agency's digital reporting system
- 'R' = The company is listed on the basis of figures from sampled companies and companies from SKAT
- 'S' = The company has some information from SKAT
- 'V' = The company has completed an accounting form electronically through ejr.dk
- 'X' = The company has completed an accounting form electronically in XBRL format
- '0' = Started reporting
- '1' = Postponement
- '2' = Postponement exceeded
- '3' = Denies accounting information
- '4' = Should submit, but is exempt for various reasons (e.g. bankruptcy, liquidation, illness, etc.)
- '5' = The company does not belong to the population, for example because it has been found that the correct industry of the company is not within the sector of accounting - statistics or that it is a pure VAT settlement unit without actual business activity
- '6' = Form submitted in completed form (+ possibly accounting sent)
- '7' = Accounting submitted
- '8' = Completed by DST alone on the basis of alternative sources (eg SKAT, E and S, Danish - Medicines Agency)
- '9' = Waiting

https://www.dst.dk/da/Statistik/dokumentation/Times/regnskabsstatistik-for-private-byerhverv/jkod

### `JUR_BEL_KOM_KODE` / DB: [`firm`]

Company municipality code.

Encodings available in the documentation:
https://www.dst.dk/da/Statistik/dokumentation/Times/Erhvervsregister/JUR-BEL-KOM-KODE

### `JUR_BEL_LDEL_KODE` / DB: [`firm`]

Country code in 2007

[TO BE DONE]

No documentation available.

https://www.dst.dk/da/Statistik/dokumentation/Times/generel-firmastatistik/generel-firmastatistik--esdvh-/jur-bel-ldel-kode

### `JUR_BEL_REGION_KODE` / DB: [`firm`]

Company region code.

- '1084' = Capital Region
- '1085' = Region Zealand
- '1083' = Region of Southern Denmark
- '1082' = Central Jutland region
- '1081' = Region North Jutland
- '10' = COPENHAGEN
- '11' = FREDERIKSBERG
- '15' = COPENHAGEN AMT
- '20' = FREDERIKSBORG AMT
- '25' = ROSKILDE AMT
- '30' = VESTSJÆLLANDS AMT
- '35' = STORSTRØMS AMT
- '40' = BORNHOLMS AMT
- '42' = FYNS AMT
- '50' = SØNDERJYLLANDS AMT
- '55' = RIBE AMT
- '60' = VEJLE AMT
- '65' = RINGKØBING AMT
- '70' = ÅRHUS AMT
- '76' = VIBORG AMT
- '80' = NORDJYLANDS AMT
- '99' = OUTSIDE DENMARK
- '97' = WHOLE COUNTRY
- '98' = Unkwown

https://www.dst.dk/da/statistik/dokumentation/times/generel-firmastatistik/jur-bel-region-kode

### `JUR_FRA_DATO` / DB: [`firm`]

Company start date in the registry.

https://www.dst.dk/da/Statistik/dokumentation/Times/Erhvervsregister/JUR-FRA-DATO

### `JUR_FUNKKODE` / DB: [`firm`]

Breakdown of workplaces into different public and private sectors.

- '11' = State non-financial quasi-corporations
- '12' = Municipal non-financial quasi-corporations
- '13' = Non-financial quasi-corporations of the regions
- '14' = State-owned non-financial corporations
- '15' = Municipal-owned non-financial corporations
- '16' = Region-owned non-financial corporations
- '18' = Private non-financial corporations
- '21' = Central Bank
- '27' = Public money and mortgage banks
- '28' = Private money and mortgage banks
- '31' = Integ. legally state-owned insti.
- '31' = Public money market associations
- '32' = Integ. legally not state-owned insti.
- '32' = Private money market associations
- '33' = Not integral. state institute (quasi)
- '33' = State and quasi-state self-indulgence. ins
- '34' = Social funds or funds
- '37' = Public investment funds
- '38' = Private investment funds
- '41' = Integ. legal county municipal-owned institute.
- '41' = Other public financial intermediaries, except insurance companies and pension funds
- '42' = Integ. legally not county-owned inst.
- '42' = Other private financial intermediaries, except insurance companies and pension funds
- '43' = Not integral. county council (quasi)
- '43' = Reg. and quasi-reg. selvej. institutions
- '47' = Public financial aid units
- '48' = Private Financial Aid Units
- '51' = Integ. legally municipal owned inst.
- '51' = Public group affiliated financial entities
- '52' = Integ. legally not come. owned inst.
- '52' = Private group affiliated financial entities
- '53' = Not integral. municipal institute (quasi)
- '53' = Comm. and quasi-comm. selvej. inst.
- '57' = Public insurance companies
- '58' = Private insurance companies
- '61' = Integ. legal state company similar.virk.
- '61' = Public pension funds
- '62' = Integ. jur. amtkom. company similar. work.
- '62' = Private pension funds
- '63' = Integ. jur. primary came. company. work.
- '70' = Not integr. off. sj.org. as a company
- '71' = Government administration and service - integrated entities
- '72' = Government administration and service - non-integrated entities
- '74' = Regional management and service - integrated units
- '75' = Regional management and service - non-integrated entities
- '76' = Municipal administration and service - integrated units
- '77' = Municipal administration and service - non-integrated entities
- '79' = Social funds and funds
- '80' = Private area
- '81' = Personally owned companies
- '89' = Non-profit institutions aimed at households
- '90' = Abroad
- '91' = International organizations (international organizations, eg EU institutions and foreign embassies in DK)
- '99' = Not provided

https://www.dst.dk/da/statistik/dokumentation/times/generel-firmastatistik/jur-funkkode

### `JUR_TIL_DATO` / DB: [`firm`]

Company end date in the registry.

https://www.dst.dk/da/Statistik/dokumentation/Times/Erhvervsregister/JUR-TIL-DATO

### `JUR_VIRK_FORM` / DB: [`firm`]

Code for business legal form (e.g. cooperative, individual company, limited company, etc.)

Encodings available in the documentation:
https://www.dst.dk/da/Statistik/dokumentation/Times/generel-firmastatistik/jur-virk-form

### `R_TID` / DB: [`firm`]

Update date.

[TO BE DONE]

[NO DOCUMENTATION AVAILABLE]

I guess it's the date of when the data was uploaded/refreshed. No documentation available.

## `PRODNR` / DB: [`frpe`]

10 digits Production Unit Number. Also called "P number", its a unique ID for each physical location from which a company operates.

https://www.dst.dk/da/Statistik/dokumentation/Times/forskningsservice/prodnr

## `ANSID` / DB: [`frpe`]

Employment Identification. A person may have several different if the person has been employed in several places over a year.

https://www.dst.dk/da/Statistik/dokumentation/Times/fravaer/ansid

### `AAR` / DB: [`firm`,`frpe`]

Year

https://www.dst.dk/da/Statistik/dokumentation/Times/fravaer/aar

### `AFLORM` / DB: [`frpe`]

Salary Form.

From 1997-2001:

- '1' = Hourly pay (when more than 50% of salary as time salary).
- '2' = Hourly pay, performance based (when more than 50% as a chord, bonus, etc.).
- '3' = Fixed pay with overtime pay (extra payment for overtime).
- '4' = Fixed pay without overtime pay (without extra payment for overtime).
- '5' = Fixed pay with commission (more than 50% of salary is payment in relation to revenue).
- '8' = Remuneration from other bodies or due to rehabilitation and the like. not paid according to common rules in the company.
- '9' = Not employees (eg holders and board members).

From 2002 - Present:

- '0' = Fix payment
- '1' = Hourly payment

https://www.dst.dk/da/Statistik/dokumentation/Times/fravaer/aflform
`

### `ALDER_LON` / DB: [`frpe`]

Age at the time of the employment relationship.

https://www.dst.dk/da/Statistik/dokumentation/Times/fravaer/alder-lon

### `FRAVAARSAG`

Reason for work absence.

- '1100' = cc (inclydung pregnancy-related illness)
- '1200' = Child's disease
- '1300' = Work accident
- '1400' = Maternity and Adoption Leave

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/fravaer/fravaarsag

### `BARSELVAEGT` / DB: [`frpe`]

Parental Leave Weight.

It is enumerated at the company level, so that all persons in the same company receive the same weight. Empty values for employees of companies with less than 10 people headcount.

Weight of `FRAVAARSAG` = 1400 (Maternity and Adoption Leave) over other absence causes.

https://www.dst.dk/da/Statistik/dokumentation/Times/fravaer/barselvaegt

### `FRAVVAEGT`

Absence weight.

The absenteeism weight is only used in the private sector and has the value 1 for the public sector. The private sector absenteeism is typically between 0.8-30.

Weight of absence (absence) own illness (1100), children's illness (1200) and work accident (1300) over other absence causes.

https://www.dst.dk/da/Statistik/dokumentation/Times/fravaer/fravvaegt

### `VAEGT_ESR` / DB: [`frpe`]

Business total absence registered weight

https://www.dst.dk/da/Statistik/dokumentation/Times/fravaer/vaegt-esr

### `BRAARB` / DB: [`frpe`]

Workplace industry.

It uses the six-digit NACE classification code following Dansk Branchekode 2007.
(see `JUR_HOVED_BRA_DB07`) applied to people instead of whole companies.

2 people within the same company can work in different workplaces (`PRODNR`) and different industries (e.g. HR / Tech), therefore have different `BRAARB`.

https://www.dst.dk/da/Statistik/dokumentation/Times/fravaer/braarb

### `BRAFIR` / DB: [`frpe`]

Legal Business code for the company the person is employeed.

Six-digit NACE classification code following Dansk Branchekode 2007.
(see `JUR_HOVED_BRA_DB07`)

https://www.dst.dk/da/Statistik/dokumentation/Times/fravaer/brafir

### `DATOOPRET` / DB: [`frpe`]

Date of creation of the data.

No much documentation available, but my guess is that when the data entry was created. For example the 2011 data (`frpe2011`) was created aferwards (e.g. `DATOOPRET` = 2013) as it takes time to collect company data.

https://www.dst.dk/da/Statistik/dokumentation/Times/fravaer/datoopret

### `FRAVPERIODE` / DB: [`frpe`]

Absence period.

Number of periods of absence in the counting year. If this person did not have a absence period related to parental leave is empty, 1 if one time, etc.

Unless rare exceptions, its categorical variable (empty or 1).

https://www.dst.dk/da/Statistik/dokumentation/Times/fravaer/fravperiode

### `FRAVTIMER` / DB: [`frpe`]

Absence hours.

Number of absence hours in the part of the absence period that lies in the counting year.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/fravaer/fravtimer

### `FRAV_FRADATO` / DB: [`frpe`]

Start date of the absence period.

https://www.dst.dk/da/Statistik/dokumentation/Times/fravaer/frav-fradato

### `FRAV_TILDATO` / DB: [`frpe`]

End date of absence period.

https://www.dst.dk/da/Statistik/dokumentation/Times/fravaer/frav-tildato

### `FUNK` / DB: [`frpe`]

Employee job function.

From 1996 - 2010:

Follows DISCOLØN 2004 codes.

From 2010 - Present:

Follows DISCO-08 codes.

Danish version of ISCO-08 by the International Labor Organization (ILO). Classification groups the work functions so that the classification at the most detailed level is 6 digits and consists of a total of 558 work function codes.

Encoding in the documentation:

https://www.dst.dk/da/Statistik/dokumentation/Times/fravaer/funk

### `KALENDERDAGE` / DB: [`frpe`]

Number of calendar days (includes weekends and holidays) of absence. Calculated from `FRAV_FRADATO` to `FRAV_TILDATO`

https://www.dst.dk/da/Statistik/dokumentation/Times/fravaer/kalenderdage

### `KOMARB` / DB: [`frpe`]

Workplace municipality.

Municipality of the employee works linked to the workplace.

Encodings: https://www.dst.dk/en/Statistik/dokumentation/nomenklaturer/nuts

https://www.dst.dk/da/Statistik/dokumentation/Times/fravaer/komarb

### `REFERENCETID` / DB: [`frpe`]

Datetime reference.

(Eg. `REFERENCETID` = 2011-31-12 and `AAR` = 2011 for all rows in `frpe2011`)

https://www.dst.dk/da/Statistik/dokumentation/Times/fravaer/referencetid

### `REFERENCTYPE` / DB: [`frpe`]

https://www.dst.dk/da/Statistik/dokumentation/Times/fravaer/referencetype

### `SEKTOR` / DB: [`frpe`]

Classification of the worker sector into public/private.

- '1' = Private
- '2' = State
- '3' = Municipality / region

https://www.dst.dk/da/Statistik/dokumentation/Times/fravaer/sektor

### `ARBGNRTI` / DB: [`idas`]

Workplace ID - To

This is the identifier for the workplace after a change (like a merger or split). Used to track workplace transitions.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/arbgnrti

### ARBGNRFR / DB: [`idas`]

Workplace ID - From

This is the identifier for the workplace before a change (like a merger or split). Used to track workplace transitions.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/arbgnrfr

### AARSVRK / DB: [`idas`]

FTEs / Full-time Equivalent Employees

Measures the total labor input converted to full-time positions, including part-time workers converted to full-time equivalents.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/aarsvrk

### ANDELOPS / DB: [`idas`]

Share of Dissolution

Represents the proportion of a workplace that was dissolved in cases of split-ups or reorganizations.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/andelops

### ANDELUDS / DB: [`idas`]

Share of Split-off

Indicates the proportion of a workplace that was split off to form new units

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/andeluds

### ANDFA / DB: [`idas`]

Share of Skilled Workers

Represents the proportion of skilled workers in the workplace's workforce.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/andfa

### ANDHF / DB: [`idas`]

Share of Workers with Higher Education

Represents the proportion of employees with higher education qualifications.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/andhf

### ANDIF / DB: [`idas`]

Share of Workers with Intermediate Education

Represents the proportion of employees with intermediate level education.
https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/andif

### ANDELDF / DB: [`idas`]

[TO BE DONE]

[NO DOCUMENTATION AVAILABLE]

### ANDLF / DB: [`idas`]

Share of Unskilled Workers

Represents the proportion of unskilled workers in the workplace's workforce.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/andlf

### ANTAAR / DB: [`idas`]

Number of Years

Indicates the number of years the workplace has existed in the statistics.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/antaar

### ANTONOV / DB: [`idas`]

[TO BE DONE]

[NO DOCUMENTATION AVAILABLE]

### ARBSTK / DB: [`idas`]

Workplace Status Code

Indicates the current status of the workplace (active, closed, etc.).

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/arbstk

### ARBSTKFR / DB: [`idas`]

Workplace Status Code - From

Status code of the workplace before a transition or change.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/arbstkfr

### ARBSTKTI / DB: [`idas`]

Workplace Status Code - To

Status code of the workplace after a transition or change.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/arbstkti

### BRANCHE1 / DB: [`idas`]

[TO BE DONE]

[NO DOCUMENTATION AVAILABLE]

### EJERKO / DB: [`idas`]

Ownership Code

Indicates the type of ownership of the workplace (private, public, etc.).

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/ejerko

### ENDNDL / DB: [`idas`]

Final Closure

Indicates whether the workplace has permanently closed down.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/endnedl

### FILIAL / DB: [`idas`]

Branch Indicator

Indicates whether the workplace is a branch/subsidiary of another company.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/filial

### FRELFREM / DB: [`idas`]

Future Relationship

Indicates the workplace's relationship to future workplace units.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/frelfrem

### FRELTILB / DB: [`idas`]

Past Relationship

Indicates the workplace's relationship to previous workplace units.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/freltilb

### IDTILB / DB: [`idas`]

Back-reference ID

Identifier used to link workplace information with previous periods.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/idtilb

### KVANDFA / DB: [`idas`]

Number of Skilled Workers

Count of skilled workers employed at the workplace.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/kvandfa

### KVANDHF / DB: [`idas`]

Number of Workers with Higher Education

Count of employees with higher education qualifications.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/kvandhf

### KVANDIF / DB: [`idas`]

Number of Workers with Intermediate Education

Count of employees with intermediate level education.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/kvandif

### KVANDLF / DB: [`idas`]

Number of Unskilled Workers

Count of unskilled workers at the workplace.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/kvandlf

### LBNRFREM / DB: [`idas`]

Forward Reference Number

Sequential number used for tracking future workplace relationships.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/lbnrfrem

### LBNRTILB / DB: [`idas`]

Backward Reference Number

Sequential number used for tracking previous workplace relationships.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/lbnrtilb

### LEDPERG / DB: [`idas`]

Management Personnel Group

Classification code for management level personnel at the workplace.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/ledperg

### LGRGNSAR / DB: [`idas`]

Geographical Location Year

Reference year for the workplace's geographical location information.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/lgrgnsar

### LONAAR / DB: [`idas`]

Wage Year

Reference year for wage information.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/lonaar

### LONGNSFA / DB: [`idas`]

Longitudinal ID - Skilled Workers

Tracking identifier for skilled worker categories over time.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/longnsfa

### LONGNSHF / DB: [`idas`]

Longitudinal ID - Higher Education

Tracking identifier for higher education categories over time.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/longnshf

### LONGNSIF / DB: [`idas`]

Longitudinal ID - Intermediate Education

Tracking identifier for intermediate education categories over time.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/LONGNSIF

### LONGNSLF / DB: [`idas`]

Longitudinal ID - Unskilled Workers

Tracking identifier for unskilled worker categories over time.

https://www.dst.dk/da/tilsalg/forskningsservice/dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/longnslf

### `AKTIEINDK` / DB: [`ind`, `indh`]

Stock Income (kr.)

**Available from 1980 - Present**. Income earned from stocks and dividends.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/personindkomster/aktieindk

### `ARBFORS` / DB: [`ind`, `indh`]

Mandatory labor market contribution payments (kr.)

**Available from 1984 - Present**. Unemployment insurance, professional quotas, early retirement and flexible benefit contributions (Rubrik52)

### `ARBLHUMV` / DB: [`ind`, `indh`]

Unemployment benefits and education allowances (kr.)

**Available from 1980 - Present**. Payments for unemployment insurance and early retirement schemes.

https://www.dst.dk/da/Statistik/dokumentation/Times/personindkomst/arblhumv

### `BESKST` / DB: [`ind`, `indh`]

Employment status.

**Only available from 1994 to 2013**. Code for a person's main source of income during the year.

- '01' = Self employed
- '02' = Work.
- '03' = Wage Mature. m. active.
- '04' = Employee
- '05' = Employee with support.
- '06' = Pensioner with effect.
- '07' = Pensioner
- '08' = Other
- '99' = Not in AKM

https://www.dst.dk/da/Statistik/dokumentation/Times/personindkomst/beskst

### `BESKST13` / DB: [`ind`]

Employment status (2013 Definition)

**Available from 1980 - Present**. Code for a person's main source of income during the year.

- '01' = Self employed
- '02' = Employee spouse
- '03' = Employee and owner of business
- '04' = Employee
- '05' = Employee with support
- '06' = Pensioner and owner of business
- '07' = Pensioner
- '08' = Others
- '09' = Retirement Beneficiary
- '10' = Unemployed at least half of the year (net unemployment)
- '11' = Beneficiary of unemployment benefit (illness, maternity leave)
- '12' = Cash Beneficiary
- '99' = Not in AKM

https://www.dst.dk/da/Statistik/dokumentation/Times/personindkomst/beskst13

### `BRUTTO` / DB: [`ind`, `indh`]

Gross Income (kr.)

**Only available from 1980 to 2013**. Total taxable gross income before deductions.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/personindkomster/brutto

### `DISPON_13` / DB: [`ind`]

Disposable Income (kr.) (2013 Definition).

**Available from 1980 - Present**. Income available after taxes and mandatory payments (e.g. labor market contributions). It can be negative for self-employed people. According to new 2013 definitions (https://www.dst.dk/Site/Dst/SingleFiles/GetArchiveFile.aspx?fi=arbe&fo=rev13--pdf&ext={2})

https://www.dst.dk/da/Statistik/dokumentation/Times/personindkomst/dispon-13

### `DISPON_NY` / DB: [`ind`, `indh`]

Disposable Income (kr.)

**Only available from 1980 to 2013**. Updated calculation of disposable income. Please check the documentation below if you use both `DISPON_13` in combination with `DISPON_NY`

https://www.dst.dk/da/Statistik/dokumentation/Times/personindkomst/dispon-ny

### `EJENDOMSVURDERING` / DB: [`ind`, `indh`]

Property Assets (kr.)

**Available from 1994 - Present**. Annual valuation of owned property. The source of the variables `EJENDOMSVURDERING` and `KOEJD` are two different public registers, where the withdrawal time from the registers can cause differences in the statements from the two registers, where there should theoretically be the same value.

https://www.dst.dk/da/Statistik/dokumentation/Times/personindkomst/ejendomsvurdering

### `ERHVERVSINDK` / DB: [`ind`, `indh`]

Business Income (kr.)

**Only available from 1994 to 2013**. Business income, salary and net profit of self-employed business incl. certain fees

https://www.dst.dk/da/Statistik/dokumentation/Times/personindkomst/erhvervsindk

### `ERHVERVSINDK_13` / DB: [`ind`]

Business Income (2013 Definition).

**Available from 1980 - Present**. Business income according to new 2013 definitions (https://www.dst.dk/Site/Dst/SingleFiles/GetArchiveFile.aspx?fi=arbe&fo=rev13--pdf&ext={2})

https://www.dst.dk/da/Statistik/dokumentation/Times/personindkomst/erhvervsindk-13

### `ERHVERVSINDK_GL` / DB: [`ind`]

Business Income (kr.) (Old Definition)

**Only available from 1980 to 2013**. Replaced by the variable `ERHVERVSINDK_13`.

https://www.dst.dk/da/Statistik/dokumentation/Times/personindkomst/erhvervsindk-gl

### `FORMREST_NY05` / DB: [`ind`, `indh`]

Net Wealth excluding pension (kr.) (2005 Definition)

**Available from 1997 - Present**. Value of all assets under 2005 definition exluding pension.

### `FORMUEINDK_BRUTTO` / DB: [`ind`]

Gross Capital Income (kr.)

**Available from 1980 - Present**. The gross income is the sum of interest income and other wealth income, which consists of dividends and realized losses / gains on securities. Excl. calculated rental value of own housing, as well as from 1987 excl. income from self-employment.

https://www.dst.dk/da/Statistik/dokumentation/Times/Personindkomst/FORMUEINDK-BRUTTO

### `FORMUEINDK_NY` / DB: [`ind`, `indh`]

Capital Income (kr.) (2013 Definition)

**Only available from 1980 to 2013**. Replaced by the variable `FORMUEINDK_BRUTTO`

https://www.dst.dk/da/Statistik/dokumentation/Times/personindkomst/formueindk-ny

### `FRADRAG` / DB: [`ind`, `indh`]

Total Deductions (kr.)

**Available from 1980 - Present**. Deductions for private payments for pension schemes, interest expenses paid, driving deductions, maintenance and child support, expenses for unemployment insurance, professional quota, early retirement scheme, employment deduction and more.

https://www.dst.dk/da/Statistik/dokumentation/Times/personindkomst/fradrag

### `KOEJD` / DB: [`ind`, `indh`]

Property Assets (kr.)

**Available from 1983 - Present**. Annual valuation of owned property. The source of the variables `EJENDOMSVURDERING` and `KOEJD` are two different public registers, where the withdrawal time from the registers can cause differences in the statements from the two registers, where there should theoretically be the same value.

https://www.dst.dk/da/Statistik/dokumentation/Times/Personindkomst/KOEJD

### `LOENMV` / DB: [`ind`]

Total salary income (kr.)

**Only available from 1980 to 2013**. Taxable salary incl. perks, tax-free pay, anniversary and severance pay, and value of stock options.

https://www.dst.dk/da/Statistik/dokumentation/Times/personindkomst/loenmv

### `LOENMV_13` / DB: [`ind`, `indh`]

Total salary income (kr.) (2013 Definition)

**Available from 1980 - Present**. Taxable salary incl. perks, tax-free pay, anniversary and severance pay, and value of stock options.

https://www.dst.dk/da/Statistik/dokumentation/Times/Personindkomst/LOENMV-13

### `NETOVSKUD` / DB: [`ind`, `indh`]

Net Profit (kr.)

**Only available from 1994 to 2013**.

https://www.dst.dk/da/Statistik/dokumentation/Times/personindkomst/netovskud

### `NETOVSKUD_13` / DB: [`ind`]

Net Profit (kr.) (2013 Definition)

**Available from 1980 - Present**. Net profit from self-employment including capital income and expenses (including interest) . Company income is self-declared B income, as opposed to salary and transfer income, which is reported to the payer's tax.

https://www.dst.dk/da/Statistik/dokumentation/Times/Personindkomst/NETOVSKUD-13

### `NETOVSKUD_GL` / DB: [`ind`, `indh`]

Net Profit (kr.) (Old Definition)

**Only available from 1980 to 2013**.

https://www.dst.dk/da/Statistik/dokumentation/Times/personindkomst/netovskud-gl

### `OVSKEDJO2_NY` / DB: [`ind`]

Accommodation rental value (kr.)

**Only available from 1980 to 2006**. From 2007, this variable (estimated value) is replaced by the variable `OVSKEJD07` (calculated rental value of own housing).

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/personindkomster/ovskejd02-ny

### `PERINDKIALT` / DB: [`ind`]

Total Personal Income (kr.)

**Only available from 1980 to 2013**. Total personal income excl. calculated rental value of own housing (`OVSKEJD07`) and before deduction of interest expenses.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/personindkomster/perindkialt

### `PERINDKIALT_13` / DB: [`ind`]

Total Personal Income (kr.) (2013 Definition).

**Available from 1980 - Present**. Total personal income under 2013 revision. Total personal income excl. calculated rental value of own housing (`OVSKEJD07`) and before deduction of interest expenses.

https://www.dst.dk/da/Statistik/dokumentation/Times/personindkomst/perindkialt-13

### `PEROEVRIGFORMUE` / DB: [`ind`]

Rental Income (kr.)

Income/profits from appartments rental, holiday rental, profits from sale of real state, etc.

**Only available from from 1980 to 2013**. Replaced by `PEROEVRIGFORMUE_13`.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/personindkomster/peroevrigformue

### `PEROEVRIGFORMUE_13` / DB: [`ind`]

Rental Income (kr.) (2013 Definition).

**Only available from 1980 to 2013**.Income/profits from appartments rental, holiday rental, profits from sale of real state, etc.

https://www.dst.dk/da/Statistik/dokumentation/Times/personindkomst/peroevrigformue-13

### `PERSAMLINKNETRENT_NY` / DB: [`ind`]

Total Personal Income with Net interest (kr.)

**Only available from 1980 to 2013**. Updated calculation of total income including deductible interest expenses on the tax bracket, deduction of labor market contributions and special pension contributions.

https://www.dst.dk/da/Statistik/dokumentation/Times/personindkomst/persamlinknetrent-ny

### `PERSONINDK` / DB: [`ind`, `indh`]

Total Personal income without Capital income (kr.)

**Available from 1980 - Present**. Capital income is a term for the return on a person's or family's assets. This includes, for example, interest, share dividends, and realized gains and losses on shares and other securities, etc.

https://www.dst.dk/da/Statistik/dokumentation/Times/Personindkomst/PERSONINDK

### `QAKTIVF_NY05` / DB: [`ind`, `indh`]

Total Assets (kr.) (2005 Definition).

**Available from 1995 - Present**. Value of personal active assets under 2005 definition excluding pension.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/personindkomster/qaktivf-ny05

### `QIVARK` / DB: [`ind`, `indh`]

Tax on Capital Income (kr.)

**Only available from 1988 - 2001**. Pleace notice that the tax percentage change depending on the years that will affect this quantity.

https://www.dst.dk/da/Statistik/dokumentation/Times/Personindkomst/QAKTSKA

### `QPASSIVN` / DB: [`ind`, `indh`]

Liabilities to the State (kr.)

**Available from 1995 - Present**. Liabilities at year-end including mortgage debt, bank debt, or student debt (Hypotekbanken). Private debt is not included.

https://www.dst.dk/da/Statistik/dokumentation/Times/Personindkomst/QPASSIVN

### `QSPLINDK` / DB: [`ind`, `indh`]

Taxable Income (kr.)

**Available from 1980 - Present**. All income that comes to ordinary taxation (e.g. not capital tax included) minus deductions.

For details, please check the documentation as it changes in relation with the danish legislation at the time.

https://www.dst.dk/da/Statistik/dokumentation/Times/Personindkomst/QSPLINDK

### `RENTEINDK` / DB: [`ind`, `indh`]

Total taxable interest income from Denmark (kr.)

**Only available from 1980 - 2013**.

https://www.dst.dk/da/Statistik/dokumentation/Times/personindkomst/renteindk

### `SAMLINK_NY` / DB: [`ind`, `indh`]

Total Personal Income (kr.)

**Only available from 1980 to 2013**. Total income incl. calculated rental value before deduction of interest expenses, and before deduction of labor market contributions and special pension contributions.

https://www.dst.dk/da/Statistik/dokumentation/Times/personindkomst/samlink-ny

### `SKATMVIALT_13` / DB: [`ind`]

Taxes (kr.) (2013 Definition)

**Available from 1980 - Present**. Amount of taxes corresponding to the person including labor market contribution, pension, and other (excludes church treasure).

For details, please check the documentation as it changes in relation with the danish legislation at the time.

https://www.dst.dk/da/Statistik/dokumentation/Times/Personindkomst/SKATMVIALT-13

### `SKATMVIALT_NY` / DB: [`ind`, `indh`]

Taxes (kr.)

**Only available from 1980 - 2013**. Amount of taxes corresponding to the person including labor market contribution, pension, and other.

https://www.dst.dk/da/Statistik/dokumentation/Times/personindkomst/skatmvialt-ny

### `SKATTOT_NY` / DB: [`ind`, `indh`]

Total Tax (kr.)

**Only available from 1980 - 2013**. The variable consists of state tax, county tax (1980-2006), health contribution (from 2007), municipal tax, church tax, wealth tax (before 1997), special income tax (before 1996), provisionally paid corporate tax (from 1987), property value tax (from 2000), state pension contribution. The final tax is calculated after deduction of various reductions and the inclusion of various tax surcharges.

https://www.dst.dk/da/Statistik/dokumentation/Times/personindkomst/skattot-ny

### `VIRKORDIND` / DB: [`ind`, `indh`]

Business scheme Income (kr.)

**Available from 1987 - Present**. Special scheme for self-employed and artists, it gives the self-employed the opportunity to tax some of their income from the company from a year of high income to a year of low income.

https://www.dst.dk/da/Statistik/dokumentation/Times/Personindkomst/VIRKORDIND

### `DISCOALLE_INDK` / DB: [`indh`]

**Only available from 1991 - 2009**. Employment Classification code.

Encodings available in the documentation:
https://www.dst.dk/da/Statistik/dokumentation/Times/personindkomst/discoalle-indk

### `FODTIDATO` / DB: [`indh`]

**Only available from 1992 - 2007**.

### `KO` / DB: [`indh`]

Gender (CPR based).

- '1' = Male
- '2' = Female
- '9' = Unknown / Company

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/folketal/koen

### `NACE` / DB: [`indh`]

Workplace Industry.

**Only available from 1992 - 2007**. It uses the six-digit NACE classification code following Dansk Branchekode 1993. `NACE_DB07` is not available but `BRAARB` from `frpe` contain NACE Codes from 2010 at `PNR` level following Dansk Branchekode 2007.

### `PERSAMLINKRENT_NY` / DB: [`indh`]

Please check `PERINDKIALT_13` from Database `ind` instead.

[NO DOCUMENTATION AVAILABLE]

### `SOCIO` / DB: [`indh`]

Please check `STILL` from Database `idan` instead.

https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/personers-tilknytning-til-arbejdsmarkedet-set-over-hele-aaret--akm-/socio

### `OPGIKOM` / DB: [`nogt`]

### `OPGIKOM_GL` / DB: [`nogt`]

### `KOM_GL` / DB: [`nogt`]

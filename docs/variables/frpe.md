# Working absence and parental leave database (2010-2021)


### `PNR`

Unique identification of person is used as key to `PERSON_ID`.

People's anonimized CPR. All CPR PNRs are converted to a unidentified PERSON_ID.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/folketal/pnr)


### `KOEN`

Gender (CPR based).

- '1' = Male
- '2' = Female
- '9' = Unknown / Company


### `CVRNR`

Central Business Register (CVR) number. The CVR number is the unique id of a legal entity.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/forskningsservice/cvrnr)

### `VERSION`

Time reference. The first time data is loaded is `VERSION = 01` for a given REFERENCE TIME, the second time `VERSION = 02`, etc.

[Official Documentation link](https://www.dst.dk/da/statistik/dokumentation/times/moduldata-faelles-variable/version)



### `PRODNR`

10 digits Production Unit Number. Also called "P number", its a unique ID for each physical location from which a company operates.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/forskningsservice/prodnr)

### `ANSID`

Employment Identification. A person may have several different if the person has been employed in several places over a year.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/fravaer/ansid)

### `AAR`

Year

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/fravaer/aar)

### `AFLORM`

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

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/fravaer/aflform)
`

### `ALDER_LON`

Age at the time of the employment relationship.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/fravaer/alder-lon)


### `FRAVAARSAG`

Reason for work absence.

- '1100' = Common disease (inclydung pregnancy-related illness)
- '1200' = Child's disease
- '1300' = Work accident
- '1400' = Maternity and Adoption Leave

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/fravaer/fravaarsag)

### `BARSELVAEGT`

Parental Leave Weight.

It is enumerated at the company level, so that all persons in the same company receive the same weight. Empty values for employees of companies with less than 10 people headcount.

Weight of `FRAVAARSAG` = 1400 (Maternity and Adoption Leave) over other absence causes.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/fravaer/barselvaegt)


### `FRAVVAEGT`

Absence weight.

The absenteeism weight is only used in the private sector and has the value 1 for the public sector. The private sector absenteeism is typically between 0.8-30.

Weight of absence (absence) own illness (1100), children's illness (1200) and work accident (1300) over other absence causes.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/fravaer/fravvaegt)

### `VAEGT_ESR`

Business total absence registered weight

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/fravaer/vaegt-esr)

### `BRAARB`

Workplace industry.

It uses the six-digit NACE classification code following Dansk Branchekode 2007.
(see `JUR_HOVED_BRA_DB07`) applied to people instead of whole companies.

2 people within the same company can work in different workplaces (`PRODNR`) and different industries (e.g. HR / Tech), therefore have different `BRAARB`.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/fravaer/braarb)

### `BRAFIR`

Legal Business code for the company the person is employeed.

Six-digit NACE classification code following Dansk Branchekode 2007.
(see `JUR_HOVED_BRA_DB07`)

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/fravaer/brafir)

### `DATOOPRET`

Date of creation of the data.

No much documentation available, but my guess is that when the data entry was created. For example the 2011 data (`frpe2011`) was created aferwards (e.g. `DATOOPRET` = 2013) as it takes time to collect company data.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/fravaer/datoopret)

### `FRAVPERIODE`

Absence period.

Number of periods of absence in the counting year. If this person did not have a absence period related to parental leave is empty, 1 if one time, etc.

Unless rare exceptions, its categorical variable (empty or 1).

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/fravaer/fravperiode)

### `FRAVTIMER`

Absence hours.

Number of absence hours in the part of the absence period that lies in the counting year.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/fravaer/fravtimer)

### `FRAV_FRADATO`

Start date of the absence period.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/fravaer/frav-fradato)

### `FRAV_TILDATO`

End date of absence period.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/fravaer/frav-tildato)

### `FUNK`

Employee job function.

- From 1996 - 2010: Follows DISCOLØN 2004 codes.

- From 2010 - Present: Follows DISCO-08 codes.

Danish version of ISCO-08 by the International Labor Organization (ILO). Classification groups the work functions so that the classification at the most detailed level is 6 digits and consists of a total of 558 work function codes.

Encoding in the documentation:

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/fravaer/funk)

### `KALENDERDAGE`

Number of calendar days (includes weekends and holidays) of absence. Calculated from `FRAV_FRADATO` to `FRAV_TILDATO`

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/fravaer/kalenderdage)

### `KOMARB`

Workplace municipality.

Municipality of the employee works linked to the workplace.

Encodings: [Official Documentation link](https://www.dst.dk/en/Statistik/dokumentation/nomenklaturer/nuts)

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/fravaer/komarb)

### `REFERENCETID`

Datetime reference.

(Eg. `REFERENCETID` = 2011-31-12 and `AAR` = 2011 for all rows in `frpe2011`)

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/fravaer/referencetid)

### `REFERENCTYPE`

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/fravaer/referencetype)

### `SEKTOR`

Classification of the worker sector into public/private.

- '1' = Private
- '2' = State
- '3' = Municipality / region

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/fravaer/sektor)

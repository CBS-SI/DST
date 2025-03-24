# IDA-Workplace Database (`idas`)


### `ARBGNR`

Workplace 12-digits Unique Code.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/arbgnr)

### `ARBGNRTI`

Workplace ID - To

This is the identifier for the workplace after a change (like a merger or split). Used to track workplace transitions.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/arbgnrti)

### `ARBGNRFR`

Workplace ID - From

This is the identifier for the workplace before a change (like a merger or split). Used to track workplace transitions.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/arbgnrfr)

### `LBNR`

Unique serial number per workplace that is constant over time for preserved (not definitively closed) workplaces.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/ida-databasen/ida-ansaettelser/lbnr)


### `AARSVRK`

FTEs / Full-time Equivalent Employees

Measures the total labor input converted to full-time positions, including part-time workers converted to full-time equivalents.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/aarsvrk)

### `ANDELOPS`

Percentage of employees (in integers) that remained from a closed Workplace ID to a the new Workplace ID after a merge or disolution.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/andelops)

### `ANDELUDS`

Percentage of employees (in integers) that were transfered from a closed Workplace ID to a different Workplace after a merge or disolution.

Indicates the proportion of a workplace that was split off to form new units

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/andeluds)

### `ANDFA`

Percentage of Skilled Workers in the Workplace.

Represents the proportion of "Basic" workers (`PTILL` = 35).The "basic" comes from `SOCIO` - used to be "skilled".

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/andfa)

### `ANDHF`

Percentage of Workers at the Highest level in the Workplace.

Represents the proportion of "top executives and employees at the highest level (PSTILL=31-33).

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/andhf)

### `ANDIF`

Percentage of Non-Skilled Workers in the Workplace.

Represents the proportion of "Other employee" workers (`PTILL` = 36).The "Other employee" comes from `SOCIO` - used to be "non-skilled worker".

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/andif)

### `ANDLEDAR`

Percentage of Unemployed Employees generated

Represents the number of employees who has been employed at the workplace the year before and been unemployed in the year of the registry.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/ida-databasen/ida-arbejdssteder/andledar)

### `ANDLF`

Percentage of "Mid-level" Workers in the Workplace.

Represents the proportion of "Mid-level or intermediate" workers (`PTILL` = 34).The "Intermediate" comes from `SOCIO` - used to be "non-skilled worker".

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/andlf)

### `ANTAAR`

Number of Employees.

This variable is similar to `AARSVRK`. The difference `ANTAAR` counts the number of people (number of heads) who have been employed at the relevant workplace, whereas `AARSVRK` converts the employment to full-time employees (FTEs) at the workplace.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/antaar)

### `ANTONOV`

Number of November-employees.

Basically, an end of the year headcount. All November-related jobs at the workplace, whether the job is the primary, secondary, tertiary, etc. Jobs consist of employment relationships where you usually work the equivalent of 1 hour a week at the reference time at the end of November.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/antnov)

### `ARBSTK`

Workplace Status Code.

Indicates the current status of the workplace (active, closed, etc.).

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/arbstk)

### `ARBSTKFR`

Workplace Status Code - From.

Status code of the workplace before a transition or change.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/arbstkfr)

### `ARBSTKTI`

Workplace Status Code - To.

Status code of the workplace after a transition or change.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/arbstkti)

### `BRANCHE1`

NACE Industry Code (DB93) for the Workplace.

From `1993` on the grouping changed. This variable no longer exist, replaced by `BRANCHE3`).

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/branche03)

### `EJERKO`

Ownership type.

Indicates the type of ownership of the workplace (private, public, etc.).

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/ejerko)

### `ENDNDL`

Final Closure.

Indicates whether the workplace has permanently closed down.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/endnedl)

### `FILIAL`

Branch/Subsidiary Indicator.

Indicates whether the workplace is a branch/subsidiary of another company.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/filial)

### `FRELFREM`

Internal/External Closure via Spinoff

Indication of whether two workplaces (one closed down and one "absorbing") come from the same company.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/frelfrem)

### `FRELTILB`

Internal/External Creation via Spinoff.

Indication of whether a created workplace (within last 2 years) belongs to the same company as the workplace from which it has been separated.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/freltilb)

### `IDTILB`

Identity change indicator.

Indicates a possible change in the identity of a workplace seen back in time, ie. between the current year and the year before.

- 'B1' = Preserved, identical 01-01-1980 31-12-3000
- 'B2' = Preserved, not identical 01-01-1980 31-12-3000
- 'O1' = newly created 01-01-1980 31-12-3000
- 'O2' = Created via separation from a workplace (min. 30% of employees and min. 2 people (v. Address change) 01-01-1980 31-12-3000
- 'O3' = Created via "takeover" of premises / buildings from a closed workplace in the same industry 01-01-1980 31-12-3000
- 'O4' = Created through transition from self-employed without employees per November (in the same industry) 01-01-1980 31-12-3000
- 'O5' = Created via transition from workplace without employees per November (in the same industry) 01-01-1980 31-12-3000
- 'SM' = Unchanged, with no employees per November also in the year before (preserved). 01-01-1980 31-12-3000
- 'T1' = New access (no connection to a workplace the year before) 01-01-1980 31-12-3000
- 'T2' = Access from work with November employees in the previous year (in the same industry) 01-01-1980 31-12-3000
- 'T3' = Access of a "fictional" entity in connection with a formal change of ownership

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/idtilb)

### `KVANDFA`

`ANDFA`, only for women.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/kvandfa)

### `KVANDHF`

`ANDHF`, only for women.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/kvandhf)

### `KVANDIF`

`ANDIF`, only for women.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/kvandif)

### `KVANDLF`

`ANDLF`, only for women.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/kvandlf)

### `LBNRFREM`

Unique serial number per workplace (`LBNR`) for the following year.

Notice that if `IDTILB` = `B1` or `B2` , the `LBNR` is preserved and therefore `LBNR` is equal to `LBNRFREM`

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/lbnrfrem)

### `LBNRTILB`

Unique serial number per workplace (`LBNR`) for the previous year.

Notice that if `IDTILB` = B1-B2 , the `LBNR` was preserved and therefore `LBNR` is equal to `LBNRTILB`

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/lbnrtilb)

### `LEDPERG`

Number of periods of unemployment that workplace generated among main employees (`PTILL` = 35-36) that worked the previous year.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/ledperg)

### `LGRGNSAR`

Average annual unemployment rate.

[TO BE DONE]

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/lgrgnsar)

### `LONAAR`

Sum of Salaries for all employees.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/lonaar)

### `LONGNS`

Average hourly salary for all main employees.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/longns)

### `LONGNSFA`

Average hourly salary for Skilled Workers in the Workplace (`PTILL` = 35).

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/longnsfa)

### `LONGNSHF`

Average hourly salary for the Highest level in the Workplace (`PTILL` = 31-33).

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/longnshf)

### `LONGNSIF`

Average hourly salary for Non-Skilled Workers in the Workplace (`PTILL` = 36).

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/LONGNSIF)

### `LONGNSLF`

Average hourly salary for "Mid-level or intermediate" workers in the Workplace (`PTILL` = 34).

[Official Documentation link](https://www.dst.dk/da/tilsalg/forskningsservice/dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/longnslf)

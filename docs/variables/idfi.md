# Company Level Database (1980-2013)



### `ARBGNR`

Workplace 12-digits Unique Code.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-arbejdssteder/arbgnr)



### `ANTALARB`

Number of workplaces in the company.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/ida-firmaer/antalarb)

### `ANTARBB`

Number of retained workplaces in the company between the current year and the year before.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/IDA-databasen/IDA-firmaer/ANTARBB)

### `FANSB`

Total number of employees in the company.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/IDA-databasen/IDA-firmaer/FANSB)

### `FANSH`

Number of _main_ employees in the company. Number of employees with main occupation in the company.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/IDA-databasen/IDA-firmaer/FANSH)

### `SARBGNRX`

1 if company largest workplace in company changed headcount, 0 otherwise.

- '0' = Unchanged employer number
- '1' = Changed employer number

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/IDA-databasen/IDA-firmaer/SARBGNRX)

### `SIDTILB`

Identity of largest workplace in the company between the current year and the year before. Categorical varaible that tracks the movement of workers from the largest workplace (e.g. HQ).

- 'B1' = Preserved, identical
- 'B2' = Preserved, not identical
- 'O1' = newly created
- 'O2' = Created via separation from a workplace (min. 30% of employees and min. 2 people (v. Address change)
- 'O3' = Created via "takeover" of premises / buildings from a closed workplace in the same industry
- 'O4' = Created through transition from self-employed without employees per November (in the same industry)
- 'O5' = Created via transition from workplace without employees per November (in the same industry)
- 'SM' = Unchanged, with no employees per November also in the year before (preserved).
- 'T1' = New access (no connection to a workplace the year before)
- 'T2' = Access from work with November employees in the previous year (in the same industry)
- 'T3' = Access of a "fictional" entity in connection with a formal change of ownership

### `SLBNR`

Serial number for largest workplace in company.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/IDA-databasen/IDA-firmaer/SLBNR)

### `STORDBXX`

6-digit industry code for largest workplace in the company. The varaible name change depending of the year of the Danish Industry Code they are using for the encoding (93', 03', 07').

- From idfi1993 to idfi2002, the variable/column is called `STORDB93`
- From idfi2003 to idfi2006, the variable/column is called `STORDB03`
- From idfi2007 onwards, the variable/column is called `STORDB07`

Check the documentation for the specific categorical encodings:

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/IDA-databasen/IDA-firmaer/STORDB03)

### `UOPLANSB`

Secondary employees in company with undisclosed workplace.

The variable must be seen in the context of the variable `FANSB` (Number of employees in the company). In this, the number of secondary employees in each company is calculated on the basis of the workplace data set (IDAS) for the given year. This includes only valid workplaces, ie. fictitious and undisclosed workplaces are not included. However, there are also secondary employees who are associated with an undisclosed workplace and who therefore do not appear in that dataset.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/IDA-databasen/IDA-firmaer/UOPLANSB)

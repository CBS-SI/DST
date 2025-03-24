# Personal Income Database (`ind`)

### `PNR`

Unique identification of person is used as key to `PERSON_ID`.

People's anonimized CPR. All CPR PNRs are converted to a unidentified PERSON_ID.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/folketal/pnr)


### `AKTIEINDK`

Stock Income (kr.)

**Available from 1980 - Present**. Income earned from stocks and dividends.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/personindkomster/aktieindk)

### `ARBFORS`

Mandatory labor market contribution payments (kr.)

**Available from 1984 - Present**. Unemployment insurance, professional quotas, early retirement and flexible benefit contributions (Rubrik52)

### `ARBLHUMV`

Unemployment benefits and education allowances (kr.)

**Available from 1980 - Present**. Payments for unemployment insurance and early retirement schemes.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/personindkomst/arblhumv)

### `BESKST`

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

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/personindkomst/beskst)

### `BESKST13`

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

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/personindkomst/beskst13)

### `BRUTTO`

Gross Income (kr.)

**Only available from 1980 to 2013**. Total taxable gross income before deductions.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/personindkomster/brutto)

### `DISPON_13`

Disposable Income (kr.) (2013 Definition).

**Available from 1980 - Present**. Income available after taxes and mandatory payments (e.g. labor market contributions). It can be negative for self-employed people. According to new 2013 definitions ([Official Documentation link](https://www.dst.dk/Site/Dst/SingleFiles/GetArchiveFile.aspx?fi=arbe&fo=rev13--pdf&ext={2})

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/personindkomst/dispon-13)

### `DISPON_NY`

Disposable Income (kr.)

**Only available from 1980 to 2013**. Updated calculation of disposable income. Please check the documentation below if you use both `DISPON_13` in combination with `DISPON_NY`

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/personindkomst/dispon-ny)

### `EJENDOMSVURDERING`

Property Assets (kr.)

**Available from 1994 - Present**. Annual valuation of owned property. The source of the variables `EJENDOMSVURDERING` and `KOEJD` are two different public registers, where the withdrawal time from the registers can cause differences in the statements from the two registers, where there should theoretically be the same value.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/personindkomst/ejendomsvurdering)

### `ERHVERVSINDK`

Business Income (kr.)

**Only available from 1994 to 2013**. Business income, salary and net profit of self-employed business incl. certain fees

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/personindkomst/erhvervsindk)

### `ERHVERVSINDK_13`

Business Income (2013 Definition).

**Available from 1980 - Present**. Business income according to new 2013 definitions ([Official Documentation link](https://www.dst.dk/Site/Dst/SingleFiles/GetArchiveFile.aspx?fi=arbe&fo=rev13--pdf&ext={2})

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/personindkomst/erhvervsindk-13)

### `ERHVERVSINDK_GL`

Business Income (kr.) (Old Definition)

**Only available from 1980 to 2013**. Replaced by the variable `ERHVERVSINDK_13`.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/personindkomst/erhvervsindk-gl)

### `FORMREST_NY05`

Net Wealth excluding pension (kr.) (2005 Definition)

**Available from 1997 - Present**. Value of all assets under 2005 definition exluding pension.

### `FORMUEINDK_BRUTTO`

Gross Capital Income (kr.)

**Available from 1980 - Present**. The gross income is the sum of interest income and other wealth income, which consists of dividends and realized losses / gains on securities. Excl. calculated rental value of own housing, as well as from 1987 excl. income from self-employment.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/Personindkomst/FORMUEINDK-BRUTTO)

### `FORMUEINDK_NY`

Capital Income (kr.) (2013 Definition)

**Only available from 1980 to 2013**. Replaced by the variable `FORMUEINDK_BRUTTO`

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/personindkomst/formueindk-ny)

### `FRADRAG`

Total Deductions (kr.)

**Available from 1980 - Present**. Deductions for private payments for pension schemes, interest expenses paid, driving deductions, maintenance and child support, expenses for unemployment insurance, professional quota, early retirement scheme, employment deduction and more.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/personindkomst/fradrag)

### `KOEJD`

Property Assets (kr.)

**Available from 1983 - Present**. Annual valuation of owned property. The source of the variables `EJENDOMSVURDERING` and `KOEJD` are two different public registers, where the withdrawal time from the registers can cause differences in the statements from the two registers, where there should theoretically be the same value.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/Personindkomst/KOEJD)

### `LOENMV`

Total salary income (kr.)

**Only available from 1980 to 2013**. Taxable salary incl. perks, tax-free pay, anniversary and severance pay, and value of stock options.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/personindkomst/loenmv)

### `LOENMV_13`

Total salary income (kr.) (2013 Definition)

**Available from 1980 - Present**. Taxable salary incl. perks, tax-free pay, anniversary and severance pay, and value of stock options.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/Personindkomst/LOENMV-13)

### `NETOVSKUD`

Net Profit (kr.)

**Only available from 1994 to 2013**.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/personindkomst/netovskud)

### `NETOVSKUD_13`

Net Profit (kr.) (2013 Definition)

**Available from 1980 - Present**. Net profit from self-employment including capital income and expenses (including interest) . Company income is self-declared B income, as opposed to salary and transfer income, which is reported to the payer's tax.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/Personindkomst/NETOVSKUD-13)

### `NETOVSKUD_GL`

Net Profit (kr.) (Old Definition)

**Only available from 1980 to 2013**.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/personindkomst/netovskud-gl)

### `OVSKEDJO2_NY`

Accommodation rental value (kr.)

**Only available from 1980 to 2006**. From 2007, this variable (estimated value) is replaced by the variable `OVSKEJD07` (calculated rental value of own housing).

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/personindkomster/ovskejd02-ny)

### `PERINDKIALT`

Total Personal Income (kr.)

**Only available from 1980 to 2013**. Total personal income excl. calculated rental value of own housing (`OVSKEJD07`) and before deduction of interest expenses.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/personindkomster/perindkialt)

### `PERINDKIALT_13`

Total Personal Income (kr.) (2013 Definition).

**Available from 1980 - Present**. Total personal income under 2013 revision. Total personal income excl. calculated rental value of own housing (`OVSKEJD07`) and before deduction of interest expenses.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/personindkomst/perindkialt-13)

### `PEROEVRIGFORMUE`

Rental Income (kr.)

Income/profits from appartments rental, holiday rental, profits from sale of real state, etc.

**Only available from from 1980 to 2013**. Replaced by `PEROEVRIGFORMUE_13`.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/personindkomster/peroevrigformue)

### `PEROEVRIGFORMUE_13`

Rental Income (kr.) (2013 Definition).

**Only available from 1980 to 2013**.Income/profits from appartments rental, holiday rental, profits from sale of real state, etc.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/personindkomst/peroevrigformue-13)

### `PERSAMLINKNETRENT_NY`

Total Personal Income with Net interest (kr.)

**Only available from 1980 to 2013**. Updated calculation of total income including deductible interest expenses on the tax bracket, deduction of labor market contributions and special pension contributions.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/personindkomst/persamlinknetrent-ny)

### `PERSONINDK`

Total Personal income without Capital income (kr.)

**Available from 1980 - Present**. Capital income is a term for the return on a person's or family's assets. This includes, for example, interest, share dividends, and realized gains and losses on shares and other securities, etc.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/Personindkomst/PERSONINDK)

### `QAKTIVF_NY05`

Total Assets (kr.) (2005 Definition).

**Available from 1995 - Present**. Value of personal active assets under 2005 definition excluding pension.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/personindkomster/qaktivf-ny05)

### `QIVARK`

Tax on Capital Income (kr.)

**Only available from 1988 - 2001**. Pleace notice that the tax percentage change depending on the years that will affect this quantity.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/Personindkomst/QAKTSKA)

### `QPASSIVN`

Liabilities to the State (kr.)

**Available from 1995 - Present**. Liabilities at year-end including mortgage debt, bank debt, or student debt (Hypotekbanken). Private debt is not included.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/Personindkomst/QPASSIVN)

### `QSPLINDK`

Taxable Income (kr.)

**Available from 1980 - Present**. All income that comes to ordinary taxation (e.g. not capital tax included) minus deductions.

For details, please check the documentation as it changes in relation with the danish legislation at the time.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/Personindkomst/QSPLINDK)

### `RENTEINDK`

Total taxable interest income from Denmark (kr.)

**Only available from 1980 - 2013**.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/personindkomst/renteindk)

### `SAMLINK_NY`

Total Personal Income (kr.)

**Only available from 1980 to 2013**. Total income incl. calculated rental value before deduction of interest expenses, and before deduction of labor market contributions and special pension contributions.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/personindkomst/samlink-ny)

### `SKATMVIALT_13`

Taxes (kr.) (2013 Definition)

**Available from 1980 - Present**. Amount of taxes corresponding to the person including labor market contribution, pension, and other (excludes church treasure).

For details, please check the documentation as it changes in relation with the danish legislation at the time.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/Personindkomst/SKATMVIALT-13)

### `SKATMVIALT_NY`

Taxes (kr.)

**Only available from 1980 - 2013**. Amount of taxes corresponding to the person including labor market contribution, pension, and other.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/personindkomst/skatmvialt-ny)

### `SKATTOT_NY`

Total Tax (kr.)

**Only available from 1980 - 2013**. The variable consists of state tax, county tax (1980-2006), health contribution (from 2007), municipal tax, church tax, wealth tax (before 1997), special income tax (before 1996), provisionally paid corporate tax (from 1987), property value tax (from 2000), state pension contribution. The final tax is calculated after deduction of various reductions and the inclusion of various tax surcharges.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/personindkomst/skattot-ny)

### `VIRKORDIND`

Business scheme Income (kr.)

**Available from 1987 - Present**. Special scheme for self-employed and artists, it gives the self-employed the opportunity to tax some of their income from the company from a year of high income to a year of low income.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/Personindkomst/VIRKORDIND)

# Generational and Inmigration data (1980-2016)


### `PNR`
Unique identification of person is used as key to `PERSON_ID`.

People's anonimized CPR. All CPR PNRs are converted to a unidentified PERSON_ID.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/folketal/pnr)

### `ALDER`

Age.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/alder)

### `FAMILIE_ID`

Basic legal family unit. All individuals have a FAMILIE_ID.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/familier/familie-id)


### `MOR_ID`

`PERSON_ID` of the person's mother.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/mor-id)

### `FAR_ID`

`PERSON_ID` of the person's father.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/far-id)

### `EFALLE`

EFALLE_ID is the social security number of the person with whom a given person lives and forms a couple in the form of marriage, registered partnership, cohabiting couples or cohabiting couples.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/forskningsservice/efalle)

### `AEGTE_ID`

Specifies the social security number ID of spouse or registered partner. There is the following connection between the person's marital status and information about the spouse:

- Married = spouse number
- Divorced = social security number of former spouse
- Widow / widower = social security number of deceased spouse
- Partnership = partner number
- Oph. partnership = social security number of former partner
- Long-term Partner = social security number of deceased partner
- Death = spouse / partner social security number

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/aegte-id)

### `BOPIKOM`

The address in the municipality (road no., house number, house letter, floor, side / door)

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/forskningsservice/bopikom)

### `KOM`

Municipal code from the National Register Address.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/kom)

### `BOP_VFRA`

Date of immigration.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/bop-vfra)

### `VAN_VTIL`

Date when immigration applies from.

A person who immigrates several times during a period is included the corresponding number of times and appears with several immigration dates.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/van-vtil)

### `CIVST`

Person's marital status (marital status). Unmarried is not included in the marital status table.

The marital code thus became from d. Oct 1 1989 expanded from 4 to 7 marital states.

- 'U' =Unmarried (not included in the marital status table)
- 'G' = Gift 'F' = Divorced
- 'E' = Widow stand The new marital status was as a result of the Registered Partnership Act
- 'P' = Registered Partnership
- 'O' = Repealed registered partnership
- 'L' = Longitudinal living of 2 partners.
- 'D' = Dead

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/civst)

### `CIV_FRA`

Date of the most recently recorded change of marital status (married, divorced, dead) of the person. Back to 2004, if `CVIST` (marital status) is equal to U (unmarried), `CIV_FRA` is set equal to the date of birth.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/folketal/civ-vfra)

### `FAMILIE_TYPE`

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

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/familie-type)

### `FM_MARK`

Person cohabitation type.

- '1' = Lives with both parents
- '2' = For children: Lives with mother who is in new couple. For adults: Living with mom.
- '3' = For children: Living with single mother. For adultsThe value does not exist.
- '4' = For children: Lives with dad who is in new couple. For adults: Living with dad.
- '5' = For children: Living with single father. For adults: The value does not exist.
- '6' = Do not live with parents

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/fm-mark)

### `FOEDREG_KODE`

Place of birth.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/folketal/foedreg-kode)

### `FOED_DAG`

Birthday.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/folketal/foed-dag)

### `IE_TYPE`

Definitions of immigrants, descendants, and people of Danish origin, which collectively comprise entire populations, are as follows:

- '1' = Danish. People, regardless of birthplace, who have at least one parent who is both a Danish citizen and born in Denmark.
- '2' = Immigrant. People born abroad. None of the parents are both Danish citizens and born in Denmark.
- '3' = Descendant. People born in Denmark. None of the parents are both Danish citizens and born in Denmark.

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/udlaendinge/ie-type)

### `GENERATION`

Whether the father and/or mother were born in Denmark or abroad.

- '0' = Danish (`IE_TYPE` = 1)
- '1' = Parents both born abroad
- '2' = Parents both born in Denmark
- '3' = One parent born in Denmark and another abroad.
- '4' = Parental information not available.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/cpr-oplysninger/generation)

### `HUSTYPE`

Household composition.

- '1' = A single man
- '2' = A single woman
- '3' = A married couple
- '4' = A few more
- '5' = A non-resident child under 18 years
- '6' = Household of several families

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/husstande/hustype)

### `KOEN`

Gender (CPR based).

- '1' = Male
- '2' = Female
- '9' = Unknown / Company

[Official Documentation link](https://www.dst.dk/da/TilSalg/Forskningsservice/Dokumentation/hoejkvalitetsvariable/folketal/koen)

### `OPR_LAND`

Citizenship / Country of origin of the person.

Encoding: [Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/nomenklaturer/lande-psd?)

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/opr-land)

### `PLADS`

A person's "place" within the couple.

- '1' = Protagonist (woman)
- '2' = Partner (man)
- '3' = Resident child

In a couple, 1 is the woman (or oldest if not man/women couple), 2 the man (or youngest if not man/women couple), 3 is a person under the age of 25 who lives at the same address as at least one of his parents who has never been married or registered partner (marital status = unmarried) and who is not a father or mother of anyone who lives or has lived in Denmark.

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/plads)

### `REG`

Region of Denmark.

- '0' = Undisclosed
- '81' = North Jutland
- '82' = Central Jutland
- '83' = Southern Denmark
- '84' = Capital Region
- '85' = Zealand

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/reg)

### `STATSB`

Citizenship / Country of origin of the person.

Codes available in the documentation (link below).

[Official Documentation link](https://www.dst.dk/da/Statistik/dokumentation/Times/moduldata-for-befolkning-og-valg/statsb)

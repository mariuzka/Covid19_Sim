set more off

*use "soep.v34\stata_de+en\raw\phrf.dta", replace

********************************************************************************

use "soep.v34\stata_de+en\bioagel.dta", replace

sort pid syear
by pid syear:  gen dup = cond(_N==1,0,_n)

drop if dup == 2

save "data\soep f�r abm\bioagel_no_dups.dta", replace

********************************************************************************

use "soep.v34\stata_de+en\pl.dta", replace

rename plb0096 homeoffice_n
rename plb0183_h work_hours_day
rename plb0186_h work_hours_week

rename plb0022_h erwerbsstatus

rename pli0040 hours_shopping // Stunden Besorgungen machen an Werktagen

rename pld0047 n_friends // Anzahl enge Freunde 
rename ple0008 health // Gegenw�rtiger Gesundheitszustand

rename pli0079 go_out // Essen, trinken gehen

rename pli0081 freq_visits_family // Besuche Familie, Verwandte
rename pli0080 freq_visits_friends // Besuche Nachbarn, Freunde

rename pli0098 freq_church // Kirchgang

rename plg0015_h stipendium

keep pid hid syear stipendium erwerbsstatus homeoffice_n work_hours_day work_hours_week n_friends health go_out freq_visits_family freq_church hours_shopping

save "data\soep f�r abm\pl_small.dta", replace

********************************************************************************

use "pequiv.dta" , replace

rename d11101 age
rename d11102ll gender
rename l11101 federal_state

rename e11106 industry1
rename e11107 industry2
rename e11101 work_hours_year

keep pid hid age gender syear federal_state industry1 industry2 work_hours_year

********************************************************************************

merge 1:1 syear pid using "soep.v34\stata_de+en\biopupil.dta"
drop _merge

********************************************************************************

merge 1:1 syear pid using "data\soep f�r abm\bioagel_no_dups.dta"
drop _merge

********************************************************************************

merge 1:1 syear pid using "data\soep f�r abm\pl_small.dta"
drop _merge

********************************************************************************

merge 1:1 syear pid using "soep.v34\stata_de+en\kidlong.dta"
drop _merge

********************************************************************************

merge 1:1 syear pid using "soep.v34\stata_de+en\pgen.dta"
drop _merge

********************************************************************************

merge m:1 syear pid using "soep.v34\stata_de+en\raw\bhp.dta"
drop _merge

********************************************************************************

merge m:1 hid using "soep.v34\stata_de+en\raw\hhrf.dta"
drop _merge

********************************************************************************

keep if syear == 2017

save "data\soep f�r abm\merged_soep_datasets.dta", replace








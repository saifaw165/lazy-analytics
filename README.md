# lazy-analytics
Automated helper functions for analysts to gather quick top level insights used in the scenario for an NPS analyst

## Functions for these involve 
### read_tableau_csv
  - Read Tableau dataset as csv is quite tempermental
### monthly_nps_pivot
  - Returns monthly nps aggregating by month. Aggregated as an average as NPS is calculated in such.
### binary_segments
  - Return binary DataFrame if data matches the specified conditions.
### item_category_nps_insight
  - Return individual persona NPS aggregated for the month 
### item_category_nps_insight_multiple
  - Return multiple persona NPS aggregated for the month 
### rolling_three_month
  - Return 3MR of a value
### verbatim_checks
  - Returns verbatim of specific factor, shown against NPS category.
### nps_calc_account
  - Return calculated NPS figure.
  - This calculation will only work effectively if we are using this with account number/ID

import pandas as pd
import numpy as np 

## Functions to do lazy analytics

def monthly_nps_pivot(monthly_nps: pd.DataFrame, nps_value:str, month_index:str) -> pd.DataFrame:
    """
    returns monthly nps aggregating by month. Aggregated as an average as NPS is calculated in such.
    """
    # pivot table to aggregate
    monthly_nps = pd.pivot_table(data=monthly_nps,index=month_index,
               values=nps_value,aggfunc='mean')
    # round nps figure 
    monthly_nps[nps_value] = monthly_nps[nps_value].round()

    return monthly_nps


def binary_segments(analysis_df: pd.DataFrame, conditions: list[tuple[str, bool]]) -> pd.DataFrame:
    """
    return binary DataFrame if data matches the specified conditions.
    
    Parameters:
    - analysis_df (pd.DataFrame): The input DataFrame.
    - conditions (List[Tuple[str, bool]]): A list of tuples, each containing a column name (segment) and a boolean value.
    
    Returns:
    - pd.DataFrame: The filtered DataFrame.
    """
    # Apply the conditions
    for segment, statement in conditions:
        analysis_df = analysis_df[analysis_df[segment] == statement]
    return analysis_df


def persona_nps_insight(segment_type: pd.DataFrame,persona: str,column:str) -> pd.DataFrame:
    """
    return individual persona NPS aggregated for the month 
    """
    # this is wrapped with the monthly nps pivot function to aggregate this in a month view 
    insights = monthly_nps_pivot(segment_type[segment_type[column]==persona])
    return insights
    

def persona_nps_insight_multiple(segment_type: pd.DataFrame,persona: list[str],column:str) -> pd.DataFrame:
    """
    return multiple persona NPS aggregated for the month 
    """
    all_insights = []
    
    # this is wrapped with the monthly nps pivot function to aggregate this in a month view 
    for items in persona:
        insights = segment_type[segment_type[column]==items]
        insights_pivot = monthly_nps_pivot(insights)
        insights_pivot[column] = items
        all_insights.append(insights_pivot)

    combined_insights = pd.concat(all_insights)

    return combined_insights



def rolling_three_month(data: pd.DataFrame,value: str) -> pd.DataFrame:
    """
    return 3MR of a value
    """
    data['3MR NPS'] = data[value].rolling(window=3).mean() 
    data['3MR NPS'] = data['3MR NPS'].round()  
    return data 



def verbatim_checks(table:pd.DataFrame,item:str,insight:str):
    """
    returns verbatim of specific factor, shown against NPS category.
    """
    final = table[table[item]==insight][['Comments','Nps Pot']]
    
    return final


def nps_calc_account(number:float):
    """
    Return calculated NPS figure. 
    This calculation will only work effectively if we are using this with account number/ID if not available resort to alternative
    function  
    """
    # for negative detractor figure
    if number < 7:
        return -100
    # for neutral passive figure
    elif number < 9:
        return 0
    # for positive promoter figure
    else:
        return 100    
    

def read_tableau_csv(tableau_csv:str) -> pd.DataFrame:
    """
    read Tableau dataset as csv is quite tempermental
    """
    dataset = pd.read_csv(tableau_csv+'.csv',encoding='utf-16',delimiter='\t')

    return dataset



